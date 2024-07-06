from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import tongyi_llm
from tools.file_create_tool import FileCreateTool

llm = tongyi_llm

file_reader = Agent(
    role="前端开发专家，精通Vue和Typescript",
    goal="阅读并理解提供给你的代码文件，能够据此为新模块创建新文件",
    backstory='有一个基于Vue和TypeScript的前端项目正在开发中，需要根据提供的模板代码开发一个新模块',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)

read_task = Task(
    description='项目需要添加一个新模块：{new_module.}'
                '请阅读如下代码，遵循其中的TEMPLATE_CODE(模块代码)部分，为新模块创建一个新文件{file_path}'
                '请确保所有的template code部分都被替换，包括templateCode, TemplateCode, template_code等等'
                '最后根据生成的代码内容创建新文件{file_path}'
                '"""'
                '{file}'
                '"""',
    expected_output='新模块的完整代码，不需要用```包裹'
                    '确保回答中的Action Input部分的格式始终如下：'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileCreateTool()]
)

my_crew_cn = Crew(
    agents=[file_reader],
    tasks=[read_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
