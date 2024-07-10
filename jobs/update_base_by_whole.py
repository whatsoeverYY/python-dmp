from crewai import Task, Crew, Process
import main
from agents.file_reader_agent import file_reader
from agents.file_updater_agent import file_updater
from tools.file_create_tool import FileCreateTool
from tools.file_read_tool import FileReadTool
from func.read_file import read_file

# 更新1个基础配置文件(全文修改)

file_update_task = Task(
    description='A new module need to be added into the project: {module_info}. '
                'Following the TEMPLATE_CODE(模板代码) part in the file to update the file {file_path}.'
                'update the {file_path} correctly.'
                'Keep the unchanged part as it is.'
                '"""'
                '{file}'
                '"""',
    expected_output='The full new code after modified.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updater,
    tools=[FileCreateTool()]
)

my_crew = Crew(
    agents=[file_updater],
    tasks=[file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

file5 = 'src/router/data/index.ts'
files = [file5]


def update_base_files_by_whole():
    for i in range(0, len(files)):
        file_path = main.BASE_ROUTE + files[i]
        inputs = {
            "file_path": file_path,
            "file": read_file(file_path),
            "module_info": main.NEW_MODULE_NAME + '(' + main.NEW_MODULE_NAME_CN + ')'
        }
        result = my_crew.kickoff(inputs=inputs)
        print('my_crew.usage_metrics', my_crew.usage_metrics)
        print('***the result***')
        print(result)
        print('***the result***')


update_base_files_by_whole()
