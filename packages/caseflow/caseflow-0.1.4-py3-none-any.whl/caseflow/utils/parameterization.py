import re
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

from caseflow.model import CaseFlowModel, InterfaceStepRequestModel
from pydantic_core import ValidationError


@dataclass
class ParamPosition:
    stepId: str
    position: List[Union[str, int]]


def find_param_first_position(cfm: CaseFlowModel, param: str) -> ParamPosition:
    """获取参数第一次出现的位置

    Args:
        cfm (CaseFlowModel): _description_
        param (str): _description_

    Raises:
        LookupError: _description_

    Returns:
        ParamPosition: _description_
    """
    result = re.search(
        rf'{param}(?:(?!stepId).)*"stepId":(?:\s+)?"(?P<stepId>\w+)"',
        cfm.model_dump_json(),
        re.DOTALL,
    )
    if not result:
        raise LookupError("参数未找到")
    stepId = result.group("stepId")
    stepModel = [step for step in cfm.steps if step.stepId == stepId][0]

    inRequest = re.search(param, stepModel.request.model_dump_json())
    position = []
    if inRequest:
        position.append("request")
        for field in stepModel.request.model_fields_set:
            print(field)
            filedValue = getattr(stepModel.request, field)
            if hasattr(filedValue, "model_dump_json"):
                if re.search(
                    param, getattr(stepModel.request, field).model_dump_json()
                ):
                    position.append(field)
                    break
            else:
                if re.search(param, str(getattr(stepModel.request, field))):
                    position.append(field)
                    break
    else:
        position.append("response")
        for field in stepModel.response.model_fields_set:
            filedValue = getattr(stepModel.response, field)
            if hasattr(filedValue, "model_dump_json"):
                if re.search(
                    param, getattr(stepModel.response, field).model_dump_json()
                ):
                    position.append(field)
                    break
            else:
                if re.search(param, str(getattr(stepModel.response, field))):
                    position.append(field)
                    break
    paramPosition = ParamPosition(stepId=stepId, position=position)
    return paramPosition


def replace_param(param: str, replace: str, cfm: CaseFlowModel):
    """替换caseflowModel参数

    Args:
        param (str): _description_
        replace (str): _description_
        cfm (CaseFlowModel): _description_
    """
    if not re.match("$\{\w+\}", replace):
        replace = f"${{{replace}}}"
    for index, step in enumerate(cfm.steps):
        if isContainsParamCheck(param, step.request.model_dump_json()):
            # only replace request
            try:
                newStep = step.request.model_dump_json().replace(param, replace)
                step.request = InterfaceStepRequestModel.model_validate_json(newStep)
                print(f"replace {index}, {step.stepId}")
            except ValidationError:
                # replace_ = replace[:2] + 'int(' + replace[2:-1] + ')' + replace[-1:]
                replace_ = f'"${{int({replace})}}"'
                newStep = step.request.model_dump_json().replace(param, replace_)
                step.request = InterfaceStepRequestModel.model_validate_json(newStep)
                print(f"replace {index}, {step.stepId}")
                pass
            except Exception:
                print(traceback.format_exc())
    return cfm


def isContainsParamCheck(param, content):
    return True


def save_caseflow(cfm: CaseFlowModel, file: Path):
    file.write_text(
        cfm.model_dump_json(
            indent=4, by_alias=True, exclude_defaults=True, exclude_none=True
        ),
    )


def load_caseflow(file: Path) -> CaseFlowModel:
    return CaseFlowModel.model_validate_json(file.read_text())
