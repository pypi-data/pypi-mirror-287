import asyncio
import copy
import hashlib
import json
import re
import uuid
from base64 import b64decode
from pathlib import Path
from typing import Optional, Union, cast
from urllib.parse import unquote_plus, urlencode, urlparse, urlunparse

from aiohttp import ClientSession, FormData, WSMsgType
from bs4 import BeautifulSoup, Tag
from haralyzer import HarParser
from jsonpath import jsonpath
from lxml import etree  # type: ignore

from caseflow.callbacks.base import AsyncCaseSteoCallbackManager
from caseflow.jsonschema import generate_schema
from caseflow.model import CaseRespnseModel


def parse_har(harFilePath: Union[Path, str]) -> Path:
    """解析har文件，转换为case_step可运行的格式

    Args:
        harFilePath (Union[Path, str]): har文件路径

    Raises:
        FileExistsError: _description_

    Returns:
        Path: _description_
    """
    filePath = Path(harFilePath)
    if not filePath.exists():
        raise FileExistsError()

    # 读取HAR文件
    har_parser = HarParser.from_file(filePath)

    # 解析HAR文件
    har_data = har_parser.har_data

    interfaces = []
    # 打印所有请求的URL

    # firfox
    if har_data["creator"]["name"] in ["Firefox", "Charles Proxy", "mitmproxy"]:
        for entry in har_data["entries"]:
            with open(Path(__file__).parent.joinpath("mime.types.allow.ini"), "r") as f:
                disabled_mime_types = [
                    line.strip() for line in f.readlines() if not line.startswith(";")
                ]

            if (
                any(
                    map(
                        lambda x: x.strip() in disabled_mime_types,
                        entry.get("response")
                        .get("content", {})
                        .get("mimeType", "")
                        .split(";"),
                    )
                )
                and entry["response"]["status"]
            ):
                interfaceStep = {
                    item: entry[item]
                    for item in [
                        "request",
                        "response",
                        "_resourceType",
                        "_webSocketMessages",
                    ]
                    if item in entry
                }
                interfaceStep["stepId"] = uuid.uuid4().hex
                interfaces.append(interfaceStep)
    else:
        # edge, chrome
        for entry in har_data["entries"]:
            if (
                entry.get("_resourceType")
                in ["document", "xhr", "eventsource", "websocket"]
                and entry["response"]["status"]
            ):
                interfaceStep = {
                    item: entry[item]
                    for item in [
                        "request",
                        "response",
                        "_resourceType",
                        "_webSocketMessages",
                    ]
                    if item in entry
                }
                interfaceStep["stepId"] = uuid.uuid4().hex
                interfaces.append(interfaceStep)
    tmpPath = Path("data/tmp")
    tmpPath.mkdir(parents=True, exist_ok=True)
    parseFilePath = tmpPath.joinpath(filePath.stem + ".json")

    caseTemplateData = {
        "variables": {},
        "steps": interfaces,
        "output": {},
        "check": {"json_schema_check": True},
    }
    with open(parseFilePath, "w") as f:
        json.dump(caseTemplateData, f, ensure_ascii=False, indent=4)

    return parseFilePath


def list_to_dict(listData):
    return {item["name"]: item["value"] for item in listData}


def transfer_var(data, variables) -> Union[dict, list]:
    if isinstance(data, str) and (paramName := re.match(r"^\$\{(\w+)\}$", data)):
        return variables.get(paramName.group(1))

    if isinstance(data, (dict, list)):
        data = json.dumps(data, ensure_ascii=False)

    data = re.sub(r'"\$\{int\((\S+)\)\}"', r"\1", data)  # int in json
    newData = re.sub(
        r"\$\{\{(.+?)\}\}", r"{\1}", data.replace("{", "{{").replace("}", "}}")
    )
    newDataDict = eval(f'json.loads(fr"""{newData}""")', {"json": json}, variables)
    return newDataDict


