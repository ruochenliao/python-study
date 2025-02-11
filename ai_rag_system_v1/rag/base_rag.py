from abc import abstractmethod
from llama_index.core import VectorStoreIndex, load_index_from_storage, SummaryIndex
from llama_index.core.indices.base import BaseIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.storage.storage_context import DEFAULT_PERSIST_DIR, StorageContext
from llama_index.vector_stores.milvus import MilvusVectorStore
from ai_rag_system_v1.utils import settings
# pip install llama-index-vector-stores-milvus
class RAG:
    def __init__(self, files: list[str]):
        self.files = files
    @abstractmethod
    async def load_data(self):
        """加载数据"""
    async def create_index_local(self, persist_dir=DEFAULT_PERSIST_DIR) -> BaseIndex:
        """
        创建本地索引，该函数是数据嵌入的重点优化模块
        入库优化：数据清洗优化--》分块优化
        参考LLmaindex的分块策略：https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/
        :param persist_dir: 本地持久化路径
        :return: BaseIndex
        """
        # 加载数据
        data = await self.load_data()
        # 创建一个句子分割器
        node_parser = SentenceSplitter.from_defaults()
        # 从文档中获取节点
        nodes = node_parser.get_nodes_from_documents(data, show_progress=True)
        # 创建向量存储索引
        index = VectorStoreIndex(nodes, show_progress=True)
        # index = VectorStoreIndex.from_documents(data, show_progress=True)
        # 对向量数据库做持久化
        index.storage_context.persist(persist_dir=persist_dir)
        # 返回创建的索引
        return index

    async def create_index(self, collection_name="default") -> BaseIndex:
        # 加载数据
        data = await self.load_data()
        # 创建一个句子分割器
        node_parser = SentenceSplitter.from_defaults()
        # 从文档中获取节点
        nodes = node_parser.get_nodes_from_documents(data)
        # 创建向量存储索引
        vector_store = MilvusVectorStore(
            uri=settings.configuration.milvus_uri,
            collection_name=collection_name, dim=settings.configuration.embedding_model_dim, overwrite=False
        )
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex(nodes, storage_context=storage_context, show_progress=True)

        return index

    @staticmethod
    async def load_index(collection_name="default") -> BaseIndex:
        vector_store = MilvusVectorStore(
            uri=settings.configuration.milvus_uri,
            collection_name=collection_name, dim=settings.configuration.embedding_model_dim, overwrite=False
        )
        return VectorStoreIndex.from_vector_store(vector_store=vector_store)

    @staticmethod
    async def load_index_local(persist_dir=DEFAULT_PERSIST_DIR) -> BaseIndex:
        return load_index_from_storage(
            StorageContext.from_defaults(persist_dir=persist_dir)
        )

