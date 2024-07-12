import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
from func.camel_case_transform import to_camel_case
from func.read_file import read_file

# 根据模板enum、csv文件创建完整enum文件

llm = custom_llm


file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Create the file {enum_file} according to files and rules listed below."
         "Basing on the data in the '数据库 Field 名称', '检索'，'列表展示' and '详情页展示' column in the csv file, "
         "define three enums."
         "The format should be like the content in the enum template file."
         "The 'TEMPLATE_CODE' part should be replaced by {new_module_name},"
         "And the three enums should be filled by the fields name in the csv file."
         "The LIST_COLUMNS enum should be filled by the fields name in the '数据库 Field 名称' column"
         " which is 'YES' in the '列表展示' column"
         "The DOC_ITEMS enum should be filled by the fields name in the '数据库 Field 名称' column"
         " which is 'YES' in the '详情页展示' column"
         "The SEARCH_PARAMS enum should be filled by the fields name in the '数据库 Field 名称' column"
         " which is 'YES' in the '检索' column."
         "csv file:"
         "{csv_file}"
         "enum template file:"
         "{enum_template_file}",
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
    agents=[file_creator],
    tasks=[file_create_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN
csv_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/export.csv'
enum_template_file = main.BASE_ROUTE + '_template_code/domains/templateCodeDomain/enum.ts'
enum_file = main.BASE_ROUTE + 'src/domains/' + to_camel_case(new_module_name) + 'Domain/enum.ts'


def create_enum():
    inputs = {
        "csv_file": read_file(csv_file),
        "enum_template_file": read_file(enum_template_file),
        "new_module_name": new_module_name,
        "enum_file": enum_file,
    }
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


create_enum()
