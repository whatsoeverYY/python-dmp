import main
from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm, tongyi_llm
from tools.file_read_tool import FileReadTool
from tools.file_create_tool import FileCreateTool

llm = tongyi_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Please read the file {file}, there are some arrays defined in it."
         "Some of the arrays are lack of some elements, you need to complete them"
         "according to the enums in the file {enum}.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to develop a new module basing on the provided template code.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)

read_task = Task(
    description="You need to read and understand the file {file}, there are some arrays defined in it."
                "Some of the arrays are lack of some elements, you need to complete them"
                "according to the enums in the file {enum}.",
    expected_output='The new code for the new module.'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_reader,
    tools=[FileReadTool()]
)
file_updator = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Modify the file {file} according to the new code content.",
    backstory='A front-end project based on Vue and TypeScript is under development.'
              'You need to create a new file {file} for the new module.',
    llm=llm,
    tools=[FileCreateTool()],
    allow_delegation=False
)
file_update_task = Task(
    description='Modify the file {file} according to the new code content.',
    expected_output='Please provide the contents of the updated file'
                    'And remember the Action Input part in your answer should always following the format:'
                    '"""'
                    'Action Input: {{"key": "value"}}'
                    '"""',
    agent=file_updator,
    tools=[FileCreateTool()]
)

my_crew = Crew(
    agents=[file_reader, file_updator],
    tasks=[read_task, file_update_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

need_update_files = [
    # '/views/templateCode/detail/TemplateCodeEditPage.tsx',
    # '/views/templateCode/BaseTemplateCodeListPage.tsx',
    # '/views/templateCode/TemplateCodeRecycleBin.tsx',
    '/views/templateCode/TemplateCodePreviewList.tsx',
]

new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN


def update_new_module_files(inputs):
    result = my_crew.kickoff(inputs=inputs)
    print('my_crew.usage_metrics', my_crew.usage_metrics)
    print('***the result***')
    print(result)
    print('***the result***')
    # for i in range(0, len(need_update_files)):
    #     inputs = {
    #         "file": main.BASE_ROUTE + need_update_files[i],
    #         "enum": main.BASE_ROUTE + 'domains/templateCodeDomain/enum.ts'
    #     }


# update_new_module_files(
#     {
#         "file": '/Users/ever/Documents/AI/projects/data-management-platform-frontend/src/views/translationalMedicine/TranslationalMedicinePreviewList.tsx',
#         "enum": '/Users/ever/Documents/AI/projects/data-management-platform-frontend/src/domains/translationalMedicineDomain/enum.ts'
#     }
# )
