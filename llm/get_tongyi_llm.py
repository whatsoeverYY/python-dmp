import main
from langchain_community.llms import Tongyi
DASHSCOPE_API_KEY=main.DASHSCOPE_API_KEY
from llm.custom_llm import CustomLLM

custom_llm = CustomLLM()

tongyi_llm = Tongyi(
    model_name='qwen-max',
    temperature=0
)

tongyi_llm_plus = Tongyi(
    model_name='qwen-plus',
    temperature=0
)

# custom_llm = tongyi_llm