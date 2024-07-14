import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool
from func.camel_case_transform import to_pascal_case
from func.read_file import read_file

llm = custom_llm

file_updator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Update the file {type_file_path} basing on the files adn rules offered.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to figure out the code basing on the provided two files.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)

file_update_task = Task(
    description="Update the file {type_file_path} basing on the files and rules offered."
                "Rules:"
                "Replace the type of the fields in the dto interface in the type file"
                " according to the type of the same fields in the dto interface in the dto type file."
                "Add correct import code into the type file."
                "Keep the unchanged part of the type file as it is."
                'dto type file:'
                '{dto_type_file}'
                'type file:'
                '{type_file}',
    expected_output='The complete code from the updated file {type_file}.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updator,
    tools=[FileCreateTool()]
)


my_crew = Crew(
    agents=[file_updator],
    tasks=[file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN
root_path = main.BASE_ROUTE + '_modules/'

dto_type_file = root_path + new_module_name.lower() + '/type.ts'
type_file = main.BASE_ROUTE + 'src/types/' + to_pascal_case(new_module_name) + 'Type.ts'


def update_type_v2():
    inputs = {
        "dto_type_file": read_file(dto_type_file),
        "type_file": read_file(type_file),
        "type_file_path": type_file,
    }
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')


# update_type_v2()
