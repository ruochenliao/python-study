"""
# pip install llama-index-embeddings-huggingface
# pip install llama-index-embeddings-instructor
# pip install llama-index-embeddings-ollama
# pip install pymilvus[model]
"""
from typing import Dict

from llama_index.llms.openai import OpenAI as LLamaIndexOpenAI
from pymilvus import model
from .config import RAGConfig

from llama_index.llms.openai.utils import ALL_AVAILABLE_MODELS, CHAT_MODELS
from pandasai.llm import OpenAI as PandasAI
from openai import OpenAI
from pandasai.schemas.df_config import Config

configuration = RAGConfig()
DEEPSEEK_MODELS: Dict[str, int] = {
    "deepseek-chat": 128000,
}
ALL_AVAILABLE_MODELS.update(DEEPSEEK_MODELS)
CHAT_MODELS.update(DEEPSEEK_MODELS)


# -------------------------LLM Settings-------------------------
def pandasai_llm(**kwargs):
    return PandasAI(model=configuration.llm_model_name, api_token=configuration.llm_api_key,
                    api_base=configuration.llm_api_base, **kwargs)


def deepseek_llm(**kwargs):
    return LLamaIndexOpenAI(model=configuration.llm_model_name, api_key=configuration.llm_api_key,
                            api_base=configuration.llm_api_base, **kwargs)


def moonshot_llm(**kwargs):
    return OpenAI(api_key=configuration.moonshot_api_key, base_url="https://api.moonshot.cn/v1", **kwargs)


def vllm(**kwargs):
    return OpenAI(api_key=configuration.vllm_api_key, base_url=configuration.vllm_base_url, **kwargs)


def openai_llm(**kwargs):
    return OpenAI(api_key=configuration.llm_api_key, base_url=configuration.llm_api_base, **kwargs)


def pandasai_config():
    return Config(llm=pandasai_llm(), custom_whitelisted_dependencies=["timeit"], open_charts=False, save_charts=False,
                  verbose=True)


# ------------------------Embedding Settings------------------------

def pymilvus_bge_small_embedding_function(**kwargs):
    return model.dense.SentenceTransformerEmbeddingFunction(
        model_name='BAAI/bge-small-zh-v1.5',
        device='cpu',  # Specify the device to use, e.g., 'cpu' or 'cuda:0'
    )


# 本地模型
def local_bge_small_embed_model(**kwargs):
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5",
                                       **kwargs)
    return embed_model


# 在线模型
def ollama_nomic_embed_model(**kwargs):
    from llama_index.embeddings.ollama import OllamaEmbedding

    ollama_embedding = OllamaEmbedding(
        model_name="nomic-embed-text:latest",
        base_url="http://123.60.22.2:11434",
    )
    return ollama_embedding


def pymilvus_bge_m3_embedding_function(**kwargs):
    from pymilvus.model.hybrid import BGEM3EmbeddingFunction

    bge_m3_ef = BGEM3EmbeddingFunction(
        model_name='BAAI/bge-m3',  # Specify the model name
        device='cpu',  # Specify the device to use, e.g., 'cpu' or 'cuda:0'
        use_fp16=False  # Specify whether to use fp16. Set to `False` if `device` is `cpu`.
    )
    return bge_m3_ef


# --------------------------Test Login User Data--------------------------
#
#
# import pandas as pd
#
# # 读取CSV文件
# df = pd.read_csv('database/users.csv')
user_data = ["admin"]
