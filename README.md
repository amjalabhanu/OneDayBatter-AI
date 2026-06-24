# OneDayBatter AI — RAG-Powered Last-Minute Study Notes Generator

> Upload your lecture slides, textbooks, or notes and get clean, structured summaries instantly. Built for students who study the day before.

---

## What It Does

OneDayBatter AI is a terminal-based RAG (Retrieval-Augmented Generation) pipeline that takes your raw study material and generates concise, well-structured notes, so you can focus on understanding, not reading through hundreds of pages.

**Input:** PDFs
**Output:** Clean, structured notes in the terminal, saved as Markdown, PDF, or Word

---

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| PDF Parsing | `PyMuPDF` | Extract text from PDFs and slides |
| Chunking | `LangChain` RecursiveCharacterTextSplitter | Split documents into retrievable chunks |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) | Convert chunks to vectors locally |
| Vector Store | `FAISS` | Fast local similarity search |
| Orchestration | `LangChain` | RAG pipeline wiring |
| LLM | `Gemini 1.5 Flash` (Google AI) | Generate structured notes |
| CLI Output | `Rich` + `Typer` | Pretty terminal interface |
| Export | `python-docx` / `fpdf2` | Save notes as PDF or Word |
| History | `SQLite` | Track past sessions |

---

## 🔍 How the RAG Pipeline Works

```
Your File
   │
   ▼
Parse & Extract Text (PyMuPDF)
   │
   ▼
Split into Chunks (LangChain)
   │
   ▼
Embed Chunks → Vectors (sentence-transformers)
   │
   ▼
Store in FAISS Index
   │
   ▼
Query: Retrieve Top-K Relevant Chunks
   │
   ▼
Send to Gemini 1.5 Flash with Prompt
   │
   ▼
Structured Notes → Terminal / File
```

---


## Roadmap

- [ ] Multi-file ingestion in one session
- [ ] Web URL ingestion (scrape and embed)
- [ ] Flashcard generation mode
- [ ] Quiz generation from notes
- [ ] Web UI (future phase)

---

> Built for students, by a student. Because reading 200 slides the night before shouldn't feel impossible.
