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


def extract_from_text(text, content):
    try:
        # Find the position of the marker in the text
        start_index = content.index(text) + len(text)
        # Extract and return the substring after the marker
        return content[start_index:].strip()
    except ValueError:
        # If the marker is not found in the text, return an empty string or an appropriate message
        return "Marker 'Final Answer:' not found in the text."


def chat_completion(message, reused):
    payload = {
        "model": main.CHAT_MODEL,
        "messages": message,
        "max_tokens": main.CHAT_MAX_TOKEN,
        "temperature": 0
    }
    response = requests.post(main.CHAT_URL, headers=headers, data=json.dumps(payload))
    res = response.json()
    print('-------------------- 接口返回 res --------------------')
    print(res)
    print('-------------------- 接口返回 res --------------------')
    res_mes = res["data"]["message"]
    print('-------------------- 接口返回 start --------------------')
    print(res["data"]["message"])
    if '```python' in res["data"]["message"] or '```json' in res["data"]["message"]:
        print('-------------------- 接口返回 start 替换``` --------------------')
        replaced_res = res_mes.replace('```python', '').replace('```json', '').replace('```typeScript', '').replace('```', '')
        print(replaced_res)
        return replaced_res
    if reused:
        print('-------------------- 接口返回 start 调整Final Answer: --------------------')
        replaced_res = '''Thought: I now know the final answer'
Final Answer:
''' + extract_from_text('Final Answer:', res_mes)
        print(replaced_res)
        return replaced_res
    print('-------------------- 接口返回 end --------------------')
    return res_mes


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

        if_reused = main.TASK_REPEAT_USAGE in prompt

        if if_reused:
            print('-------------------- custom llm prompt - TASK_REPEAT_USAGE --------------------')
        print('-------------------- custom llm prompt - here is the output content Start --------------------')
        print(prompt)
        print('-------------------- custom llm prompt - here is the output content End --------------------')

        text = chat_completion(message, if_reused)
        if stop is not None:
            text = enforce_stop_tokens(text, stop)

        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_name": self.model_name, **super()._identifying_params}
