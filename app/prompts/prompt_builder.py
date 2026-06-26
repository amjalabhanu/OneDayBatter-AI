#The prompt builder assembles Query and Retrieved info into one prompt.
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from prompts.system_prompt import SYSTEM_PROMPT

def build_prompt(question: str, documents: list[Document]):
    context = "\n\n".join(
        document.page_content
        for document in documents
    )
    
    prompt=ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_PROMPT
            ),
            (
                "human",
                """
Context:
{context}

Question:
{question}
""",
            )
        ]
    )
    return prompt.invoke(
        {
            "context": context, 
            "question": question,
        }
    )


