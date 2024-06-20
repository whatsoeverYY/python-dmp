from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
import main

llm = custom_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Please read the three files {csv_file}, {origin_type_file} and {basic_interfaces}."
         "Step1: Basing on the field names exist in the '数据库 Field 名称' column of the {csv_file}, "
         "update the {origin_type_file} by removing the redundancy."
         "Step2: Choose interface from the {basic_interfaces} to replace the customized interface "
         "in the {origin_type_file}, and add the import phase according to the note from the {basic_interfaces}."
         "Please Make sure all customized interface are replaced.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the dto basing on the provided two files.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)

read_task = Task(
    description="You are given three files {csv_file}, {origin_type_file} and {basic_interfaces}."
                'Please read them and then update the {origin_type_file} by removing the redundancy'
                'basing on the field names exist in the "数据库 Field 名称" column of the {csv_file} and'
                'replace the customized interface by interface from the {basic_interfaces} and add'
                'the appropriate import phase.'
                'Write them into a new file {type_file}.',
    expected_output='The updated code from {origin_type_file}.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileReadTool()]
)
file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Create the file {type_file} according to the new code content.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to create a new file {type_file} for the new module.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)
file_create_task = Task(
    description='Create the file {type_file} according to the new code content.',
    expected_output='Please provide the contents of the new file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_creator,
    tools=[FileCreateTool()]
)

my_crew = Crew(
    agents=[file_reader, file_creator],
    tasks=[read_task, file_create_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
new_module_name = 'TRANSLATIONAL_MEDICINE'
new_module_name_cn = '转化医学'
basic_interfaces = main.ROOT_PATH + '_modules/' + 'basic_interfaces.ts'
csv_file = main.ROOT_PATH + '_modules/' + new_module_name.lower() + '/export.csv'
origin_type_file = main.ROOT_PATH + '_modules/' + new_module_name.lower() + '/origin_type.ts'
type_file = main.ROOT_PATH + '_modules/' + new_module_name.lower() + '/type.ts'

result = my_crew.kickoff(inputs={"csv_file": csv_file, "origin_type_file": origin_type_file
    , "basic_interfaces": basic_interfaces, "type_file": type_file})

