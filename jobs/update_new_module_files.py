import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm, tongyi_llm_plus
from tools.file_create_tool import FileCreateTool
from func.common import replace_path_name
from func.read_file import read_file

llm = custom_llm


file_updator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Modify the file {file_path} according to files and rules below.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to update the file {file_path} basing on the files and rules provided.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)
file_update_task = Task(
    description='Modify the file {file_path} according to files and rules below.'
                'Rules:'
                'Some of the arrays in the file are lack of some elements, you need to complete them'
                'according to the enums in the file enum.'
                "Keep the unchanged part of the file as it is."
                'file:'
                '{file}'
                'enum:'
                '{enum}',
    expected_output='Please provide the contents of the updated file'
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


need_update_files = [
    '/views/templateCode/TemplateCodePreviewList.tsx',
    '/views/templateCode/TemplateCodeEditList.tsx',
    '/views/templateCode/TemplateCodeRecycleBin.tsx',
    '/views/templateCode/detail/TemplateCodeEditPage.tsx',
]

new_module_path = main.BASE_ROUTE + 'src'
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN


def update_new_module_files():
    for i in range(0, len(need_update_files)):
        file_path = replace_path_name(new_module_path + need_update_files[i], new_module_name)
        inputs = {
            "file": read_file(file_path),
            "enum": read_file(replace_path_name(new_module_path + main.ENUM_FILE, new_module_name)),
            "file_path": file_path
        }
        result = my_crew.kickoff(inputs=inputs)
        print('my_crew.usage_metrics', my_crew.usage_metrics)
        print('***the result***')
        print(result)
        print('***the result***')


# update_new_module_files()
