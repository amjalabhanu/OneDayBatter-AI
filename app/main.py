from context.app_context import AppContext
from pipelines.ingest import ingest_pdf
from pipelines.query import ask_question

def main():
    context=AppContext()
    while True:
        print("\n1.Ingest PDF")
        print("\n2.Ask Questions")
        print("\n3. Exit")
        try:
            choice=int(input(">"))
        except ValueError:
            print("\nInvalid! Retry")
            continue
        if(choice==1):
            ingest_pdf(context)
        elif choice==2:
            ask_question(context)
        elif choice==3:
            print("\nThank you for using OneDayBatterAI!")
            break
        else:
            print("\nInvalid! Retry")

if __name__=="__main__":
    main()