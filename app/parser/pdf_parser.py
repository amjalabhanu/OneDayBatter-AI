from pathlib import Path
from langchain_core.documents import Document
import pymupdf

def load_pdf(pdf_path:str)->list[Document]:
    pdf_path=Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    pdf=pymupdf.open(pdf_path)
    documents=[]
    try:
        for page_number, page in enumerate(pdf,start=1):
            text=page.get_text()
            document=Document(
                page_content=text,
                metadata={
                    "source":pdf_path.name,
                    "page":page_number
                }
            )
            documents.append(document)
    finally:
        pdf.close()
    return documents