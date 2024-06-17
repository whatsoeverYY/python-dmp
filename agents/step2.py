from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from crewai_tools import (FileReadTool)
from tools.output_update_tool import OutputUpdateTool

llm = custom_llm

file1 = '/Users/ever/workspace/data-management-platform-frontend/src/router/dict/index.ts'
file2 = '/Users/ever/workspace/data-management-platform-frontend/src/locales/cn.ts'
file3 = '/Users/ever/workspace/data-management-platform-frontend/src/views/dictionary/config/configs.tsx'
file4 = '/Users/ever/workspace/data-management-platform-frontend/src/views/dictionary/config/dictionary.tsx'

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript.",
    goal="Understand the content of the document and make accurate modifications based on the requirements.",
    backstory='Add relevant configurations to each file according to the newly added content.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)
read_task = Task(
    description="An enumeration member 'Parameter Type (CT_PARAM_TYPE)' "
                'has been added to the dictionary type DICTYPENAMES in the project. '
                'Please read the file {file}, analyze the objects in this file that need to be configured,'
                'and specify the new code that needs to be added.',
    expected_output='Please list the names of the objects in this file that need to be modified '
                    'and the new code that needs to be added. Do not include the existing code content in the result.',
    agent=file_reader
)

file_updater = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript.",
    goal="Modify the file {file} according to the identified objects and the new code content.",
    backstory="Modify the file {file} according to the identified objects and the new code content.",
    llm=llm,
    tools=[OutputUpdateTool()],
    allow_delegation=False
)
file_update_task = Task(
    description='Modify the file {file} according to the identified objects and the new code content.',
    expected_output='Please provide the contents of the modified file',
    agent=file_updater
)

my_crew = Crew(
    agents=[file_reader, file_updater],
    tasks=[read_task, file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
result = my_crew.kickoff(inputs={"file": file3})
print('my_crew.usage_metrics', my_crew.usage_metrics)
print('***the result***')
print(result)
print('***the result***')