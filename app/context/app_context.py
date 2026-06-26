from models.embedder import load_embedding_model
from langchain_huggingface import HuggingFaceEmbeddings
from models.gemini import load_llm

class AppContext: 
    def __init__(self):
        print("\nInitializing Application....\n")
        self.embedding_model: HuggingFaceEmbeddings=load_embedding_model() #The embedding model is loaded only once when the application starts.
        self.llm=load_llm()