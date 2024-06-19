from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import tongyi_llm
from crewai_tools import (FileReadTool)
from tools.output_update_tool import OutputUpdateTool

llm = tongyi_llm

file1 = '/Users/ever/workspace/data-management-platform-frontend/src/router/dict/index.ts'
file2 = '/Users/ever/workspace/data-management-platform-frontend/src/locales/cn.ts'
file3 = '/Users/ever/workspace/data-management-platform-frontend/src/views/dictionary/config/configs.tsx'
file4 = '/Users/ever/workspace/data-management-platform-frontend/src/views/dictionary/config/dictionary.tsx'

file_reader = Agent(
    role="一个前端开发专家，精通vue、typescript",
    goal="理解文件内容，根据需求正确分析出需要修改的对象以及新增的代码",
    backstory='有一个基于Vue和TypeScript的前端项目在开发中',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)
file_updater = Agent(
    role="前端开发专家，精通vue、typescript",
    goal="根据分析得出的需要添加配置的对象以及新增的代码内容，对文件{file}进行修改",
    backstory="项目文件中有一个变量进行了更新，需要对给定的文件进行相应的配置添加",
    llm=llm,
    tools=[OutputUpdateTool()],
    allow_delegation=False
)
read_task = Task(
    description='项目中的字典类型DICTYPENAMES增加了一个枚举成员：参数类型(CT_PARAM_TYPE)，请阅读文件{file}，'
                '分析出该文件中需要添加配置的对象以及需要新增的代码，不要包含文件中已有的代码内容',
    expected_output='请输出该文件中需要修改的对象名称以及新增的代码内容，不要包含文件中已有的代码内容',
    agent=file_reader
)

file_update_task = Task(
    description='根据分析得出的需要添加配置的对象、新增的代码内容，使用工具对{file}进行修改',
    expected_output='请输出修改后的文件内容',
    agent=file_updater
)

my_crew = Crew(
    agents=[file_reader, file_updater],
    tasks=[read_task, file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
result = my_crew.kickoff(inputs={"file": file1})
print('my_crew.usage_metrics', my_crew.usage_metrics)
print('***the result***')
print(result)
print('***the result***')