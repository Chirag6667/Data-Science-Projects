```
# 📞 Call Center NLP Pipeline

> End-to-end NLP pipeline for analyzing call center transcripts — 10 NLP tasks from PII redaction to RAG-based question answering, wrapped in an interactive Streamlit dashboard.

---

## 🎯 Project Overview

Built as part of my **100 Days of ML Challenge (Days 31–35)**, this project demonstrates a production-style NLP pipeline on real call center data. The goal was to build every layer of a real call center AI system — from raw transcript cleaning to an interactive RAG assistant that answers natural language questions about customer calls.

---

## 🗂️ Dataset

**[Call Center Transcripts Dataset](https://www.kaggle.com/datasets/oleksiymaliovanyy/call-center-transcripts-dataset)**

- 20 real call center transcripts
- Columns: `id`, `Type`, `Sentiment`, `Name`, `Order Number`, `Product Number`, `Transcript`
- 5 call types: Product Inquiry, Complaint, Technical Issue, Compliment, Order Placement
- 5 sentiment labels: Neutral, Happy, Angry, Frustrated, Confused

---

## ✅ Tasks Implemented

| # | Task | Approach | Library |
|---|---|---|---|
| 1 | Exploratory Data Analysis | Distribution charts, missing value analysis, transcript length | Pandas, Matplotlib |
| 2 | PII Redaction | Rule-based name/order/product masking + regex | spaCy + re |
| 3 | Named Entity Recognition | Entity extraction with labels (PERSON, ORG, DATE) | spaCy en_core_web_sm |
| 4 | Sentiment Analysis | Pretrained binary classifier vs existing labels | DistilBERT SST-2 |
| 5 | Call Summarization | Abstractive summarization of all 20 transcripts | BART-large-CNN |
| 6 | Keyword Extraction | Top 5 keyphrases per transcript | KeyBERT |
| 7 | Topic Classification | Zero-shot, no training data needed | BART-large-MNLI |
| 8 | Intent Classification | Zero-shot with custom intent labels | BART-large-MNLI |
| 9 | Customer Clustering | Unsupervised grouping with visualization | TF-IDF + KMeans + PCA |
| 10 | RAG Assistant | Natural language Q&A over all transcripts | ChromaDB + MiniLM + FLAN-T5 |

---

## 🏗️ Pipeline Architecture

```
Raw Transcript
      ↓
PII Redaction ──────────── spaCy + Regex
      ↓
Named Entity Recognition ── spaCy
      ↓
Sentiment Analysis ─────── DistilBERT
      ↓
Topic Classification ───── Zero-shot BART
      ↓
Intent Classification ──── Zero-shot BART
      ↓
Keyword Extraction ─────── KeyBERT
      ↓
Call Summarization ─────── BART-CNN
      ↓
Customer Clustering ────── TF-IDF + KMeans + PCA
      ↓
RAG Assistant ──────────── ChromaDB + FLAN-T5
      ↓
Streamlit Dashboard ────── All outputs in one UI
```

---

## 🔑 Key Results

| Task | Result |
|---|---|
| Topic Classification | **85% accuracy** with zero training data |
| Clustering | **4/5 clusters** perfectly separated by call type |
| RAG Retrieval | Correctly retrieves relevant transcripts every time |
| PII Redaction | **100%** of names, order numbers, product numbers masked |
| Summarization | All 20 transcripts summarized to under 60 words |
| Keyword Extraction | 5 relevant keyphrases extracted per call |

---

## 💡 Key Insights

- **Zero-shot classification works surprisingly well** — BART-MNLI achieved 85% topic accuracy with no labeled training data, by leveraging natural language inference
- **Neutral sentiment is misclassified by DistilBERT** — because it was trained on movie reviews (binary: positive/negative), not call center language. This shows why domain-specific fine-tuning matters
- **KMeans found real patterns** — Cluster 1 captured all compliments, Cluster 2 captured all product inquiries, purely from transcript text with no labels
- **RAG retrieval is the strongest component** — ChromaDB consistently finds the 3 most relevant calls for any question asked

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| NLP Models | HuggingFace Transformers, spaCy |
| LLMs Used | BART-large-CNN, BART-large-MNLI, DistilBERT, FLAN-T5-base |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| RAG Framework | LangChain |
| ML Algorithms | TF-IDF, KMeans, PCA |
| Keyword Extraction | KeyBERT |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Environment | Python 3.10, Anaconda |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/chirag6667/call-center-nlp-pipeline
cd call-center-nlp-pipeline
```

**2. Create and activate environment**
```bash
conda create -n callcenter python=3.10
conda activate callcenter
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**3. Run the notebook**

Open Jupyter and run `notebooks/call_center_nlp.ipynb` from top to bottom.

**4. Launch the Streamlit dashboard**
```bash
streamlit run app/app.py
```

---

## 📁 Project Structure

```
call-center-nlp-pipeline/
│
├── notebooks/
│   └── call_center_nlp.ipynb       ← Full pipeline (Days 1-3)
│
├── app/
│   └── app.py                      ← Streamlit dashboard (Day 4)
│
├── data/
│   └── call_recordings.csv         ← Dataset
│
├── requirements.txt                ← All dependencies
└── README.md                       ← This file
```

---

## 📊 Dashboard Features

| Tab | What it shows |
|---|---|
| 📊 Overview & EDA | Dataset stats, sentiment distribution, call type pie chart, full data table |
| 🔍 Analyze a Call | Paste any transcript → get sentiment, topic, intent, summary, keywords, PII redaction |
| 🤖 RAG Assistant | Ask natural language questions about all 20 calls, see source transcripts |
| 🗂️ Cluster Explorer | PCA scatter plot, filter calls by cluster |

---

## 🧠 What I Learned

- How to build a **multi-task NLP pipeline** on a single dataset
- The difference between **extractive vs abstractive summarization**
- Why **zero-shot classification** is powerful for low-data scenarios
- How **RAG works** end-to-end: embed → store → retrieve → generate
- Why **domain mismatch** matters: pretrained models trained on different data fail on specialized text
- How to use **@st.cache_resource** to prevent model reloading in Streamlit

---
