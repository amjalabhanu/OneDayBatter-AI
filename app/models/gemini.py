import os
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import api_key


def load_llm() -> ChatGoogleGenerativeAI:
    print("\nLoading Gemini....")
    print(f"{api_key}")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.2
    )

def generate_response(llm: ChatGoogleGenerativeAI, prompt):
    return llm.invoke(prompt)