from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
import main

llm = custom_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Please read the two files {csv_file} and {enum_template_file}."
         "Basing on the data in the '数据库 Field 名称', '检索' and '列表展示’ column of the {csv_file}, "
         "define three enums."
         "The format should be like the content in the {enum_template_file}."
         "The 'TEMPLATE_CODE' part should be replaced by {new_module_name},"
         "And the three enums should be filled by the fields name in the {csv_file}."
         "The LIST_COLUMNS enum and the DOC_ITEMS enum should be filled by the fields name in the '数据库 Field 名称'"
         " which is not 'NO' in the '列表展示' column"
         "The SEARCH_PARAMS enum should be filled by the fields name in the '数据库 Field 名称'"
         " which is not 'NO' in the '检索' column.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the dto basing on the provided two files.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)

read_task = Task(
    description="You are given two files {csv_file} and {enum_template_file}."
                'Please read them and figure out three enums definition'
                "basing on the data in the '数据库 Field 名称', '检索' and '列表展示’ column of the {csv_file}"
                "and the template code in the {enum_template_file}."
                'Write them into a new file {enum_file}.',
    expected_output='The new code.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileReadTool()]
)
file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Create the file {enum_file} according to the new code content.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to create a new file {enum_file} for the new module.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)
file_create_task = Task(
    description='Create the file {enum_file} according to the new code content.',
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
csv_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/export.csv'
enum_template_file = main.BASE_ROUTE + '_template_code/domains/templateCodeDomain/enum.ts'
enum_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/enum.ts'

inputs = {
    "csv_file": csv_file,
    "enum_template_file": enum_template_file,
    "new_module_name": new_module_name,
    "enum_file": enum_file,
}
result = my_crew.kickoff(inputs=inputs)

