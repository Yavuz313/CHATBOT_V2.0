import json
import os
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 🔹 Daha güçlü bir embedding modeli kullanarak eşleşmeleri iyileştiriyoruz
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    encode_kwargs={"normalize_embeddings": True}
)

# 🔹 Q&A verisini yükleyip vektör veritabanı oluştur
def load_qa_and_create_vectorstore():
    with open("Q&A_cleaned.json", "r", encoding="utf-8") as f:
        qa_data = json.load(f)

    documents = [
        Document(
            page_content=f"Question: {item['QUESTION']}\nAnswer: {item['ANSWER']}",
            metadata={}
        )
        for item in qa_data
    ]

    text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    split_docs = text_splitter.split_documents(documents)

    persist_directory = "./vistula_chroma"

    # 🔹 Eğer eski veritabanı varsa, yeni veriyle yeniden oluştur
    if os.path.exists(persist_directory):
        os.system("rm -rf vistula_chroma")  # Eski vektör veritabanını siliyoruz

    vectordb = Chroma.from_documents(split_docs, embedding_model, persist_directory=persist_directory)

    return vectordb.as_retriever()
