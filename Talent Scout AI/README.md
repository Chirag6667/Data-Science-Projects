# 🤖 TalentScout AI - Hiring Assistant Chatbot

## Overview
TalentScout AI is an intelligent hiring assistant chatbot built for tech recruitment screening. It conducts initial candidate interviews by collecting essential information and generating relevant technical questions based on the candidate's declared tech stack.

## Features
- 👋 Greets candidates and explains the screening process
- 📋 Collects candidate information sequentially:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position
  - Current Location
  - Tech Stack
- 💻 Generates 3-5 technical questions per technology declared
- 🔄 Maintains conversation context throughout the session
- 🚫 Stays focused on recruitment — ignores off-topic questions
- 👋 Gracefully ends conversation on keywords: bye, exit, quit, goodbye

## Two Versions Available

### Version 1 — Gemini (Google AI)
- Model: gemini-2.0-flash
- File: app_gemini.py
- API: Google AI Studio (free tier)

### Version 2 — Groq (LLaMA)
- Model: llama3-8b-8192
- File: app_groq.py
- API: Groq Console (free tier)

## Tech Stack
- Python
- Streamlit — frontend UI
- Google Generative AI — Gemini version
- Groq — LLaMA version
- Prompt Engineering — custom system prompts for hiring context

## Installation

### Step 1 — Install dependencies
pip install streamlit google-generativeai groq

### Step 2 — Set API key

For Gemini version:
Replace YOUR_GEMINI_API_KEY in app_gemini.py with your key from aistudio.google.com

For Groq version:
set GROQ_API_KEY=your_key_here  (Windows)
export GROQ_API_KEY=your_key_here  (Mac/Linux)

### Step 3 — Run the app

Gemini version:
streamlit run app.py

Groq version:
streamlit run app1.py

## How It Works
1. Candidate opens the chatbot in browser
2. TalentScout greets and begins collecting information one field at a time
3. After tech stack is declared, generates tailored technical questions
4. Candidate answers questions
5. Chatbot thanks candidate and explains next steps
6. Session ends gracefully

## Prompt Design
The system prompt instructs the LLM to:
- Act strictly as a hiring assistant
- Follow a sequential information gathering workflow
- Generate difficulty-appropriate technical questions based on years of experience
- Redirect off-topic conversations back to screening
- Maintain full conversation context

## Challenges & Solutions
- Gemini API quota issues — solved by switching to Groq as alternative sometimes this also doesn't works best if you have paid version
- Model name changes — updated to gemini-2.0-flash and llama3-8b-8192
- Context maintenance — solved using Streamlit session state to store full conversation history