def transfer_var_return_str(data, variables) -> str:
    if isinstance(data, (dict, list)):
        data = json.dumps(data, ensure_ascii=False)
    if "{" not in str(data):
        return data
    newData = re.sub(
        r"\$\{\{(.+?)\}\}", r"{\1}", data.replace("{", "{{").replace("}", "}}")
    )
    endSpaceFlag = False
    if newData.endswith('"'):
        newData += " "
        endSpaceFlag = True
    newStr = eval(f'fr"""{newData}"""', {"json": json}, variables)
    if endSpaceFlag:
        newStr = newStr[:-1]
    return newStr


async def run_case(
    interfaces,
    variables=None,
    cookie_jar=None,
    config=None,
    run_manager: Optional[AsyncCaseSteoCallbackManager] = None,
    streaming: bool = False,
):
    if isinstance(variables, CaseRespnseModel):
        cookie_jar = variables.cookie_jar
        variables = variables.output
    outputRule = interfaces.get("output")

    config = config or {}
    config = {**interfaces.get("config", {}), **config}

    # variables = variables or interfaces['variables']

    if variables and isinstance(variables, dict):
        variables = dict(interfaces["variables"], **variables)
    else:
        variables = interfaces["variables"]

    interfaces = interfaces["steps"]
    output = {}

    wsMsgList = []

    outputRuleFromStep = {}
    if outputRule:
        for outputKey, parseRule in outputRule.items():
            if parseRule.get("from") == "step":
                parseRuleItem = copy.deepcopy(parseRule.get("path"))
                parseRuleItem.update({"name": outputKey})
                if parseRule.get("stepId") in outputRuleFromStep:
                    outputRuleFromStep[parseRule.get("stepId")].append(parseRuleItem)
                else:
                    outputRuleFromStep[parseRule.get("stepId")] = [parseRuleItem]

    async with ClientSession(cookie_jar=cookie_jar, read_bufsize=2**20) as session:
        for stepIndex, entry in enumerate(interfaces, 1):
            run_step_manager: Optional[AsyncCaseSteoCallbackManager] = None
            if run_manager:
                run_step_id = (
                    uuid.UUID(hex=entry.get("stepId"))
                    if entry.get("stepId")
                    else uuid.uuid4()
                )
                # run_step_manager = run_manager.get_child()
                run_step_manager = await run_manager.get_child().on_case_step_start(
                    stepEntry=entry, run_id=run_step_id, stepIndex=stepIndex
                )

            allow_redirects = (
                False
                if entry["response"]["status"] in [301, 302, 303, 307, 308]
                else True
            )

            if config.get("debugStepId") and entry.get("stepId") == config.get(
                "debugStepId"
            ):
                import pdb

                pdb.set_trace()

            # 更新参数
            variablesDef = {}
            variables_ = variables
            if "input" in entry:
                for stepVarName, stepVarDef in entry["input"].items():
                    match stepVarDef["type"]:
                        case "function":
                            variablesDef[stepVarName] = eval(
                                transfer_var_return_str(
                                    stepVarDef["body"], variables=variables_
                                )
                            )
                            if stepVarDef.get("isUpdateToGlobal"):
                                variables[stepVarName] = variablesDef[stepVarName]

                variables_ = dict(variables, **variablesDef)
            else:
                variables_ = variables

            # TODO: 优化步骤逻辑判断
            if logic := entry.get("logic"):
                match logic["type"]:
                    case "if":
                        logicResult = eval(
                            transfer_var_return_str(logic["body"], variables=variables_)
                        )
                        if not logicResult:
                            if run_step_manager:
                                await run_step_manager.on_case_step_end(
                                    stepEntry=entry,
                                    stepResult=None,
                                    stepIndex=stepIndex,
                                )
                            continue
                    case _:
                        pass
            # 更新headers
            headers = list_to_dict(
                transfer_var(entry["request"]["headers"], variables=variables_)
            )
            if "Content-Length" in headers:
                headers.pop("Content-Length")
            if "content-length" in headers:
                headers.pop("content-length")
            # 删除http2.0中的:header
            if entry["request"].get("httpVersion") == "http/2.0":
                for item in list(headers.keys()):
                    if item.startswith(":"):
                        headers.pop(item)

            # 更新query params

            queryParamsDict = list_to_dict(
                transfer_var(entry["request"]["queryString"], variables=variables_)
            )

            url = entry["request"]["url"]
            url = transfer_var_return_str(url, variables=variables_)
            parsed_url = urlparse(url)
            encoded_query_params = urlencode(queryParamsDict, doseq=True)

            updated_url = urlunparse(
                (
                    parsed_url.scheme,
                    parsed_url.netloc,
                    parsed_url.path,
                    parsed_url.params,
                    encoded_query_params,
                    parsed_url.fragment,
                )
            )

            # 更新data
            requestBodyData = None
            if "postData" in entry["request"] and entry["request"]["postData"]:
                bodyContentType = headers.get("Content-Type") or headers.get(
                    "content-type"
                )
                if bodyContentType and bodyContentType.startswith(
                    "multipart/form-data"
                ):
                    # multipart/form-data
                    pass
                    formData = list_to_dict(
                        transfer_var(
                            entry["request"]["postData"].get("params"),
                            variables=variables_,
                        )
                    )
                    newData = FormData(fields=formData)
                    # handle binary data
                    for item in newData._fields:
                        type_options, _, value = item
                        if isinstance(value, str) and (
                            fileValue := value.partition("(二进制)")[-1]
                        ):
                            newData.add_field(
                                type_options.get("name"), variables_.get(fileValue)
                            )
                            newData._fields.remove(item)
                    requestBodyData = newData
                    headers.pop("Content-Type")
                elif bodyContentType and bodyContentType.startswith("application/json"):
                    data = entry["request"]["postData"].get("text", "")
                    # ${varName} 变量引用格式转换
                    newData = re.sub(
                        r"\$\{\{(.+?)\}\}",
                        r"{\1}",
                        data.replace("{", "{{").replace("}", "}}"),
                    )
                    if newData:
                        newDataDict = eval(
                            f'json.loads(fr"""{newData}""")', {"json": json}, variables_
                        )
                        requestBodyData = json.dumps(newDataDict)
                    else:
                        requestBodyData = None
                elif bodyContentType and bodyContentType.startswith(
                    "application/x-www-form-urlencoded"
                ):
                    formData = list_to_dict(
                        transfer_var(
                            entry["request"]["postData"].get("params"),
                            variables=variables_,
                        )
                    )
                    for key, value in formData.items():
                        if "%" in value:
                            formData[key] = unquote_plus(value)

                    # params replace
                    #  todo: 流程优化，统一 dict，replace ，FormData
                    if paramsReplaceList := entry.get("paramsReplace"):
                        for paramsReplace in paramsReplaceList:
                            for key, value in paramsReplace.items():
                                if key == "__update":
                                    value = transfer_var(value, variables=variables_)
                                    if isinstance(value, dict):
                                        value = {
                                            k: v
                                            for k, v in value.items()
                                            if v is not None
                                        }
                                        formData.update(**value)
                                    else:
                                        raise TypeError(
                                            "paramsReplace中key为__update时，对应的value值需为dict类型"
                                        )
                                else:
                                    # todo: normal replace
                                    pass
                        pass

                    newData = FormData(fields=formData)
                    requestBodyData = newData
                elif postDataText := entry["request"]["postData"].get("text"):
                    requestBodyData = postDataText
                else:
                    requestBodyData = None

            match entry.get("_resourceType"):
                case "document" | "xhr" | "eventsource" | None:
                    if run_step_manager:
                        await run_step_manager.on_request_start(
                            request={
                                "url": updated_url,
                                "headers": headers,
                                "session": session,
                            },
                            stepIndex=stepIndex,
                        )
                    match entry["request"]["method"]:
                        case "GET":
                            async with session.get(
                                updated_url,
                                headers=headers,
                                allow_redirects=allow_redirects,
                            ) as response:
                                if entry.get("is_stream_response"):
                                    respTextList = []
                                    firstChunk = True

                                    async for chunk in response.content:
                                        if firstChunk and run_step_manager:
                                            firstChunk = False
                                            await run_step_manager.on_request_receive_first_chunk_response(
                                                chunk=chunk, stepIndex=stepIndex
                                            )

                                        respTextList.append(chunk)

                                    respText = (
                                        b"\n".join(respTextList).decode("utf8")
                                        if respTextList
                                        else ""
                                    )
                                else:
                                    respText = await response.text()
                        case "POST":
                            async with session.post(
                                updated_url,
                                headers=headers,
                                data=requestBodyData,
                                # data=bytes(newDataStr, encoding='utf8'),
                                # json=newDataDict,
                                allow_redirects=allow_redirects,
                            ) as response:
                                if entry.get("is_stream_response"):
                                    respTextList = []
                                    firstChunk = True

                                    async for chunk in response.content:
                                        if firstChunk and run_step_manager:
                                            firstChunk = False
                                            await run_step_manager.on_request_receive_first_chunk_response(
                                                chunk=chunk, stepIndex=stepIndex
                                            )
                                        if run_step_manager:
                                            await run_step_manager.on_request_receive_chunk_end(
                                                chunk=chunk, stepIndex=stepIndex
                                            )
                                        respTextList.append(chunk)

                                    respText = (
                                        b"\n".join(respTextList).decode("utf8")
                                        if respTextList
                                        else ""
                                    )
                                else:
                                    respText = await response.text()

                        case "PUT":
                            async with session.put(
                                updated_url,
                                headers=headers,
                                data=requestBodyData,
                                # data=bytes(newDataStr, encoding='utf8'),
                                # json=newDataDict,
                                allow_redirects=allow_redirects,
                            ) as response:
                                respText = await response.text()
                        case "DELETE":
                            async with session.delete(
                                updated_url,
                                headers=headers,
                                data=requestBodyData,
                                # data=bytes(newDataStr, encoding='utf8'),
                                # json=newDataDict,
                                allow_redirects=allow_redirects,
                            ) as response:
                                respText = await response.text()
                        case "PATCH":
                            async with session.patch(
                                updated_url,
                                headers=headers,
                                data=requestBodyData,
                                # data=bytes(newDataStr, encoding='utf8'),
                                # json=newDataDict,
                                allow_redirects=allow_redirects,
                            ) as response:
                                respText = await response.text()
                        case _:
                            pass
                            continue

                    if run_step_manager:
                        await run_step_manager.on_request_end(
                            response={"resonse": response, "respText": respText},
                            stepIndex=stepIndex,
                        )

                case "websocket":
                    if run_step_manager:
                        await run_step_manager.on_websocket_shake_hands_start(
                            request={
                                "url": updated_url,
                                "headers": headers,
                                "session": session,
                            },
                            stepIndex=stepIndex,
                        )
                    async with session.ws_connect(
                        updated_url,
                        headers=headers,
                    ) as ws:

                        async def send_msg():
                            for wsmsg in entry.get("_webSocketMessages"):
                                if ws.closed:
                                    break
                                if wsmsg["type"] == "send":
                                    sendMsg = transfer_var_return_str(
                                        wsmsg["data"], variables_
                                    )
                                    if run_step_manager:
                                        await run_step_manager.on_websocket_send_start(
                                            msg=sendMsg, stepIndex=stepIndex
                                        )
                                    await ws.send_str(sendMsg)

                        async def receive_msg():
                            WEBSOCKET_RECEIVE_MSG_TIMEOUT = 60
                            firstChunk = True
                            while True:
                                try:
                                    async with asyncio.timeout(
                                        WEBSOCKET_RECEIVE_MSG_TIMEOUT
                                    ) as cm:
                                        msg = await ws.receive()

                                        if firstChunk and run_step_manager:
                                            firstChunk = False
                                            await run_step_manager.on_websokcet_receive_first_chunk_msg(
                                                chunk=msg.data, stepIndex=stepIndex
                                            )

                                        cm.reschedule(
                                            asyncio.get_running_loop().time()
                                            + WEBSOCKET_RECEIVE_MSG_TIMEOUT
                                        )
                                        wsMsgList.append(msg)
                                        if run_step_manager:
                                            isStopReceive = await run_step_manager.on_websocket_receive_end(
                                                wsMsgList=wsMsgList,
                                                stepIndex=stepIndex,
                                                ws=ws,
                                            )
                                            if isStopReceive:
                                                break
                                        if msg.type == WSMsgType.CLOSED:
                                            break
                                except TimeoutError:
                                    break

                        tasks = [
                            asyncio.create_task(send_msg()),
                            asyncio.create_task(receive_msg()),
                        ]
                        await asyncio.gather(*tasks)
                        respText = "\n".join([m.data for m in wsMsgList if m.data])
                        response = ws._response
                        if run_step_manager:
                            await run_step_manager.on_websocket_close_end(
                                response={
                                    "resonse": response,
                                    "respText": respText,
                                    "wsMsgList": wsMsgList,
                                },
                                stepIndex=stepIndex,
                            )
                case _:
                    raise TypeError(
                        f'未知请求类型：{entry.get("_resourceType")}, stepId: {entry.get("stepId")}'
                    )
            # 提取变量
            out = entry.get("out")
            if out:
                pass
                for varName, varPath in out.items():
                    match varPath["from"]:
                        case "cookies":
                            if varPath["path"] not in response.cookies:
                                raise KeyError(
                                    f"变量【{varName}】提取失败：cookies中未找到{varPath['path']}"
                                )
                            variables[varName] = response.cookies.get(
                                varPath["path"]
                            ).value  # type: ignore[reportOptionalMemberAccess]
                        case "body":
                            parseExp = transfer_var_return_str(
                                varPath["path"], variables=variables_
                            )
                            isJsonParse = True if parseExp.startswith("$") else False
                            if isJsonParse:
                                result = jsonpath(json.loads(respText), parseExp)
                                if result:
                                    variables[varName] = result[0]
                                else:
                                    variables[varName] = None
                            else:
                                # 正则提取
                                result = re.findall(parseExp, respText)
                                if result:
                                    variables[varName] = result[0]
                                else:
                                    variables[varName] = None
                        case "headers":
                            variables[varName] = response.headers.get(varPath["path"])
                        case "message":
                            if entry.get("_resourceType") == "websocket":
                                wsMsgList = [
                                    json.loads(msg.data)
                                    for msg in wsMsgList
                                    if msg.type == WSMsgType.TEXT
                                ]
                                variables[varName] = wsMsgList
                        case "html_input_tag":
                            soup = BeautifulSoup(respText, "html.parser")
                            inputTagList = (
                                soup.find_all("input")
                                + soup.find_all("select")
                                + soup.find_all("textarea")
                            )
                            # inputTagValueDict = {
                            #     item.get('name'): item.get('value')
                            #     for item in inputTagList
                            #     if item.get('name') and item.get('value') is not None
                            # }
                            inputTagValueDict = {}
                            for item in inputTagList:
                                if not item.get("name"):
                                    continue
                                if item.name == "select":
                                    selectedEle = item.findChild(
                                        "option", attrs={"selected": "selected"}
                                    )
                                    selectedEleValue = None
                                    if selectedEle:
                                        selectedEleValue = selectedEle.get("value")
                                    inputTagValueDict[item.get("name")] = (
                                        selectedEleValue
                                    )
                                else:
                                    inputTagValueDict[item.get("name")] = item.get(
                                        "value"
                                    )

                            if varPath["path"]:
                                parseExp = transfer_var_return_str(
                                    varPath["path"], variables=variables_
                                )
                                variables[varName] = inputTagValueDict.get(parseExp)
                            else:
                                variables[varName] = inputTagValueDict

                        case "html_or_xml":
                            soup = BeautifulSoup(respText, "lxml")
                            if not soup.is_xml:
                                soup = BeautifulSoup(respText, "html.parser")
                            parseExp = cast(
                                dict,
                                transfer_var(varPath["path"], variables=variables_),
                            )
                            element = soup.find(**parseExp)
                            if element:
                                if isinstance(element, Tag):
                                    variables[varName] = (
                                        element.get("value") or element.get_text()
                                    )
                                else:
                                    variables[varName] = element.get_text()
                            else:
                                variables[varName] = None
                        case "xpath":
                            html = etree.HTML(respText)
                            parseExp = transfer_var_return_str(
                                varPath["path"], variables=variables_
                            )
                            element = html.xpath(parseExp)
                            if element:
                                variables[varName] = (
                                    element[0].get("value") or element[0].text
                                )
                            else:
                                variables[varName] = None
                            pass
                        case _:
                            pass
                    if funcList := varPath.get("function"):
                        for func in funcList:
                            funcType = list(func.keys())[0]
                            funcValue = list(func.values())[0]
                            if isinstance(funcValue, list):
                                funcValue = [
                                    transfer_var_return_str(item, variables=variables_)
                                    for item in funcValue
                                ]
                            else:
                                funcValue = [
                                    transfer_var_return_str(
                                        funcValue, variables=variables_
                                    ),
                                ]
                            match funcType:
                                case "re":

                                    def re_parse(exp, index="0"):
                                        assert (
                                            variables[varName] is not None
                                        ), "正则提取失败，原始字符不能为空"
                                        assert isinstance(
                                            variables[varName], (str, bytes)
                                        ), "正则提取失败，原始字符类型不正确"
                                        # TODO: 解决re提取是原始字符串为None异常
                                        result = re.findall(exp, variables[varName])
                                        if result:
                                            if int(index) == -1:
                                                variables[varName] = result
                                            else:
                                                variables[varName] = result[int(index)]
                                        else:
                                            variables[varName] = None

                                    re_parse(*funcValue)
                                case "jsonpath":

                                    def jsonpath_parse(exp, index="0"):
                                        result = jsonpath(variables[varName], exp)
                                        if result:
                                            if int(index) == -1:
                                                variables[varName] = result
                                            else:
                                                variables[varName] = result[int(index)]
                                        else:
                                            variables[varName] = None

                                    jsonpath_parse(*funcValue)
                                case _:
                                    pass

                            pass

                stepOutputVariables = {key: variables.get(key) for key in out.keys()}
                if run_step_manager:
                    await run_step_manager.on_step_output(
                        stepEntry=entry,
                        stepIndex=stepIndex,
                        stepVariables=variables,
                        stepOutputVariables=stepOutputVariables,
                    )

            # 提取step output
            if parseRuleList := outputRuleFromStep.get(entry.get("stepId")):
                for parseRule in parseRuleList:
                    outputVarName = parseRule["name"]
                    match parseRule["from"]:
                        case "cookies":
                            if parseRule["path"] not in response.cookies:
                                raise KeyError(
                                    f"output变量【{outputVarName}】提取失败：cookies中未找到{parseRule['path']}"
                                )
                            output[outputVarName] = response.cookies.get(
                                parseRule["path"]
                            ).value  # type: ignore[reportOptionalMemberAccess]
                        case "body":
                            parseExp = transfer_var_return_str(
                                parseRule["path"], variables=variables_
                            )
                            isJsonParse = True if parseExp.startswith("$") else False
                            if isJsonParse:
                                # json 提取
                                result = jsonpath(json.loads(respText), parseExp)
                                if result:
                                    output[outputVarName] = result[0]
                                else:
                                    output[outputVarName] = None
                            else:
                                # 正则提取
                                result = re.findall(parseExp, respText)
                                if result:
                                    output[outputVarName] = result[0]
                                else:
                                    output[outputVarName] = None
                        case "headers":
                            output[outputVarName] = response.headers.get(
                                parseRule["path"]
                            )
                        case _:
                            pass
                    if funcList := parseRule.get("function"):
                        for func in funcList:
                            funcType = list(func.keys())[0]
                            funcValue = list(func.values())[0]
                            funcValue = transfer_var_return_str(
                                funcValue, variables=variables_
                            )
                            match funcType:
                                case "re":
                                    result = re.findall(
                                        funcValue, output[outputVarName]
                                    )
                                    if result:
                                        output[outputVarName] = result[0]
                    if streaming:
                        yield CaseRespnseModel(
                            output={outputVarName: output[outputVarName]},
                            cookie_jar=session.cookie_jar,
                        )
            if run_step_manager:
                await run_step_manager.on_step_check(
                    stepEntry=entry,
                    stepResponse=response,
                    stepRespText=respText,
                    stepIndex=stepIndex,
                )
            # 校验响应码
            skip_check_response_status = [304]
            if entry["response"]["status"] not in skip_check_response_status:
                assert response.status == entry["response"]["status"], (
                    f'check step: {stepIndex}, stepId: {entry.get("stepId")}, url: {entry["request"]["url"]}\n'
                    f"响应状态码与预期不符。\n"
                    f"预期值: {entry['response']['status']}\n"
                    f"实际值: {response.status}"
                )
            # 校验结构
            json_schema_check_global = config.get("check", {}).get(
                "json_schema_check", True
            )
            if (
                json_schema_check_global
                and (
                    "application/json" in response.headers.get("Content-Type", "")
                    or "application/json" in response.headers.get("content-type", "")
                )
                and "text" in entry["response"]["content"]
            ):
                if not entry.get("check", {}).get("json_schema_check", {}).get("skip"):
                    if respEncoding := entry["response"]["content"].get("encoding"):
                        match respEncoding:
                            case "base64":
                                schemeStandard = generate_schema(
                                    b64decode(entry["response"]["content"]["text"]),
                                    depth=None,
                                )
                            case _:
                                schemeStandard = generate_schema(
                                    entry["response"]["content"]["text"], depth=None
                                )
                    else:
                        schemeStandard = generate_schema(
                            entry["response"]["content"]["text"], depth=None
                        )
                    schemeActual = generate_schema(respText, depth=None)
                    assert (
                        hashlib.sha256(str(schemeStandard).encode()).hexdigest()
                        == hashlib.sha256(str(schemeActual).encode()).hexdigest()
                    ), (
                        f'check step: {stepIndex}, stepId: {entry.get("stepId")}, url: {entry["request"]["url"]}\n'
                        f"响应报文结构与预期报文结构不一致。\n"
                        f"预期报文结构: {schemeStandard}\n"
                        f"实际报文结构: {schemeActual}"
                    )

            # callback
            # clean cookie for logout
            if entryCallback := entry.get("callback"):
                if entryCallback.get("clear_cookies"):
                    session.cookie_jar.clear()
                    # TODO: clear_domain

            if run_step_manager:
                stepResult = None
                if out := entry.get("out"):
                    stepResult = {key: variables.get(key) for key in out.keys()}
                await run_step_manager.on_case_step_end(
                    stepEntry=entry, stepResult=stepResult, stepIndex=stepIndex
                )
            # break step
            if break_step_logic := entry.get("break_step"):
                breakFlag = False
                if break_step_logic.get("body"):
                    breakFlag = eval(
                        transfer_var_return_str(
                            break_step_logic["body"], variables=variables_
                        )
                    )
                if breakFlag:
                    break

    # 返回定义的out参数
    if outputRule:
        for outputKey, parseRule in outputRule.items():
            if parseRule.get("from") == "variables":
                output[outputKey] = variables.get(parseRule.get("path"))
                if streaming:
                    yield CaseRespnseModel(
                        output={outputKey: output[outputKey]},
                        cookie_jar=session.cookie_jar,
                    )
    yield CaseRespnseModel(output=output, cookie_jar=session.cookie_jar)


def run_case_define_case_file(func, filePath):
    async def wrapper(*args, **kwars):
        interfaces = load_parse_http_file(filePath)
        return await func(interfaces, *args, **kwars)

    return wrapper


def load_parse_http_file(filePath):
    with open(filePath, "r", encoding="utf8") as f:
        interfaces = json.load(f)
        return interfaces


async def concurrent_run_case(interfaces):
    async def run_async_generator():
        gen = run_case(interfaces)
        result = None
        try:
            while True:
                result = await anext(gen)
        except StopAsyncIteration:
            pass
        return result

    tasks = [asyncio.create_task(run_async_generator()) for _ in range(1)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
