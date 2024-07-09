from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
from func.camel_case_transform import to_pascal_case
import main

llm = custom_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Please read the two files {dto_type_file}, and {type_file}."
         "Update the dto interface in the {type_file} according to the dto interface in the {dto_type_file}."
         "Make sure all fields in the dto interface in the {type_file} have the same type as the fields"
         " in the dto interface in the {dto_type_file}."
         "And add the import into the {type_file} according to the import code in the {dto_type_file}",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the dto basing on the provided two files.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)

read_task = Task(
    description="You are given two files {dto_type_file} and {type_file}."
                'Please read them and then update the {type_file} '
                'by replacing the type of the fields in the dto interface'
                ' according to the type of the same fields in the dto interface in the {dto_type_file}.'
                'and add correct import code into the {type_file}.',
    expected_output='The complete code from the updated file {type_file}.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileReadTool()]
)


file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Modify the file {type_file} according to the new code content.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to create a new file {type_file} for the new module.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)
file_create_task = Task(
    description='Modify the file {type_file} according to the new code content.',
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
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN
root_path = main.BASE_ROUTE + '_modules/'

dto_type_file = root_path + new_module_name.lower() + '/type.ts'
type_file = main.BASE_ROUTE + 'src/types/' + to_pascal_case(new_module_name) + 'Type.ts'

inputs = {
    "dto_type_file": dto_type_file,
    "type_file": type_file,
}


def update_type_v2():
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


update_type_v2()
