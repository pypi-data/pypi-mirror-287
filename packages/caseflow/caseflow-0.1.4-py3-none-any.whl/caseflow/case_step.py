import asyncio
import traceback
from pathlib import Path
from typing import Any, AsyncIterator, Dict, List, Optional, TypeAlias, Union

from langchain.globals import set_debug
from langchain_core.callbacks.base import Callbacks
from langchain_core.runnables import RunnableSerializable
from langchain_core.runnables.config import RunnableConfig, ensure_config

from caseflow.callbacks.base import AsyncCaseSteoCallbackManager
from caseflow.run_case import load_parse_http_file, run_case

from .model import CaseRespnseModel

CaseStepInput = Union[Dict, CaseRespnseModel]
CaseStepOutput: TypeAlias = CaseRespnseModel


class CaseStep(RunnableSerializable[CaseStepInput, CaseStepOutput]):
    metadata: Optional[Dict[str, Any]] = None
    """Metadata to be used for tracing."""
    tags: Optional[List[str]] = None
    """Tags to be used for tracing."""
    callbacks: Callbacks = None
    verbose: bool = False
    interfaces: Optional[dict] = None
    step_json_file_path: Optional[Union[Path, str]] = None

    class Config:  # type: ignore
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def invoke(
        self, input: CaseStepInput, config: RunnableConfig | None = None, **kwargs
    ) -> CaseStepOutput:
        config = ensure_config(config)
        if self.metadata:
            config["metadata"] = {**config.get("metadata", {}), **self.metadata}
        if self.tags:
            config["tags"] = config.get("tags", []) + self.tags
        # return self._call_with_config(
        #     self._invoke, input, config, run_type="casestep", **kwargs
        # )
        return self._invoke(input=input, config=config, **kwargs)

    def _invoke(self, input, config=None, **kwargs):
        self.load_innterface_step_from_file()
        with asyncio.Runner() as runner:
            result = runner.run(self.ainvoke(input=input, config=config, **kwargs))
            return result

    async def ainvoke(
        self, input: CaseStepInput, config: RunnableConfig | None = None, **kwargs
    ) -> CaseStepOutput:
        config = ensure_config(config)
        if self.metadata:
            config["metadata"] = {**config.get("metadata", {}), **self.metadata}
        if self.tags:
            config["tags"] = config.get("tags", []) + self.tags
        caseResult = await self._ainvoke(input=input, config=config, **kwargs)
        return caseResult

    async def _ainvoke(self, input, config=None, **kwargs):
        self.load_innterface_step_from_file()
        if "streaming" not in kwargs:
            kwargs["streaming"] = False
        resultLis = []
        async for chuck in self.astream(input=input, config=config, **kwargs):
            resultLis.append(chuck)
        # return await run_case(
        #     self.interfaces,
        #     variables=input,
        #     config=config,
        #     run_manager=case_step_run_manager,
        # )
        return resultLis[-1]

    def load_innterface_step_from_file(self):
        if self.interfaces:
            return
        if self.step_json_file_path:
            self.interfaces = load_parse_http_file(self.step_json_file_path)

    async def astream(
        self,
        input: CaseStepInput,
        config: RunnableConfig | None = None,
        **kwargs: Any | None,
    ) -> AsyncIterator[CaseStepOutput]:
        self.load_innterface_step_from_file()
        config = ensure_config(config)
        if self.metadata:
            config["metadata"] = {**config.get("metadata", {}), **self.metadata}
        if self.tags:
            config["tags"] = config.get("tags", []) + self.tags

        callbacks = config.get("callbacks")
        tags = config.get("tags")
        metadata = config.get("metadata")
        verbose = kwargs.get("verbose")
        if kwargs.get("streaming") is None:
            streaming = True
        else:
            streaming = kwargs.pop("streaming")
        if not self.verbose and verbose is not None:
            verbose_ = verbose
        else:
            verbose_ = self.verbose
        callback_manager = AsyncCaseSteoCallbackManager.configure(
            callbacks,
            self.callbacks,
            verbose_,
            tags,
            self.tags,
            metadata,
            self.metadata,
        )
        run_manager = await callback_manager.on_case_start(caseInfo=self.caseInfo)

        async def input_aiter() -> AsyncIterator[CaseStepInput]:
            yield input

        chunk = CaseStepOutput()
        try:
            async for chunk in self._atransform_stream_with_config(
                input_aiter(),
                self._astream,
                config=config,
                streaming=streaming,
                case_step_run_manager=run_manager,
                **kwargs,
            ):
                yield chunk
        except Exception as e:
            await run_manager.on_case_error(caseInfo=self.caseInfo, error=e)
            print(traceback.format_exc())
            raise Exception(traceback.format_exc()) from e
        else:
            await run_manager.on_case_end(caseInfo=self.caseInfo, caseResult=chunk)

    async def _astream(
        self, input, config, streaming=True, **kwargs
    ) -> AsyncIterator[CaseStepOutput]:
        case_step_run_manager = kwargs.get("case_step_run_manager")
        cookie_jar = kwargs.get("cookie_jar")
        async for chunk in run_case(
            self.interfaces,
            variables=await anext(input),
            cookie_jar=cookie_jar,
            config=config,
            run_manager=case_step_run_manager,
            streaming=streaming,
        ):
            yield chunk

    @property
    def caseInfo(self):
        return self.dict()


if __name__ == "__main__":
    import os

    from langchain_core.globals import set_debug

    os.environ["tracing_callback_v2"] = "true"
    # set_verbose(True)
    set_debug(True)
    c = CaseStep(step_json_file_path="data/json/lmaip/lmaip.login.json")

    async def test():
        async for chuck in c.astream({}):
            print(chuck)

    result = asyncio.run(test())
    # result = asyncio.run(
    #     c.ainvoke(
    #         {},
    #         config={
    #             "callbacks": [
    #                 CaseStepStdOutCallbackHandler(),
    #             ]
    #         },  # type: ignore
    #     )
    # )
    print(result)
