from llama_index.llms.openai import OpenAI

"""
    deepseek
"""


def deepseek_llm(**kwargs):
    client = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f",  # 来自与deepseek 的 api_key
                    model="deepseek-chat",
                    api_base="https://api.deepseek.com/v1",
                    **kwargs)
    return client
