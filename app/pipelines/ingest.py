from parser.pdf_parser import load_pdf
from utils.file_selector import selectd_pdf
from splitter.chunker import split_documents
from vectorstore.faiss_store import build_vector_store, save_vector_store, load_vector_store

def ingest_pdf(context):
    pdf_path=selectd_pdf()
    documents=load_pdf(pdf_path)
    print("\nParsed Sucessfully")

    chunks=split_documents(documents)
    print("\nChunked Sucessfully")
    print(f"Pages: {len(documents)}")
    print(f"Chunks: {len(chunks)}")
    print("\nFirst Chunk Metadata: ")
    print(chunks[0].metadata)

    # embeddings=create_embeddings(model,chunks)
    # print(f"Embeddings: {len(embeddings)}")
    # print(f"Vector Size: {len(embeddings[0])}")
    embedding_model=context.embedding_model
    print("\nEmbedding Model loaded Sucessfully")

    vector_store=build_vector_store(chunks,embedding_model)
    save_vector_store(vector_store)
    print("\nVector Store Created Sucessfully")
    print("\nFAISS Index Saved")


