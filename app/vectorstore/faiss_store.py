from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

VECTOR_STORE_PATH=Path("data/vectorstore/faiss_index")

def build_vector_store(
        documents: list[Document],
        embedding_model: Embeddings) -> FAISS:
    # creates a FAISS vector store from document chunks 
    return FAISS.from_documents(documents=documents,embedding=embedding_model)
    
def save_vector_store(vector_store: FAISS) ->None:
    VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(VECTOR_STORE_PATH
    ))

def load_vector_store(embedding_model: Embeddings) -> FAISS:
    return FAISS.load_local(
        folder_path=str(VECTOR_STORE_PATH),
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )
