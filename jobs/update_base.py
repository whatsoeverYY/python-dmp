from crewai import Task, Crew, Process
import main
from agents.file_reader_agent import file_reader
from agents.file_updater_agent import file_updater
from tools.file_read_tool import FileReadTool
from tools.output_update_tool import OutputUpdateTool
from func.read_file import read_file

# 更新4个基础配置文件(通过修改的对象以及新增的代码进行修改)

file_update_task = Task(
    description='A new module need to be added into the project: {module_info}.'
                'Following the TEMPLATE_CODE(模板代码) part in the file to update the file {file_path}'
                'analyze the objects in this file that need to be configured,'
                'and specify the new code that needs to be added.'
                'Pay attention to the field format in the new code,'
                'which should always follow the format of the code exists whether it is in uppercase format'
                'or camelcase format or other format.'
                'The code file reads as follows'
                '"""'
                '{file}'
                '"""',
    expected_output='Please list the names of the objects in this file that need to be modified '
                    'and the new code that needs to be added. '
                    'Do not include the existing code content in the result!'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updater,
    tools=[OutputUpdateTool()]
)


my_crew = Crew(
    agents=[file_updater],
    tasks=[file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

file1 = 'src/types/DataType.ts'
file2 = 'src/utils/dataType.ts'
file3 = 'src/type/router.ts'  # 有修改遗漏
file4 = 'src/locales/cn.ts'
files = [file1, file2, file3, file4]
# files = [file3, file4]


def update_base_files():
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


update_base_files()
