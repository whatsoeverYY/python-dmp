from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
from func.camel_case_transform import to_pascal_case
import main

llm = custom_llm

# 创建包含三个接口的XXXType.ts文件

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Please read the two files {csv_file} and {type_template_file}."
         "Basing on the data in the '数据库 Field 名称' and '检索' column of the {csv_file}, "
         "define three interfaces."
         "The format should be like the content in the {type_template_file}."
         "The 'TEMPLATE_CODE' part should be replaced by {new_module_name},"
         "And the three interfaces should be filled by the fields name in the {csv_file}."
         "The dto interface should be filled by the fields name in the '数据库 Field 名称'"
         "The other two interfaces SearchFormParams and SearchParams "
         "should be filled by the fields name in the '数据库 Field 名称'"
         " which is 'YES' in the '检索' column."
         "And the fields in SearchFormParams should all be added the prefix 'fe_'."
         "The type of all fields in those three interfaces should be string."
         "Each field should add comment to clarify the name which can be known from "
         "the '字段名称' column from the {csv_file}",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the dto basing on the provided two files.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)
read_task = Task(
    description="You are given two files {csv_file} and {type_template_file}."
                'Please read them and figure out three enums definition'
                "basing on the data in the '数据库 Field 名称' and '检索' and of the {csv_file}"
                "and the template code in the {type_template_file}."
                'Write correct code into a new file {type_file}.',
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
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN
basic_interfaces = main.BASE_ROUTE + '_modules/' + 'basic_interfaces.ts'
csv_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/export.csv'
type_template_file = main.BASE_ROUTE + '_template_code/types/TemplateCodeType.ts'
origin_type_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/origin_type.ts'

type_file = main.BASE_ROUTE + 'src/types/' + to_pascal_case(new_module_name) + 'Type.ts'

inputs = {
    "csv_file": csv_file,
    "origin_type_file": origin_type_file,
    "type_template_file": type_template_file,
    "basic_interfaces": basic_interfaces,
    "new_module_name": new_module_name,
    "type_file": type_file,
}


def create_new_type():
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


create_new_type()
