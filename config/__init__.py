from llama_index.core import Settings

from config.embeddings import embed_model_local_bge_small
from config.llm import deepseek_llm

Settings.embed_model = embed_model_local_bge_small()
Settings.llm = deepseek_llm()
