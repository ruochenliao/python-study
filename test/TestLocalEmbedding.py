from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from config import embed_model_local_bge_small

# 0、设置向量嵌入模型
Settings.embed_model = embed_model_local_bge_small()

# 1、简单地创建向量
data = SimpleDirectoryReader(input_dir="data").load_data()
# 构建索引，正常执行一次即可
index = VectorStoreIndex.from_documents(data, show_progress=True)

# 2、对文档进行切割
node_spliter = SentenceSplitter.from_defaults()
nodes = node_spliter.get_nodes_from_documents(data)
index = VectorStoreIndex(nodes)

# 3、持久化到本地
index.storage_context.persist()

# 4、从本地加载向量
local_index = load_index_from_storage(storage_context=StorageContext.from_defaults(persist_dir="./index"))
llm = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f",  # 来自与deepseek 的 api_key
             model="deepseek-chat",
             api_base="http://127.0.0.1:1234/v1")

# 5、让模型通过向量检索
engine = local_index.as_query_engine(llm=llm)
result = engine.query("怎么生成 hrgw-signature")

print(result)
