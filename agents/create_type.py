import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_create_tool import FileCreateTool
from func.read_file import read_file

llm = custom_llm

# 创建只包含dto的type.ts文件

file_creator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="create a new file {type_file} basing on the files adn rules offered.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the code basing on the provided three files and rules.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)

file_create_task = Task(
    description="Create a new file {type_file} basing on the files adn rules offered as below."
                "Rules:"
                "Step1: Basing on the field names exist in the '数据库 Field 名称' column of the csv file, "
                "update the origin type file by removing the redundancy."
                "Step2: Choose interface from the basic interfaces file to replace the customized interface "
                "in the origin type file, "
                "and add the import phase according to the note from the basic interfaces file."
                "Please Make sure all customized interface are replaced, "
                "and the type of the fields in the origin type file "
                "are from the basic interfaces file."
                "Use the new content in the origin type file to create the new file {type_file}."
                "csv file:"
                "{csv_file}"
                "origin type file:"
                "{origin_type_file}"
                "basic interfaces file:"
                "{basic_interfaces}",
    expected_output='The complete new code.'
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
modules_route = main.BASE_ROUTE + '_modules/' + new_module_name.lower()

basic_interfaces = main.BASE_ROUTE + '_modules/' + 'basic_interfaces.ts'
csv_file = modules_route + '/export.csv'
origin_type_file = modules_route + '/origin_type.ts'
type_file = modules_route + '/type.ts'


def create_type():
    inputs = {
        "csv_file": read_file(csv_file),
        "origin_type_file": read_file(origin_type_file),
        "basic_interfaces": read_file(basic_interfaces),
        "type_file": type_file
    }
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


create_type()
