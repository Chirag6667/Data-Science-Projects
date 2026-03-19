# app.py
# TalentLens - Main Application
# Intelligent Candidate Screening by TalentScout

import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from styles import get_styles
from prompts import get_system_prompt, get_welcome_message
from utils import (
    extract_candidate_info,
    detect_exit_intent,
    detect_stage,
    get_stage_progress,
    save_candidate_data
)

# Load environment variables
load_dotenv(override=True)

# Streamlit page config
st.set_page_config(
    page_title="TalentLens | TalentScout",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS 
st.markdown(get_styles(), unsafe_allow_html=True)

# Initialize Groq client 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize session state 
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = False

if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "name": None,
        "email": None,
        "phone": None,
        "location": None,
        "experience": None,
        "position": None,
        "tech_stack": None
    }

if "interview_complete" not in st.session_state:
    st.session_state.interview_complete = False

# Header
st.markdown("""
<div class="ts-header">
    <p class="ts-title">🔍 TalentLens</p>
    <p class="ts-subtitle">INTELLIGENT CANDIDATE SCREENING · POWERED BY TALENTSCOUT</p>
</div>
""", unsafe_allow_html=True)

# Stage Progress Bar
stage = detect_stage(st.session_state.messages)
progress = get_stage_progress(stage)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 10px;">
        <span class="stage-badge">{stage}</span>
    </div>
    """, unsafe_allow_html=True)
    st.progress(progress / 100)


# Main Chat Area

# Show welcome message if conversation not started
if not st.session_state.conversation_started:
    st.markdown(get_welcome_message())
    if st.button("🚀 Begin Interview", use_container_width=True):
        st.session_state.conversation_started = True
        # Add first bot message
        initial_message = "Welcome to TalentLens! I'm your AI hiring assistant from TalentScout." \
        " I'll be guiding you through a brief screening interview today. To get started, could you please tell me your full name?"
        st.session_state.messages.append({
            "role": "assistant",
            "content": initial_message
        })
        st.rerun()

else:
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(f"""
            <div class="bot-message">
                🔍 <strong>TalentLens</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="user-message">
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)

    # Chat input
    if not st.session_state.interview_complete:
        user_input = st.chat_input("Type your response here...")

        if user_input:
            # Add user message to history
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            # Check for exit intent
            if detect_exit_intent(user_input):
                st.session_state.interview_complete = True
                farewell = "Thank you for your time today! Your responses have been recorded and our TalentScout team will review them shortly." \
                            " You can expect to hear back from us within 3-5 business days. Best of luck! 🌟"
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": farewell
                })
                save_candidate_data(st.session_state.candidate_info)
                st.rerun()

            else:
                # Get LLM response
                with st.spinner("TalentLens is thinking..."):
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system",
                             "content": get_system_prompt()}
                        ] + st.session_state.messages,
                        temperature=0.7,
                        max_tokens=500
                    )

                bot_reply = response.choices[0].message.content

                # Add bot response to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

                # Extract candidate info from conversation
                extracted = extract_candidate_info(
                    st.session_state.messages
                )
                for key, value in extracted.items():
                    if value:
                        st.session_state.candidate_info[key] = value

                st.rerun()

    else:
        # Interview complete
        st.success("✅ Interview Complete! Thank you for your time.")
        if st.button("📥 Download Summary", use_container_width=True):
            summary = st.session_state.candidate_info
            st.json(summary)


