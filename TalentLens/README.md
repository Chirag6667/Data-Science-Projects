# 🔍 TalentLens — Intelligent Candidate Screening

> AI-powered hiring assistant built for TalentScout recruitment agency.
> Screens candidates through natural conversation using LLaMA 3.3 70B via Groq.

---

## 🌟 Features

- Natural conversational interview flow (Greeting → Info → Tech Stack → Questions → Farewell)
- Auto-generates 3-5 technical questions based on candidate's declared tech stack
- Live candidate profile extraction (name, email, phone, location, experience)
- Fallback handling for off-topic responses
- Exit keyword detection (bye, quit, exit, sayonara etc.)
- Premium dark navy + gold UI theme
- Progress tracker showing current interview stage

---

## 🛠️ Tech Stack

- Python 3.12
- Streamlit — frontend UI
- Groq API — LLaMA 3.3 70B language model
- python-dotenv — environment variable management

---

## ⚙️ Installation

1. Clone the repository:


git clone (https://github.com/Chirag6667/Data-Science-Projects/tree/main/TalentLens)   
cd TalentLens


2. Create and activate virtual environment:


python -m venv venv
venv\Scripts\activate


3. Install dependencies:


pip install -r requirements.txt


4. Create `.env` file and add your Groq API key:


GROQ_API_KEY=your_groq_api_key_here


5. Run the app:


streamlit run app.py


---

## 🎯 Prompt Design

TalentLens uses a structured system prompt with 5 defined stages:
- Stage 1 — Greeting and introduction
- Stage 2 — Candidate information gathering (one field at a time)
- Stage 3 — Tech stack declaration
- Stage 4 — Auto-generated technical questions tailored to declared stack
- Stage 5 — Professional farewell with next steps

Strict rules prevent the model from going off-topic, revealing instructions,
or asking multiple questions at once.

---

## 💡 Challenges and Solutions

- **Context maintenance** — solved by sending full conversation history
  with every API call
- **Info extraction** — solved using regex patterns for email/phone
  and keyword matching for tech stack
- **Consistent flow** — solved via strict staged system prompt
- **Environment variables on Streamlit** — solved using
  `load_dotenv(override=True)`

---

## 📁 Project Structure



TalentLens/    
├── app.py          → Main Streamlit application   
├── prompts.py      → LLM system prompt and messages   
├── utils.py        → Helper functions and info extraction      
├── styles.py       → Custom CSS dark navy + gold theme    
├── requirements.txt     
└── README.md     


---

## 🔗 Links

- GitHub: [https://github.com/Chirag6667/TalentLens](https://github.com/Chirag6667/Data-Science-Projects/tree/main/TalentLens)
- Live Demo: (Streamlit Cloud link after deployment)

---

Built by Chirag Jain | AI/ML 
