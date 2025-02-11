import re

from llama_index.core import SQLDatabase, StorageContext
from llama_index.core.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.core.objects import SQLTableSchema, SQLTableNodeMapping, ObjectIndex
from llama_index.vector_stores.milvus import MilvusVectorStore
from sqlalchemy import create_engine

from config.config import RagConfig
from .base_rag import RAG


class DatabaseRAG(RAG):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        engine = create_engine(RagConfig.pg_connection_string)
        self.sql_database = SQLDatabase(engine)

    async def load_data(self):
        tables = self.sql_database.get_usable_table_names()
        table_schema_objs = []
        for table in tables:
            single_table_info = self.sql_database.get_single_table_info(table)
            match = re.search(r"with comment: \((.*?)\)", single_table_info)
            table_description = match.group(1) if match else f"{table} table"

            table_schema_objs.append(
                SQLTableSchema(table_name=table, context=table_description)
            )

        return table_schema_objs

    async def create_index(self, collection_name="chainlit"):
        # 加载数据
        data = await self.load_data()

        table_node_mapping = SQLTableNodeMapping(sql_database=self.sql_database)

        # 创建向量索引存储
        vector_store = MilvusVectorStore(
            uri=RagConfig.milvus,
            collection_name=collection_name, dim=RagConfig.embedding_model_dim, overwrite=True
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # 会把data和table_node_mapping映射后的嵌入到向量里去
        index = ObjectIndex.from_objects(
            objects=data,
            object_mapping=table_node_mapping,
            storage_context=storage_context
        )

        return index

    async def create_query_engine(self):
        index = await self.load_index(collection_name="database")
        query_engine = SQLTableRetrieverQueryEngine(
            sql_database=self.sql_database,
            table_retriever=index.as_retriever(similarity_top_k=1)
        )

        return query_engine
