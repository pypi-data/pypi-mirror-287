from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, TypeAlias, Union

from aiohttp.abc import AbstractCookieJar
from pydantic import BaseModel, Field

# ScriptStepModel = TypeVar("ScriptStepModel")

OutVarName: TypeAlias = str


class CaseRespnseModel(BaseModel):
    output: Optional[Dict[OutVarName, Any]] = None
    cookie_jar: Optional[AbstractCookieJar] = None

    class Config:
        arbitrary_types_allowed = True


class CaseFlowModel(BaseModel):
    variables: Dict
    # steps: List[Union[InterfaceStepModel, ScriptStepModel]]
    steps: List[InterfaceStepModel]
    output: Optional[Dict[OutVarName, CaseOutVarExtractModel]]
    check: CaseFlowCheckModel
    version: Optional[str] = None


class CaseFlowOutPutModel(BaseModel):
    pass


class CaseFlowCheckModel(BaseModel):
    json_schema_check: bool = True


class InterfaceStepModel(BaseModel):
    request: InterfaceStepRequestModel
    response: InterfaceStepResponseModel
    _resourceType: Optional[str] = None
    _webSocketMessages: Optional[List[Dict[str, Any]]] = None
    stepId: str
    input_: Optional[Dict] = Field(default=None, alias="input")
    out: Optional[Dict[OutVarName, InterfaceStepOutVariableExtractModel]] = None
    logic: Optional[StepLogicModel] = None


class InterfaceStepInputVariableExtractModel(BaseModel):
    type_: OutVarExtractFromEnum = Field(..., alias="type")
    body: str
    isUpdateToGlobal: Optional[bool] = None


class InputVarGenerateEnum(Enum):
    FUNCTION = "function"


class StepLogicModel(BaseModel):
    type_: StepLogicEnum = Field(..., alias="type")
    body: str


class StepLogicEnum(Enum):
    IF = "if"


class InterfaceStepOutVariableExtractModel(BaseModel):
    from_: OutVarExtractFromEnum = Field(..., alias="from")
    path: str
    function: Optional[List[OutVarExtractPostFunctionModel]] = None


class OutVarExtractFromEnum(Enum):
    COOKIES = "cookies"
    BODY = "body"
    HEADERS = "headers"
    MESSAGE = "message"
    HTML_INPUT_TAG = "html_input_tag"
    HTML_OR_XML = "html_or_xml"
    XPATH = "xpath"


class CaseOutVarExtractModel(BaseModel):
    from_: CaseOutVarExtractEnum = Field(..., alias="from")

    # 存在stepId时，path是InterfaceStepOutVariableExtractModel
    path: Union[str, InterfaceStepOutVariableExtractModel]
    function: Optional[List[OutVarExtractPostFunctionModel]] = None
    stepId: Optional[str] = None


class CaseOutVarExtractEnum(Enum):
    COOKIES = "cookies"
    BODY = "body"
    HEADERS = "headers"
    VARIABLES = "variables"


class OutVarExtractPostFunctionEnum(Enum):
    RE = "re"
    JSONPATH = "jsonpath"


VarExtractExpressionStr: TypeAlias = str
VarExtractIndexStr: TypeAlias = Union[int, str]
VarExtractExpressionWithIndexTuple = Tuple[VarExtractExpressionStr, VarExtractIndexStr]
VarExtractExpressionOrWithIndex = Union[
    VarExtractExpressionStr, VarExtractExpressionWithIndexTuple
]


class OutVarExtractPostFunctionModel(BaseModel):
    re: Optional[VarExtractExpressionOrWithIndex] = None
    jsonpath: Optional[VarExtractExpressionOrWithIndex] = None


class InterfaceStepRequestModel(BaseModel):
    method: str
    url: str
    httpVersion: str
    headers: Optional[List[Dict[str, Any]]] = None
    queryString: Optional[List[Dict[str, Any]]] = None
    cookies: Optional[List[Dict[str, Any]]] = None
    headersSize: int
    bodySize: int
    postData: Optional[Dict[str, Any]] = None


class InterfaceStepResponseModel(BaseModel):
    status: int
    statusText: str
    httpVersion: str
    headers: Optional[List[Dict[str, Any]]] = None
    cookies: Optional[List[Dict[str, Any]]] = None
    content: Dict
    redirectURL: Optional[str] = None
    headersSize: int
    bodySize: int
    _transferSize: int
    _error: Optional[Any] = None


class InterfaceStepResponseContentModel(BaseModel):
    size: int
    mimeType: str
    compression: int
    text: str
