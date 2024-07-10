import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
from func.camel_case_transform import to_pascal_case
from func.read_file import read_file

llm = custom_llm

# 创建包含三个interface的XXXType.ts文件

file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Create the new file {type_file} according to the files and rules listed below."
         "Basing on the data in the '数据库 Field 名称' and '检索' column of the csv file, "
         "define three interfaces."
         "The format should be like the content in the type template file."
         "The 'TEMPLATE_CODE' part should be replaced by {new_module_name},"
         "And the three interfaces should be filled by the fields name in the csv file."
         "The dto interface should be filled by the fields name in the '数据库 Field 名称' column."
         "The other two interfaces SearchFormParams and SearchParams "
         "should be filled by the fields name in the '数据库 Field 名称' column"
         " which is 'YES' in the '检索' column."
         "And the fields in SearchFormParams should all be added the prefix 'fe_'."
         "The type of all fields in those three interfaces should be string."
         "Each field should add comment to clarify the name which can be known from "
         "the '字段名称' column from the csv file"
         "csv file:"
         "{csv_file}"
         "type template file:"
         "{type_template_file}",
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
    agents=[file_creator],
    tasks=[file_create_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN

csv_file = main.BASE_ROUTE + '_modules/' + new_module_name.lower() + '/export.csv'
type_template_file = main.BASE_ROUTE + '_template_code/types/TemplateCodeType.ts'

type_file = main.BASE_ROUTE + 'src/types/' + to_pascal_case(new_module_name) + 'Type.ts'


def create_new_type():
    inputs = {
        "csv_file": read_file(csv_file),
        "type_template_file": read_file(type_template_file),
        "new_module_name": new_module_name,
        "type_file": type_file,
    }
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


create_new_type()
