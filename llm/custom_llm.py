from typing import Any, List, Mapping, Optional
import main
import requests
import json
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain.llms.base import LLM
from llm.utils import enforce_stop_tokens

headers = {
    "Content-Type": "application/json",
    "Authorization": main.CHAT_AUTHORIZATION,
    'X-Ai-Engine': main.CHAT_ENGINE
}


def chat_completion(message):
    payload = {
        "model": main.CHAT_MODEL,
        "messages": message,
        "max_tokens": main.CHAT_MAX_TOKEN,
        "temperature": 0
    }
    response = requests.post(main.CHAT_URL, headers=headers, data=json.dumps(payload))
    res = response.json()
    print('-------------------- 接口返回 start --------------------')
    print(res["data"]["message"])
    print('-------------------- 接口返回 end --------------------')
    return res["data"]["message"]


if __name__ == '__main__':
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': 'hello'
        },
    ]
    chat_completion(messages)


class CustomLLM(LLM):
    model_name: str = "gpt-4o"

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> ChatResult:
        message = [
            {
                'role': 'user',
                'content': prompt
            }
        ]
        # print('-------------------- here is the prompt start --------------------')
        # print(prompt[0:2000])
        # print('-------------------- here is the prompt end --------------------')
        text = chat_completion(message)
        if stop is not None:
            text = enforce_stop_tokens(text, stop)

        # 初始化generation对象， 对里面的content指定值进行处理
        # generation = ChatGeneration(message={"content": text, "type": "answer"})
        # 最近返回ChatResult形式的消息结果
        # chatResult = ChatResult(generations=[generation])
        # print(chatResult)
        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_name": self.model_name, **super()._identifying_params}
