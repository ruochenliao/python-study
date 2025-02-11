import os
from pathlib import Path
from typing import Optional, List

import chainlit as cl
import pandas as pd
from chainlit.element import ElementBased
from chainlit.input_widget import Switch
from chainlit.types import ThreadDict
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.chat_engine.types import ChatMode
from llama_index.core.memory import ChatMemoryBuffer
from pandas import DataFrame
from pandasai import Agent

from ai_rag_system_v1.rag.multimodal_rag import MultiModalRAG
from ai_rag_system_v1.rag.traditional_rag import TraditionalRAG
from ai_rag_system_v1.utils import settings
import ai_rag_system_v1.utils.utils_ui as cl_utils

async def view_pdf(elements: List[ElementBased]):
    """查看PDF文件"""
    files = []
    contents = []
    for element in elements:
        if element.name.endswith(".pdf"):
            pdf = cl.Pdf(name=element.name, display="side", path=element.path)
            files.append(pdf)
            contents.append(element.name)
    if len(files) == 0:
        return
    await cl.Message(content=f"查看PDF文件：" + "，".join(contents), elements=files).send()

def llm_starters():
    starters = [
        cl.Starter(
            label="大模型提高软件测试效率",
            message="详细介绍如何借助大语言模型提高软件测试效率。",
            icon="/public/apidog.svg",
        ),
        cl.Starter(
            label="自动化测试思路",
            message="详细描述一下接口及UI自动化测试的基本思路。",
            icon="/public/pulumi.svg",
        ),
        cl.Starter(
            label="性能测试分析及瓶颈定位思路",
            message="详细描述一下软件性能测试分析及瓶颈定位的核心思路。",
            icon="/public/godot_engine.svg",
        ),
        cl.Starter(
            label="如何学习大模型应用的核心技术",
            message="给出学习大语言模型的一些重要的技术和方法。",
            icon="/public/gleam.svg",
        )
    ]

    return starters


def database_starters():
    starters = [
    cl.Starter(
                label="获取每种媒体类型的销售百分比",
                message="获取每种媒体类型的销售百分比,并以饼状图输出",
                icon="/public/apidog.svg",
            ),
            cl.Starter(
                label="获取每单位每类别的前10名的销售额",
                message="获取每单位每类别的前10名的销售额及销售占比，柱状图输出",
                icon="/public/pulumi.svg",
            ),
            cl.Starter(
                label="每位顾客在各流派上花费了多少钱",
                message="每位顾客在各流派上花费了多少钱",
                icon="/public/godot_engine.svg",
            ),
            cl.Starter(
                label="音乐商店每个流派有多少首歌",
                message="音乐商店每个流派有多少首歌",
                icon="/public/gleam.svg",
            )
]
    return starters

@cl.on_chat_start
async def start():
    await cl.ChatSettings(
        [
            Switch(id="multimodal", initial=False, label="多模态RAG", tooltip="多模态RAG", description="多模态RAG" ),
        ]
    ).send()
    # 初始化默认聊天引擎（直接与大模型对话）
    memory = ChatMemoryBuffer.from_defaults(token_limit=1024)
    chat_engine = SimpleChatEngine.from_defaults(memory=memory)
    cl.user_session.set("chat_engine", chat_engine)
    cl.user_session.set("history", [])

@cl.set_chat_profiles
async def chat_profile(current_user: cl.User):
    profiles = [
        cl.ChatProfile(
            name="大模型对话",
            markdown_description=f"与大模型对话",
            icon=f"/public/kbs/4.png",
        ),
        cl.ChatProfile(
            name="数据库对话",
            markdown_description=f"与数据库对话",
            icon=f"/public/kbs/db.jpg",
        )
    ]

    return profiles


@cl.set_starters
async def set_starters():
    # await cl_utils.train()
    return database_starters()


@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.User]:
    # 可以对接第三方认证
    if username in settings.user_data and password in settings.user_data:
        return cl.User(identifier=username,
                       metadata={"role": "user", "provider": "credentials"})
    else:
        return None
    # if (username, password) == ("danwen001", "danwen001"):
    #     return cl.User(identifier="danwen001",
    #                    metadata={"role": "admin", "provider": "credentials"})
    # else:
    #     return None


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    chat_engine = SimpleChatEngine.from_defaults()
    for message in thread.get("steps", []):
        if message["type"] == "user_message":
            chat_engine.chat_history.append(ChatMessage(content=message["output"], role="user"))
        elif message["type"] == "assistant_message":
            chat_engine.chat_history.append(ChatMessage(content=message["output"], role="assistant"))

    cl.user_session.set("chat_engine", chat_engine)

@cl.on_settings_update
async def setup_settings(settings):
    cl.user_session.set("settings", settings)


@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="", author="Assistant")
    chat_mode = cl.user_session.get("chat_profile", "大模型对话")
    history = cl.user_session.get("history", [])

    if chat_mode == "数据库对话":
        sql = await cl_utils.generate_sql(message.content, history=history)
        is_valid = await cl_utils.is_sql_valid(sql)
        if is_valid:
            df = await cl_utils.execute_query(sql)
            # 展示数据表格
            await cl.Message(content=df.to_markdown(index=False), author="Assistant").send()

            fig = await cl_utils.plot(human_query=message.content,sql=sql, df=df)
            elements = [cl.Plotly(name="chart", figure=fig, display="inline")]
            await cl.Message(content="生成的图表如下：", elements=elements, author="Assistant").send()

            history.extend([
                {
                    "content": sql,
                    "role": "assistant"
                },
                {
                    "content": message.content,
                    "role": "user"
                }]
            )
            return

    elif chat_mode == "大模型对话":
        await view_pdf(message.elements)
        files = []
        # 获取用户上传的文件（包含图片）
        for element in message.elements:
            if isinstance(element, cl.File) or isinstance(element, cl.Image):
                files.append(element.path)
        m = cl.user_session.get("settings", False)

        if not m and len(files) > 0:
            rag = TraditionalRAG(files=files)
            index = await rag.create_index_local()
            chat_engine = index.as_chat_engine(chat_mode=ChatMode.CONTEXT)
            cl.user_session.set("chat_engine", chat_engine)
        elif m and len(files) > 0:
            rag = MultiModalRAG(files=files)
            index = await rag.create_index_local()
            chat_engine = index.as_chat_engine(chat_mode=ChatMode.CONTEXT)
            cl.user_session.set("chat_engine", chat_engine)

    chat_engine = cl.user_session.get("chat_engine")
    res = await cl.make_async(chat_engine.stream_chat)(message.content)
    # 流式界面输出
    for token in res.response_gen:
        await msg.stream_token(token)
    await msg.send()

user_data = ["admin","nebula"]
pass