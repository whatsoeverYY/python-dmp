from crewai import Agent, Task, Crew, Process
from llm.get_tongyi_llm import custom_llm
from tools.output_update_tool import OutputUpdateTool

llm = custom_llm

file_updater = Agent(
    role="An front-end development expert, proficient in Vue and TypeScript",
    goal="Modify the file according to the identified objects and the new code content.",
    backstory="A variable in a file of the project has been updated, "
              "and the corresponding configuration needs to be added to the given file.",
    llm=llm,
    tools=[OutputUpdateTool()],
    allow_delegation=False
)