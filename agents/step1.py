from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import tongyi_llm as llm
from crewai_tools import (FileReadTool)
from tools.output_read_tool import OutputReadTool

file1='/Users/ever/workspace/data-management-platform-frontend/src/router/dict/index.ts'
file2='/Users/ever/workspace/data-management-platform-frontend/src/views/dictionary/config/configs.tsx'

file_reader = Agent(
    role="前端开发专家，精通vue、typescript",
    goal="理解文件内容，根据需求正确修改文件",
    backstory='需要根据新增的内容，给各个文件文件添加相关配置',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)
read_task = Task(
    description='项目中的字典类型DICTYPENAMES增加了一个枚举成员：参数类型(CT_PARAM_TYPE)，请阅读文件{file}，'
                '分析出需要添加配置的对象以及需要增加的代码',
    expected_output='请输出需要修改的对象名称以及新增的代码内容',
    agent=file_reader
)

output_printer = Agent(
    role="前端开发专家，精通vue、typescript",
    goal="根据分析得出的需要添加配置的对象以及新增的代码内容，对文件{file}进行修改",
    backstory="根据分析得出的需要添加配置的对象以及新增的代码内容，对文件{file}进行修改",
    llm=llm,
    tools=[OutputReadTool()],
    allow_delegation=False
)
output_printer_task = Task(
    description='根据分析得出的需要添加配置的对象、新增的代码内容，对{file}进行修改',
    expected_output='修改后的文件内容',
    agent=output_printer
)

my_crew = Crew(
    agents=[file_reader, output_printer],
    tasks=[read_task, output_printer_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
result = my_crew.kickoff(inputs={"file": file1})
print('my_crew.usage_metrics', my_crew.usage_metrics)
print('***the result***')
print(result)
print('***the result***')