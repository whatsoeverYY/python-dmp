from llm.get_tongyi_llm import tongyi_llm as llm
from langchain.agents import initialize_agent, Tool
from langchain_core.tools import BaseTool, StructuredTool, Tool, tool
# from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType
from tools.tools import create_file
from langchain_core.pydantic_v1 import BaseModel, Field

class File(BaseModel):
    file_path: str = Field()
    content: str = Field()
    pass

createFile = StructuredTool(
        name="创建文件",
        func=create_file,
        description="需要写文件",
        args_schema=File,
    )

tools = [createFile]
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)

agent("将aaaa写入/Users/ever/Documents/AI/projects/ai-projects/automatic-generate-code-for-dmp/agents.py/readme文件中")