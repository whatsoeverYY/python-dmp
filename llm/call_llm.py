from openai import _ModuleClient as OpenAI
import main

DASHSCOPE_API_KEY = main.DASHSCOPE_API_KEY


def get_answer(content: str) -> str:
    client = OpenAI(
        api_key=DASHSCOPE_API_KEY,  # 替换成真实DashScope的API_KEY
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务endpoint
    )

    completion = client.chat.completions.create(
        model="qwen-long",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': content
                # 'content': '大型语言模型(llm)已经彻底改变了人工智能领域，使以前被认为是人类独有的自然语言处理任务成为可能...'
            },
            # {
            #     'role': 'user',
            #     'content': '文章讲了什么？'
            # }
        ],
        stream=False
    )
    print('answer: ', completion.choices[0].message.content)
    # for chunk in completion:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].dict())
    return completion.choices[0].message.content
