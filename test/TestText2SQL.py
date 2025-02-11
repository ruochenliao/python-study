# 创建数据连接引擎
from llama_index.core import SQLDatabase, Settings
from llama_index.core.indices.struct_store import NLSQLTableQueryEngine
from llama_index.llms.openai import OpenAI
from sqlalchemy import create_engine
from config import embed_model_local_bge_small

llm = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f",  # 来自与deepseek 的 api_key
             model="deepseek-chat",
             api_base="http://127.0.0.1:1234/v1")
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

