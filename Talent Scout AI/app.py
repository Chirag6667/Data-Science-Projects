import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBXl9rsBvPTCDzDphZDpSyb7TQhYfQE6C4") # API KEY HERE
model = genai.GenerativeModel('gemini-2.0-flash') # Initializing Gemini Model

SYSTEM_PROMPT = """
You are TalentScout, a professional AI Hiring Assistant for a tech recruitment agency.
Your ONLY purpose is to screen technology job candidates.

STRICT RULES:
- Never deviate from hiring/recruitment topics
- If asked anything unrelated, politely redirect back to screening
- Be professional, friendly and encouraging
- Exit gracefully if user says: bye, exit, quit, goodbye

YOUR WORKFLOW - Follow this exact sequence:
1. Greet the candidate warmly and explain your purpose
2. Collect information ONE BY ONE in this order"
    - Full Name
    - Email Address
    - Phone Number
    - Years of Experience
    - Desired Position
    - Current Location
    - Tech Stack (programming languages. frameworks, databases, tools)
3. Once Tech Stack is collected, generate 3-5 techical questions FOR EACH Technology mentioned
4. After questions are answered, thank the candidate and explain next steps
5. End conversation gracefully

TECHNICAL QUESTIONS RULES:
- Questions must be specific to the technology mentioned
- Match difficulty to years of experience
- Example: If candidate says Python + Django, ask about Python OOP, decorators, Django ORM, middleware etc.

CONTEXT:
- Always remember previous messages in the conversation
- Never ask for information already provided
- Keep responses concise and professional
"""

# STREAMLIT UI CONFIG

#TITLE
st.set_page_config(
    page_title="TalentScout - AI Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# PAGE HEADER
st.title("🤖 TalentScout")
st.subheader("AI-Powered Hiring Assistant")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

    st.session_state.chat.send_message(SYSTEM_PROMPT)

    initial_response = st.session_state.chat.send_message(
        "Start the conversation by greeting the candidate."
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": initial_response.text
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Box
user_input = st.chat_input("Type your message here...")

if user_input:
    
    exit_keywords = ["bye","exit", "quit", "goodbye", "stop"]

    if any(keyword in user_input.lower() for keyword in exit_keywords):
        st.session_state.messages.append({
                    "role": "user",
                    "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)
        
        goodbye = "Thank you for your time! We will review your profile and get back to you within 3-5 bussiness day. Best of luck!👋"
        st.session_state.messages.append({
            "role": "assistant",
            "content": goodbye
        })
        with st.chat_message("assistant"):
            st.markdown(goodbye)
    
    else:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)
        
        try:
            response = st.session_state.chat.send_message(user_input)
            bot_response = response.text
        
        except Exception as e:
            bot_response = f"API Error: {str(e)}" # Fallback if API fails

        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response
        })

        with st.chat_message("assistant"):
            st.markdown(bot_response)