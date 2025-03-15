from langchain_core.language_models import LLM
from typing import Any, List, Mapping, Optional
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun


class myLLm(LLM):

    @property
    def _llm_type(self) -> str:
        return "zzyAI"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        pd = prompt.find("吗")
        if pd >= 0:
            return "这是个提问"
        return "哦."

llm = myLLm()
response = llm.invoke("你好吗")
print(response)
