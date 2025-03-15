from langchain.agents import initialize_agent, AgentType
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.llm import LLMChain
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

DEEPSEEK_API_MODEL = "deepseek-v3"
DEEPSEEK_API_KEY = "sk-bMxEJNPNWjBzB4Pj5jrvKQDQy9blH1LXNnlmxLNllhfrj9Bo"
DEEPSEEK_API_BASE = "https://api.lkeap.cloud.tencent.com/v1"

# DEEPSEEK_API_MODEL = "deepseek-v3"
# DEEPSEEK_API_KEY = "sk-aeb8d69039b14320b0fe58cb8285d8b1"
# DEEPSEEK_API_BASE = "https://dashscope.aliyuncs.com/compatible-mode/v1"

llm = ChatOpenAI(
    model=DEEPSEEK_API_MODEL,
    openai_api_key=DEEPSEEK_API_KEY,
    openai_api_base=DEEPSEEK_API_BASE,
    max_tokens=1024
)

message = [
    SystemMessage(content="你是一个名sql专家"),
    HumanMessage(content="写一个简单的SQL")
]
# 第一次对话
response = llm.invoke(message)
print(response.content)


# 给与问题和答案作为输入例子
############################用few-shot，给定一些例子，让模型学会某些特定的回复
examples = [
    {
        "question": "查询35岁以上的员工?",
        "answer": "select * from employee where age > 35"
    },
    {
        "question": "查询女性员工",
        "answer": "select * from employee where gender = 'female'"
    },
    {
        "question": "查询所有员工",
        "answer": "select * from employee"
    },
]

example_prompt = PromptTemplate(template="Question:{question}\n{answer}",
                                input_variables=["question", "answer"])  # 设置一个提示模板
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:{input}",  # 相当于一个后缀
    input_variables=["input"]
)

response = llm.invoke(prompt.format(input="查询所有35以上的女性员工"))
response.pretty_print()

# agent
#llm-math 是一个用于计算的代理人工具
tool = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(
    tools=tool, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True
)
agent.invoke("5的3.5次方是多少? no need to add action")

# 基础应用——聊天模块
conversation = ConversationChain(llm=llm, verbose=True)
response = conversation.run("你好，你会写 SQL 吗？")
print(response)




