from llm.get_tongyi_llm import tongyi_llm as llm
from langchain.agents import initialize_agent, Tool, create_structured_chat_agent, AgentExecutor
from langchain_core.tools import BaseTool, StructuredTool, Tool, tool
# from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType
from tools.tools import create_file, read_from_file
from langchain_core.pydantic_v1 import BaseModel, Field

class WriteFile(BaseModel):
    file_path: str = Field()
    content: str = Field()
    pass
class ReadFile(BaseModel):
    file_path: str = Field()
    pass

createFile = StructuredTool(
        name="创建文件",
        func=create_file,
        description="当需要写文件时",
        args_schema=WriteFile,
    )
readFile = StructuredTool(
        name="阅读文件",
        func=read_from_file,
        description="当尝试阅读文件时",
        args_schema=ReadFile,
    )

tools = [readFile]
# tools = [readFile, createFile]
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True
)
test_file = '/Users/ever/workspace/data-management-platform-frontend/src/type/enum.ts'
agent.invoke("阅读"+test_file+"文件，并输出完整内容")
# agent.invoke("阅读"+test_file+"文件，向其中的"
#       "DICTYPENAMES枚举值追加一个枚举成员：地区类型(AREA_TYPE)，并输出更新后的完整内容")