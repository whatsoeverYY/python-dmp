from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from tools.file_read_tool import FileReadTool

llm = custom_llm

file_reader = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Understand the content of the provided document and "
         "correctly analyze the objects in the file provided that need to be modified "
         "and the code that needs to be added based on the requirements.",
    backstory='A front-end project based on Vue and TypeScript is under development.',
    llm=llm,
    tools=[FileReadTool()],
    allow_delegation=False
)