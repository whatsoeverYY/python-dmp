from crewai import Task, Crew, Process
from main import BASE_ROUTE
from file_reader_agent import file_reader
from file_updater_agent import file_updater
from tools.file_read_tool import FileReadTool
from tools.output_update_tool import OutputUpdateTool

file1 = 'router/dict/index.ts'
file2 = 'locales/cn.ts'
file3 = 'views/dictionary/config/configs.tsx'
file4 = 'views/dictionary/config/dictionary.tsx'

read_task = Task(
    description="An enumeration member 'Parameter Type (CT_PARAM_TYPE)' "
                'has been added to the dictionary type DICTYPENAMES in the project. '
                'Please read the file {file}, analyze the objects in this file that need to be configured,'
                'and specify the new code that needs to be added.',
    expected_output='Please list the names of the objects in this file that need to be modified '
                    'and the new code that needs to be added. '
                    'Do not include the existing code content in the result.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
                    # 'Please noted that the Action Input content in your analysis'
                    # ' should be a simple a python dictionary enclosed in curly braces '
                    # 'without any specific language type description',
    agent=file_reader,
    tools=[FileReadTool()]
)
file_update_task = Task(
    description='Modify the file {file} according to the identified objects and the new code content.',
    expected_output='Please provide the contents of the modified file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updater,
    tools=[OutputUpdateTool()]
)

my_crew = Crew(
    agents=[file_reader, file_updater],
    tasks=[read_task, file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
result = my_crew.kickoff(inputs={"file": BASE_ROUTE + file4})
print('my_crew.usage_metrics', my_crew.usage_metrics)
print('***the result***')
print(result)
print('***the result***')