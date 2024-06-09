import main
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.llms import Tongyi

DASHSCOPE_API_KEY=main.DASHSCOPE_API_KEY
llm = Tongyi(temperature=1)
tools = load_tools([], llm=llm)
agent = create_csv_agent(
    llm=llm,
    path="/Users/ever/workspace/data-management-platform-frontend/modules/tm/export.csv"
)
response = agent.invoke('请列举出这个csv文件的所有列名')
print('response', response.get('output'))