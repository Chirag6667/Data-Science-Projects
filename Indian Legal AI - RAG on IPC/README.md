# 🏛️ Indian Legal AI — RAG on Complete IPC

> An AI-powered legal assistant built on the complete **Indian Penal Code (IPC)** using Retrieval Augmented Generation (RAG). Ask any legal question and get accurate answers backed by actual IPC sections.

Python, LangChain, Groq, HuggingFace

---

## 🎯 What it does

Ask natural language questions about Indian law and get accurate, context-aware answers sourced directly from the official IPC document.

```
"What is the punishment for murder?"
→ "Death or imprisonment for life + fine — Section 302 IPC"
```

---

## ⚡ RAG Pipeline

```
IPC.pdf (119 pages)
    → PyPDFLoader (extract text)
    → RecursiveCharacterTextSplitter (1146 chunks)
    → HuggingFace Embeddings (all-MiniLM-L6-v2)
    → ChromaDB (vector store)
    → User Question (retrieves top 3 chunks)
    → LLaMA 3.3 70B via Groq (generates answer)
```

---

## 🔧 Tech Stack

| Component | Tool |
|-----------|------|
| Framework | LangChain LCEL |
| LLM | LLaMA 3.3 70B via Groq API |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |
| PDF Loader | PyPDFLoader |
| Data | Official IPC PDF — 119 pages, 511 sections |

---

## 📐 Key Concepts

### Why RAG?
LLMs hallucinate on domain-specific legal questions. RAG grounds the LLM by retrieving actual IPC sections before answering — no hallucinations, just facts.

### Chunking Strategy
```
chunk_size = 500
chunk_overlap = 50
```
Overlap ensures no legal section gets cut at chunk boundaries.

### Retrieval
```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```
Top 3 most relevant IPC chunks are retrieved per question.

---

## 💬 Sample Results

**Q:** What is the punishment for murder?
**A:** Death or imprisonment for life + fine — Section 302 IPC

**Q:** What are the IPC sections for kidnapping?
**A:** Sections 359, 360, 365, 366, 367, 368, 364A — each covering different types of kidnapping

**Q:** What happens if someone causes arson?
**A:** Liable under Section 285 — imprisonment up to 6 months or fine up to ₹1000 or both

---

## 🔑 Setup

1. Get free Groq API key from [console.groq.com](https://console.groq.com)
2. Add it in the notebook:
```python
os.environ["GROQ_API_KEY"] = "your_key_here"
```

---
