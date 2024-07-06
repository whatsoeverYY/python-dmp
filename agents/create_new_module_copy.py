from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from tools.file_create_tool import FileCreateTool

llm = custom_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Reading the code file provided, Understand the content of the provided template code and "
         "correctly figure out the new code and create a new file for the new module.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to develop a new module basing on the provided template code.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)

read_task = Task(
    description="A new module need to be added into the project: {new_module}."
                'Please read the code file below, following the TEMPLATE_CODE(模块代码) part of the code,'
                'write a new file {file_path} for the new module.'
                'Remember that all kinds of template code part need to be changed, '
                'like templateCode, TemplateCode, template_code and so on.'
                'Then create the file {file_path} according to the new code content.'
                '"""'
                '{file}'
                '"""',
    expected_output='The new code for the new module.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileCreateTool()]
)

my_crew = Crew(
    agents=[file_reader],
    tasks=[read_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)