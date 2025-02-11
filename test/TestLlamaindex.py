from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.chat_engine.types import ChatMode
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI

# 1、 使用llamaindex 自有的deepseek 框架，但是修改deepseek 远端地址
# from llama_index.llms.deepseek import DeepSeek
# llm = DeepSeek(model="deepseek-reasoner", api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f")

# 2、使用本地 deepseek 进行聊天，需要修改 /venv/lib/python3.11/site-packages/llama_index/llms/openai/utils.py，添加deep model
llm = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f",  # 来自与deepseek 的 api_key
             model="deepseek-chat",
             api_base="http://127.0.0.1:1234/v1")
Settings.llm = llm

chat_engine = SimpleChatEngine.from_defaults()
response = chat_engine.chat("你好")
print("deepseek 回复:")
print(response)


# 3、 创建本地持久化嵌入向量
from config import embed_model_local_bge_small
Settings.embed_model = embed_model_local_bge_small()

# 加载数据（数据连接器）
data = SimpleDirectoryReader(input_dir="data").load_data()
# 构建索引，正常执行一次即可
index = VectorStoreIndex.from_documents(data, show_progress=True)

# 查询引擎
q = index.as_query_engine()
result = q.query("介绍一下怎么调用DOS接口")
print(result)

result = q.query("怎么生成DOS header 签名")
print(result)

# 检索引擎 index.as_retriever()

# 本地持久化index
index.storage_context.persist(persist_dir="index")


"""
    加载陷入模型
"""
# 加载索引
storage_context = StorageContext.from_defaults(persist_dir="./index")
index = load_index_from_storage(storage_context)
# 存储聊天历史
memory = ChatMemoryBuffer.from_defaults(token_limit=1024)

# 聊天引擎 index.as_chat_engine
chat_engine = index.as_chat_engine(
    chat_mode=ChatMode.CONTEXT,
    memory=memory,
    system_prompt=(
        "通过应用token和应用app，可以计算得出 hrgw-signature"
    ),
)

chat_engine.chat("怎么生成DOS header 签名")
