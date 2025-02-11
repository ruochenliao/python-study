from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.milvus import MilvusVectorStore

from config import embed_model_local_bge_small

# 1、设置嵌入模型
Settings.embed_model = embed_model_local_bge_small()

data = SimpleDirectoryReader(input_dir="data").load_data()

# 2、生成拆分器
node_parser = SentenceSplitter.from_defaults()
nodes = node_parser.get_nodes_from_documents(data)
# 3、创建向量索引存储
vector_store = MilvusVectorStore(
    uri="http://9.135.72.202:19530",
    collection_name="dos_index",
    dim=512,
    overwrite=False
)

# 5、将nodes索引存储到 storage_context.vector_store 中去
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)

# 6、从 milvus 加载向量
remote_index = VectorStoreIndex.from_vector_store(vector_store)

#7、引擎通过向量聊天
llm = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f",  # 来自与deepseek 的 api_key
             model="deepseek-chat",
             api_base="http://127.0.0.1:1234/v1")
engine = remote_index.as_query_engine(llm=llm)
result = engine.query("怎么生成 hrgw-signature")
print(result)
