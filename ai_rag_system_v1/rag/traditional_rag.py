import asyncio
import os

from llama_index.core import SimpleDirectoryReader, Document

from .base_rag import RAG
from .ocr import ocr_to_file_from_llm, ocr_image_or_pdf_to_text_from_umi_ocr


class TraditionalRAG(RAG):

    async def load_data(self):
        """
        加载数据，该函数需要优化文件内容的识别、清洗
        :return:
        """
        docs = []
        for file in self.files:
            # 对图片及文档通过umi-ocr进行OCR识别
            # f_name = ocr_image_or_pdf_to_text_from_umi_ocr(file)
            # 对图片及文档通过Moonshot大模型进行OCR识别

            # 可以扩展文件的清洗处理，确保最后生成的文件是高质量的
            f_name = ocr_to_file_from_llm(file)

            data = SimpleDirectoryReader(input_files=[f_name]).load_data()
            doc = Document(text="\n\n".join([d.text for d in data[0:]]), metadata={"path": file})
            docs.append(doc)
            os.remove(f_name)
        return docs

if __name__ == "__main__":
    rag = TraditionalRAG(files=["../test_data/222.jpg"])
    asyncio.run(rag.create_index_local())
