from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def retrieve_documents(
        vector_store: FAISS,
        query: str,
        k: int=4) -> list[tuple[Document]]:
    # Retrieves the top-k documents along with their similarity scores.
    return vector_store.similarity_search_with_score(query=query, k=k)

