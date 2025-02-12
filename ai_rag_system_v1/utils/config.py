import os

from pydantic import BaseModel, Field


class RAGConfig(BaseModel):
    milvus_uri: str = Field(default=os.getenv("MILVUS_URI"), description="Milvus URI")
    embedding_model_dim: int = Field(default=512, description="Embedding model dimension")
    moonshot_api_key: str = Field(default=os.getenv("MOONSHOT_API_KEY"), description="Moonshot API key")
    llm_api_key: str = Field(default=os.getenv("LLM_API_KEY"), description="LLM API key")
    llm_api_base: str = Field(default=os.getenv("LLM_API_BASE"), description="LLM API base")
    llm_model_name: str = Field(default=os.getenv("LLM_MODEL_NAME"), description="LLM model name")
    pg_connection_string: str = Field(default=os.getenv("PG_CONNECTION_STRING"), description="Postgres connection string")
    ocr_download_dir: str = Field(default=os.getenv("OCR_DOWNLOAD_PATH"), description="OCR download directory")
    ocr_base_url: str = Field(default=os.getenv("OCR_BASE_URL"), description="OCR base URL")
    vllm_api_key: str = Field(default=os.getenv("VLLM_API_KEY"), description="VLLM API key")
    vllm_base_url: str = Field(default=os.getenv("VLLM_BASE_URL"), description="VLLM base URL")
    vllm_model_name: str = Field(default=os.getenv("VLLM_MODEL_NAME"), description="VLLM model name")
    minio_endpoint: str = Field(default=os.getenv("MINIO_ENDPOINT"), description="Minio endpoint")
    minio_access_key: str = Field(default=os.getenv("MINIO_ACCESS_KEY"), description="Minio access key")
    minio_secret_key: str = Field(default=os.getenv("MINIO_SECRET_KEY"), description="Minio secret key")
    minio_bucket_name: str = Field(default=os.getenv("MINIO_BUCKET_NAME"), description="Minio bucket name")

    db_connection_string: str = Field(default=os.getenv("DB_CONNECTION_STRING"),
                                      description="Database connection string")

    milvus_collection_doc_name: str = Field(default=os.getenv("MILVUS_COLLECTION_DOC_NAME","danwen_doc"),
                                           description="Milvus collection name")
    milvus_collection_ddl_name: str = Field(default=os.getenv("MILVUS_COLLECTION_DDL_NAME", "danwen_ddl"),description="Milvus collection name")
    milvus_collection_sql_name: str = Field(default=os.getenv("MILVUS_COLLECTION_SQL_NAME", "danwen_sql"),description="Milvus collection name")



    mysql_host: str = Field(default=os.getenv("MYSQL_HOST"), description="MySQL host")
    mysql_user: str = Field(default=os.getenv("MYSQL_USER"), description="MySQL user")
    mysql_password: str = Field(default=os.getenv("MYSQL_PASSWORD"), description="MySQL password")
    mysql_db: str = Field(default=os.getenv("MYSQL_DB"), description="MySQL database")
    mysql_port: int = Field(default=os.getenv("MYSQL_PORT"), description="MySQL port")

    pg_host: str = Field(default=os.getenv("PG_HOST"), description="PG_HOST")
    pg_user: str = Field(default=os.getenv("PG_USER"), description="PG_USER")
    pg_password: str = Field(default=os.getenv("PG_PASSWORD"), description="PG_PASSWORD")
    pg_db: str = Field(default=os.getenv("PG_DB"), description="PG_DB")
    pg_port: int = Field(default=os.getenv("PG_PORT"), description="PG_PORT")
