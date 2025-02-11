# import os.path

from fastapi import FastAPI, UploadFile, Form
from chainlit.utils import mount_chainlit
from fastapi.responses import HTMLResponse

from rag.database_rag import DatabaseRAG
# from rag_system_text2SQL.utils.r import R
# from rag.tranditional_rag import TraditionalRAG
from rag.multimodal_rag import MultiModalRAG

app = FastAPI()

@app.post("/train/")
async def create_upload_files(collection_name: str):

    db_rag = DatabaseRAG(files=["./data"])
    await db_rag.create_index("chainlit")
    multi_modal_rag = MultiModalRAG(files=["./data"])
    await multi_modal_rag.create_index()
    return "index success"


@app.get("/")
async def main():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/train/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)

# mount_chainlit(app=app, target="ui.py", path="/chainlit")
# 启动fastapi命令： uvicorn app:app --host 0.0.0.0 --port 80