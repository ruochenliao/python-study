from llama_index.core import Settings

from ai_rag_system_v1.utils import settings

Settings.embed_model = settings.local_bge_small_embed_model()
Settings.llm = settings.deepseek_llm()