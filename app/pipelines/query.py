from retrieval.retriever import retrieve_documents
from vectorstore.faiss_store import load_vector_store
from prompts.prompt_builder import build_prompt
from models.gemini import generate_response

def ask_question(context):
    print("\nLoading Vector Store....")
    embedding_model=context.embedding_model
    vector_store=load_vector_store(embedding_model)
    query=input("\nHeyy! What do you want to know about?")
    documents=retrieve_documents(vector_store,query)
    print("\nRetrieved Documents")
    doc=[]
    for rank,(document,score) in enumerate(documents, start=1):
        doc.append(document)
        print("-" * 60)
        print(f"Rank : {rank}")
        print(f"Score : {score:.4f}")
        print(f"Source: {document.metadata['source']}")
        print(f"Page : {document.metadata['page']}")
        print()
        PREVIEW_LENGTH=300
        print(document.page_content[:PREVIEW_LENGTH])
        print()
    prompt=build_prompt(question=query, documents=doc)
    print("\nPrompt builder message:\n")
    for index, message in enumerate(prompt.messages, start=1):
        print("-"*50)
        print(f"Message {index}")
        print(message.type.upper())
        print("-"*50)
        print(message.content)
        print()
    response=generate_response(context.llm, prompt)
    print("\nAnswer for your question is:\n")
    print(response.content)