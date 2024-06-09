import main
from langchain_community.llms import Tongyi
DASHSCOPE_API_KEY=main.DASHSCOPE_API_KEY

tongyi_llm = Tongyi(temperature=1)