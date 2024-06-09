from crewai import Crew, Agent, Task, Process
from llm.get_tongyi_llm import tongyi_llm as llm
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

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
    goal='Write engaging articles on AI discoveries',
    backstory='',
    llm=llm,
    verbose=True
)

# Create tasks for the agents
research_task = Task(
    description='Identify breakthrough AI technologies',
    expected_output='breakthrough AI technologies',
    agent=researcher
)
write_article_task = Task(
    description='Draft an article on the latest AI technologies',
    expected_output='an article on the latest AI technologies',
    agent=writer
)

# Assemble the crew with a sequential process
my_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_article_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
my_crew.kickoff()
print('my_crew.usage_metrics', my_crew.usage_metrics)