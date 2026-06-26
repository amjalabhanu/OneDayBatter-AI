from pathlib import Path

PDF_DIRECTORY=Path("data/pdfs") #Path Object from pathlib module

def selectd_pdf()->str:
    pdf_files=list(PDF_DIRECTORY.glob("*.pdf")) #searches directory for all files ending with .pdf.
    #glob() returns an iterator (generator-like object), not a list. So wrapping it with list(...) converts it into a list
    if not pdf_files:
        print("\nNo PDFs Found! Please add PDF to data/pdfs/ to access them.")
        exit() #stop the execution of a Python program immediately
    print("\nAvailable PDFs:\n")
    for index,pdf in enumerate(pdf_files, start=1):
        print(f"{index}.{pdf.name}")
    while True:
        try:
            choice=int(input("\nSelect a PDF: "))
            if 1<=choice<=len(pdf_files):
                return str(pdf_files[choice-1])
            print("\nInvalid choice. Try again!")
        except ValueError:
            print("\nPlease enter a valid number.")
        






