# 创建数据连接引擎
from typing import Dict

from llama_index.core import SQLDatabase, Settings
from llama_index.core.indices.struct_store import NLSQLTableQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai.utils import CHAT_MODELS, ALL_AVAILABLE_MODELS
from sqlalchemy import create_engine

from config import embed_model_local_bge_small
# 定义Deepseek模型字典，存储模型名和对应的token限制
DEEPSEEK_MODELS: Dict[str, int] = {
    "deepseek-v3": 128000
}

# 更新所有可用模型和聊天模型字典，整合Deepseek模型
ALL_AVAILABLE_MODELS.update(DEEPSEEK_MODELS)
CHAT_MODELS.update(DEEPSEEK_MODELS)

llm = OpenAI(api_key="sk-aeb8d69039b14320b0fe58cb8285d8b1",  # 来自与deepseek 的 api_key
             model="deepseek-v3",
             api_base="https://dashscope.aliyuncs.com/compatible-mode/v1")
Settings.llm = llm

Settings.embed_model = embed_model_local_bge_small()
engine = create_engine("postgresql://myuser:mypassword@9.135.72.202:5432/chainlit")

# 创建数据库操作对象
sql_database = SQLDatabase(engine)

sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    llm=llm,
    verbose=True
)

response = sql_query_engine.query("获取所有学生信息")
print(response)

response = sql_query_engine.query("让我们邀请在我们的数据集中创作了最多摇滚音乐的艺术家。编写一个查询，返回前 10 名摇滚乐队艺术家的名字和总曲目数。")
print(response)

