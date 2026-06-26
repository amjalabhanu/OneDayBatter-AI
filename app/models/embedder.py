# from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
#This wrapper internally uses sentence-transformers, but it implements the interface that LangChain's vector stores (like FAISS) expect.

def load_embedding_model()->HuggingFaceEmbeddings: #loads embedding model separately
    print("\nLoading Embedding Model....")
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")



# this create manual embeddings which is not that flexible for a production level project so replacing with the langchain
# wrapper so it would be automatically generate embeddings and FAISS calls the model.


# def create_embeddings(model: SentenceTransformer, documents: list[Document]):
#     """
#     Creates embeddings for each document chunk.

#     Args:
#         documents: List of LangChain Document objects.

#     Returns:
#         List of embeddings (one embedding per document).
#     """
#     texts=[doc.page_content for doc in documents]

#     embeddings=model.encode(
#         texts,
#         convert_to_numpy=True,
#         show_progress_bar=True
#     )
#     return embeddings