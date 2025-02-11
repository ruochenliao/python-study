from abc import ABC

from pymilvus import MilvusClient
from vanna.milvus import Milvus_VectorStore
from vanna.openai import OpenAI_Chat
from ai_rag_system_v1.utils import settings
from ai_rag_system_v1.rag.base_rag import RAG

class DQuestionMilvus(Milvus_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        if config is None:
            milvus_client = MilvusClient(uri=settings.configuration.milvus_uri)
            config = {'model': settings.configuration.llm_model_name,
                      "milvus_client": milvus_client,
                      "embedding_function": settings.pymilvus_bge_small_embedding_function(),
                      "language": "Chinese",
                      "sql_collection_name": settings.configuration.milvus_collection_sql_name,
                      "ddl_collection_name": settings.configuration.milvus_collection_ddl_name,
                      "doc_collection_name": settings.configuration.milvus_collection_doc_name
                      }
        Milvus_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self,client=settings.openai_llm(), config=config)


class SQLiteDatabaseRAG(DQuestionMilvus):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        self.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
    async def load_data(self):
        pass
    async def create_index(self, collection_name="default"):
        """
        数据库表的结构化信息训练到向量数据库
        :param collection_name:
        :return:
        """
        existing_training_data = self.get_training_data()
        if len(existing_training_data) > 0:
            for _, training_data in existing_training_data.iterrows():
                self.remove_training_data(training_data['id'])
        df_ddl = self.run_sql("SELECT type,sql FROM sqlite_master WHERE sql is not null")
        # 数据训练进向量数据库
        for ddl in df_ddl['sql'].to_list():
            self.train(ddl=ddl)

class MySQLDatabaseRAG(DQuestionMilvus):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        self.connect_to_mysql(host=settings.configuration.mysql_host,
                              dbname=settings.configuration.mysql_db,
                              user=settings.configuration.mysql_user,
                              password=settings.configuration.mysql_password,
                              port=int(settings.configuration.mysql_port))
    async def load_data(self):
        pass
    async def create_index(self, collection_name="default"):
        df_ddl = self.run_sql(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS where table_schema = '{settings.configuration.mysql_db}'")
        plan = self.get_training_plan_mysql(df_ddl)
        self.train(plan=plan)

if __name__ == "__main__":
    d = SQLiteDatabaseRAG()
    d.create_index()
    # d = MySQLDatabaseRAG()
    # df_ddl = d.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS where table_schema = 'student_db'")
    # plan = d.get_training_plan_mysql(df_ddl)
    # d.train(plan=plan)
    # d.milvus_client.drop_collection(collection_name="vannasql")
    # d.milvus_client.drop_collection(collection_name="vannaddl")
    # d.milvus_client.drop_collection(collection_name="vannadoc")