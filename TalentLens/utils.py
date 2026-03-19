# utils.py
# TalentLens - Helper functions
# Utilities functions for candidate data extraction and management

import json
import re
from datetime import datetime

def extract_candidate_info(conversation_history):
    """
    Extracts candidate information from conversation history
    Returns a dictionary with candidate details
    """
    candidate = {
        "name": None,
        "email": None,
        "phone": None,
        "location": None,
        "experience": None,
        "position": None,
        "tech_stack": None
    }

    full_text = " ".join([
        msg["content"] for msg in conversation_history
        if msg["role"] == "user"
    ])

    # Extract email using regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, full_text)
    if email_match:
        candidate["email"] = email_match.group()

    # Extract phone using regex
    phone_pattern = r'\+?\d[\d\s\-\(\)]{8,15}'
    phone_match = re.search(phone_pattern, full_text)
    if phone_match:
        candidate["phone"] = phone_match.group()

    # Extract name — first user message after greeting
    if len(conversation_history) >= 2:
        first_user_msg = next(
            (msg["content"] for msg in conversation_history 
             if msg["role"] == "user"), None
        )
        if first_user_msg and len(first_user_msg.split()) <= 5:
            candidate["name"] = first_user_msg.strip()

    # Extract experience — look for numbers followed by year keywords
    exp_pattern = r'(\d+)\s*(?:years?|yrs?|yr)?(?:\s+of)?\s+experience'
    exp_match = re.search(exp_pattern, full_text, re.IGNORECASE)
    if exp_match:
        candidate["experience"] = f"{exp_match.group(1)} years"

    # Extract tech stack — look for common tech keywords
    tech_keywords = [
        "python", "java", "javascript", "react", "node", "sql",
        "django", "flask", "tensorflow", "pytorch", "pandas",
        "numpy", "sklearn", "mongodb", "mysql", "postgresql",
        "docker", "kubernetes", "aws", "azure", "git", "html",
        "css", "typescript", "golang", "rust", "c++", "swift"
    ]
    found_techs = []
    for tech in tech_keywords:
        if tech.lower() in full_text.lower():
            found_techs.append(tech.capitalize())
    if found_techs:
        candidate["tech_stack"] = ", ".join(found_techs)

    # Extract location — look for city/country names after location keywords
    location_pattern = r'(?:from|in|at|location|based in|located in|location is| i am from| i live in| currently in| staying in)\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)'
    location_match = re.search(location_pattern, full_text, re.IGNORECASE)
    if location_match:
        candidate["location"] = location_match.group(1)

    return candidate

def detect_exit_intent(user_message):
    """
    Detects if user wants to exit the conversation
    Returns True if exit keyword detected
    """
    exit_keywords = [
        "exit", "quit", "bye", "goodbye", 
        "stop", "end", "finish", "done"
    ]
    return any(
        keyword in user_message.lower() 
        for keyword in exit_keywords
    )


def detect_stage(conversation_history):
    """
    Detects current interview stage based on conversation length
    Returns stage name as string
    """
    message_count = len(conversation_history)

    if message_count <= 2:
        return "🤝 Greeting"
    elif message_count <= 10:
        return "📋 Information Gathering"
    elif message_count <= 14:
        return "💻 Tech Stack"
    elif message_count <= 22:
        return "🧠 Technical Questions"
    else:
        return "✅ Completed"


def save_candidate_data(candidate_info):
    """
    Saves candidate data to a JSON file
    Simulates database storage for demo purposes
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"candidate_{timestamp}.json"

    data = {
        "timestamp": timestamp,
        "candidate": candidate_info
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename


def format_tech_stack(tech_string):
    """
    Formats tech stack string into clean list
    Example: "Python, Django, React" → ["Python", "Django", "React"]
    """
    if not tech_string:
        return []

    # Split by common separators
    techs = re.split(r'[,;/\n]+', tech_string)

    # Clean each item
    return [tech.strip() for tech in techs if tech.strip()]


def get_stage_progress(stage):
    """
    Returns progress percentage for stage tracker
    """
    stages = {
        "🤝 Greeting": 10,
        "📋 Information Gathering": 35,
        "💻 Tech Stack": 60,
        "🧠 Technical Questions": 85,
        "✅ Completed": 100
    }
    return stages.get(stage, 0)