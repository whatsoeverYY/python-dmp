from llm.get_tongyi_llm import tongyi_llm as llm
from langchain_openai import ChatOpenAI
from langchain_community.llms import Tongyi
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

template = '''
        你的名字是小黑子,当人问问题的时候,你都会在开头加上'唱,跳,rap,篮球!',然后再回答{question}
    '''
prompt = PromptTemplate(
    template=template,
    input_variables=["question"]  # 这个question就是用户输入的内容,这行代码不可缺少
)
# 将llm与prompt联系起来
chain = prompt | llm

# model = ChatOpenAI(llm=llm, prompt=prompt)
question = '你是谁'
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi! Nice to mee you"),
]

res = chain.invoke(messages)

print(res)