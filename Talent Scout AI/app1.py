import streamlit as st
from groq import Groq


# ============================================
# INITIALIZE GROQ CLIENT
# ============================================

client = Groq(api_key="Your API KEY OF GROQ")

# ============================================
# SYSTEM PROMPT
# ============================================

SYSTEM_PROMPT = """
You are TalentScout, a professional AI Hiring Assistant for a tech recruitment agency.
Your ONLY purpose is to screen technology job candidates.

STRICT RULES:
- Never deviate from hiring topics
- If asked unrelated questions, redirect politely
- Be professional and concise
- Exit gracefully if user says bye, exit, quit, goodbye

WORKFLOW:
1. Greet candidate
2. Collect information ONE BY ONE:
- Full Name
- Email
- Phone
- Years of Experience
- Desired Position
- Location
- Tech Stack
3. After tech stack, generate 3-5 technical questions per technology
4. After answers, thank candidate and explain next steps
"""

# ============================================
# STREAMLIT PAGE SETUP
# ============================================

st.set_page_config(
    page_title="TalentScout - AI Hiring Assistant",
    page_icon="🤖"
)

st.title("🤖 TalentScout")
st.subheader("AI-Powered Hiring Assistant")
st.markdown("---")

# ============================================
# SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello! Welcome to TalentScout. Let's begin. Could you please share your full name?"}
    ]

# ============================================
# DISPLAY CHAT HISTORY
# ============================================

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ============================================
# USER INPUT
# ============================================

user_input = st.chat_input("Type your message here...")

if user_input:

# Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

# Exit handling
    exit_words = ["bye", "exit", "quit", "goodbye", "stop"]

    if any(word in user_input.lower() for word in exit_words):

        goodbye_message = "Thank you for your time. We will review your profile and get back to you within 3-5 business days. Best of luck! 👋"

        st.session_state.messages.append(
            {"role": "assistant", "content": goodbye_message}
        )

        with st.chat_message("assistant"):
            st.markdown(goodbye_message)

    else:
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content

        except Exception as e:
            bot_reply = "There was an issue connecting to the AI service. Please try again."

# Store assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        with st.chat_message("assistant"):
            st.markdown(bot_reply)