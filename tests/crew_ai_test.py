from crewai import Crew, Agent, Task, Process
from llm.get_tongyi_llm import tongyi_llm as llm
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
from tools.file_create_tool import FileCreateTool

# Define agents with specific roles and tools
researcher = Agent(
    role='Senior Research Analyst',
    goal='Discover innovative AI technologies',
    backstory='',
    llm=llm,
    tools=[DuckDuckGoSearchRun()]
)

writer = Agent(
    role='Content Writer',
    goal='write a poet in the file /Users/ever/Documents/AI/projects/ai-projects/automatic-generate-code-for-dmp/poet',
    backstory='',
    llm=llm,
    tools=[FileCreateTool()],
    verbose=True
)

# Create tasks for the agents
research_task = Task(
    description='Identify breakthrough AI technologies',
    expected_output='breakthrough AI technologies',
    agent=researcher
)
write_article_task = Task(
    description='create a file according to the requirements',
    expected_output='a new file with the poet content',
    agent=writer
)

# Assemble the crew with a sequential process
my_crew = Crew(
    agents=[writer],
    tasks=[write_article_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
my_crew.kickoff()
print('my_crew.usage_metrics', my_crew.usage_metrics)