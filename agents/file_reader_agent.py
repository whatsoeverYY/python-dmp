from crewai import Agent
from llm.get_tongyi_llm import custom_llm
from tools.file_read_tool import FileReadTool

llm = custom_llm

'''
role：精通vue 和 TS的前端开发专家
goal：阅读并理解给出的文件内容，根据任务说明给出正确的代码
'''
file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Read and understand the provided files, "
         "and provide the correct code according to the task instructions.",
    backstory='A front-end project based on Vue and TypeScript is under development.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)