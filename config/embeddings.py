# pip install llama-index-embeddings-huggingface
# pip install llama-index-embeddings-instructor

# pip install llama-index-embeddings-ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

"""
    本地模型
    BAAI/bge-small-zh-v1.5 是一个中文预训练语言模型，
    适用于多种自然语言处理任务。通过 Hugging Face 的 Transformers 库，你可以方便地加载和使用这个模型来处理各种 NLP 任务。
    embed_model 是一个使用 Hugging Face 预训练模型 BAAI/bge-small-zh-v1.5 来生成文本嵌入（embeddings）的对象。
    主要用途
    生成文本嵌入的主要用途包括但不限于以下几个方面：
    
    文本相似度计算：
    
    通过将文本转换为嵌入向量，可以计算不同文本之间的相似度。这在信息检索、推荐系统和文本聚类等任务中非常有用。
    文本分类：
    
    嵌入向量可以作为特征输入到分类器中，用于情感分析、主题分类等任务。
    信息检索：
    
    在搜索引擎中，可以将查询和文档都转换为嵌入向量，然后通过向量相似度来检索相关文档。
    问答系统：
    
    嵌入向量可以用于匹配问题和答案，帮助构建更智能的问答系统。
    文本生成：
    
    嵌入向量可以作为生成模型的输入，用于生成与输入文本相关的内容。
"""
def embed_model_local_bge_small(**kwargs):
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5",
                                       cache_folder=r"../embed_cache",
                                       **kwargs)
    return embed_model
# 在线模型
# def embed_model_ollama_nomic(**kwargs):
#     from llama_index.embeddings.ollama import OllamaEmbedding
#
#     ollama_embedding = OllamaEmbedding(
#         model_name="nomic-embed-text:latest",
#         base_url="http://123.60.22.2:11434",
#     )
#     return ollama_embedding
