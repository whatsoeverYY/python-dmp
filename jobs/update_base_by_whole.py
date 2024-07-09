from crewai import Task, Crew, Process
import main
from agents.file_reader_agent import file_reader
from agents.file_updater_agent import file_updater
from tools.file_create_tool import FileCreateTool
from tools.file_read_tool import FileReadTool

# 更新1个基础配置文件(全文修改)

read_task = Task(
    description='A new module need to be added into the project: {module_info}. Just read the file {file}, '
                'following the TEMPLATE_CODE(模板代码) part of the code including the comment part,'
                'update the {file} correctly.'
                'All other dependencies are settled, so no need to worry about it.',
    expected_output='The full new code after modified.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileReadTool()]
)
file_update_task = Task(
    description='Modify the file {file} according to the the new code content.',
    expected_output='The whole contents of the modified file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updater,
    tools=[FileCreateTool()]
)

my_crew = Crew(
    agents=[file_reader, file_updater],
    tasks=[read_task, file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

file4 = 'src/router/data/index.ts'
files = [file4]


def update_base_files_by_whole():
    for i in range(0, len(files)):
        inputs = {
            "file": main.BASE_ROUTE + files[i],
            "module_info": main.NEW_MODULE_NAME + '(' + main.NEW_MODULE_NAME_CN + ')'
        }
        result = my_crew.kickoff(inputs=inputs)
        print('my_crew.usage_metrics', my_crew.usage_metrics)
        print('***the result***')
        print(result)
        print('***the result***')


update_base_files_by_whole()
