import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm, tongyi_llm_plus
from tools.file_read_tool import FileReadTool
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
file_update_task_type = Task(
    description='Modify the file {file_path} according to files and rules below.'
                'Rules:'
                'The object in the file are lack of some elements, you need to complete them'
                'according to the interfaces fields in the file type.'
                'The format of the new elements should follow the rule in the comments.'
                'If there are prefix before the fields in the comments, '
                'you need to add the prefix to the new elements as well.'
                "Keep the unchanged part of the file as it is."
                'file:'
                '{file}'
                'type:'
                '{type}',
    expected_output='Please provide the contents of the updated file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updator,
    tools=[FileCreateTool()]
)

file_update_task_enum = Task(
    description='Modify the file {file_path} according to files and rules below.'
                'Rules:'
                'The class in the file are lack of some elements, you need to complete them '
                'according to the enums in the file enum.'
                'The format of the new elements should always follow the rule in the comments.'
                'Make sure the fields value in the new elements has the same prefix as in the comments.'
                "Keep the unchanged part of the file as it is.\n"
                'file:\n'
                '{file}'
                'enum:\n'
                '{enum}',
    expected_output='Please provide the contents of the updated file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updator,
    tools=[FileCreateTool()]
)

my_crew_type = Crew(
    agents=[file_updator],
    tasks=[file_update_task_type],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

my_crew_enum = Crew(
    agents=[file_updator],
    tasks=[file_update_task_enum],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

# LLM更新配置
need_update_by_type = [
    '/domains/templateCodeDomain/entity.ts',
    '/domains/templateCodeDomain/transform.ts',
]
need_update_by_enum = [
    '/views/templateCode/locales/cn.ts',
    '/views/templateCode/composition/useTemplateCodeSearchFormItems.tsx',
    '/views/templateCode/composition/useTemplateCodeDocEdit.tsx',
    '/views/templateCode/composition/useTemplateCodeListColumns.tsx',
]

new_module_path = main.BASE_ROUTE + 'src'
new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN


def update_new_module_files_by_type_v2(arr=need_update_by_type):
    for i in range(0, len(arr)):
        file_path = replace_path_name(new_module_path + arr[i], new_module_name)
        inputs = {
            "file": read_file(file_path),
            "type": read_file(replace_path_name(new_module_path + main.TYPE_FILE, new_module_name)),
            "file_path": file_path
        }
        result = my_crew_type.kickoff(inputs=inputs)
        print('my_crew.usage_metrics', my_crew_type.usage_metrics)
        print('***the result***')
        print(result)
        print('***the result***')


def update_new_module_files_by_enum_v2(arr=need_update_by_enum):
    for i in range(0, len(arr)):
        file_path = replace_path_name(new_module_path + arr[i], new_module_name)
        inputs = {
            "file": read_file(file_path),
            "enum": read_file(replace_path_name(new_module_path + main.ENUM_FILE, new_module_name)),
            "file_path": file_path
        }
        result = my_crew_enum.kickoff(inputs=inputs)
        print('my_crew.usage_metrics', my_crew_enum.usage_metrics)
        print('***the result***')
        print(result)
        print('***the result***')

# update_new_module_files_by_type_v2()
# update_new_module_files_by_enum_v2()
