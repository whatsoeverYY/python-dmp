from typing import Any, List, Mapping, Optional
import main
import requests
import os
import json
import logging
import datetime
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
    if '```python' in res["data"]["message"] or '```json' in res["data"]["message"]:
        raise Exception("Action Input格式错误，请重试")
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


def setup_logger(output_filename):
    """配置并返回一个新的logger实例"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 创建一个handler，用于写入日志文件
    log_file_name = os.path.join('logs', output_filename)
    handler = logging.FileHandler(log_file_name)
    handler.setLevel(logging.INFO)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(handler)

    return logger


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
        # now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # 获取当前时间并格式化为字符串
        # log_file_name = f"function_output_{now}.log"  # 动态生成日志文件名

        # 设置并获取logger实例
        # logger = setup_logger(log_file_name)
        # logger.info(prompt)

        text = chat_completion(message)
        if stop is not None:
            text = enforce_stop_tokens(text, stop)

        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_name": self.model_name, **super()._identifying_params}
