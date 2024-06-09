from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import tongyi_llm as llm
from tools.file_write_tool import FileWriteTool
from crewai_tools import (FileReadTool)

file_reader = Agent(
    role="前端开发专家，精通vue、typescript",
    goal="理解文件内容",
    backstory='',
    llm=llm,
    tools=[FileReadTool()]
)

file_writer = Agent(
    role='writer',
    goal='将内容写入文件中',
    backstory='',
    llm=llm,
    tools=[FileWriteTool()],
    verbose=True
)
file='/Users/ever/Documents/AI/projects/ai-projects/automatic-generate-code-for-dmp/hello.js'
read_task = Task(
    description='阅读文件'+file+', 在DICTYPENAMES枚举中增加一个枚举类型：测试类型(TEST_TYPE)',
    expected_output='修改后的文件内容',
    agent=file_reader
)
write_task = Task(
    description='将修改后的内容写入文件'+file+'中',
    expected_output='修改内容后的文件hello.js',
    agent=file_writer
)
my_crew = Crew(
    agents=[file_reader, file_writer],
    tasks=[read_task, write_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
result = my_crew.kickoff()
print('my_crew.usage_metrics', my_crew.usage_metrics)
print('result', result)