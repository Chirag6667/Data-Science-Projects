# styles.py
# TalentLens - Custom CSS Theme
# Dark Navy + Gold luxury theme for premium hiring experience

def get_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Inter:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0a0f1e;
        color: #e8e8e8;
    }
    .ts-header {
        background: linear-gradient(135deg, #0a0f1e 0%, #1a2340 100%);
        border-bottom: 2px solid #c9a84c;
        padding: 1.5rem 2rem;
        margin-bottom: 1rem;
    }
    .ts-title {
        font-family: 'Playfair Display', serif;
        color: #c9a84c;
        font-size: 2rem;
        letter-spacing: 2px;
        margin: 0;
    }
    .ts-subtitle {
        color: #8899aa;
        font-size: 0.85rem;
        letter-spacing: 1px;
        margin: 0;
    }
    .bot-message {
        background: linear-gradient(135deg, #1a2340 0%, #1e2a45 100%);
        border-left: 3px solid #c9a84c;
        border-radius: 0 12px 12px 12px;
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 80%;
        color: #e8e8e8;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .user-message {
        background: linear-gradient(135deg, #1e3a2a 0%, #1a3525 100%);
        border-right: 3px solid #4caf7d;
        border-radius: 12px 0 12px 12px;
        padding: 12px 16px;
        margin: 8px 0 8px auto;
        max-width: 80%;
        color: #e8e8e8;
        font-size: 0.95rem;
        text-align: right;
    }
    .profile-card {
        background: linear-gradient(135deg, #1a2340 0%, #1e2a45 100%);
        border: 1px solid #c9a84c33;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .profile-title {
        font-family: 'Playfair Display', serif;
        color: #c9a84c;
        font-size: 1rem;
        border-bottom: 1px solid #c9a84c44;
        padding-bottom: 0.5rem;
        margin-bottom: 0.8rem;
    }
    .profile-item {
        color: #8899aa;
        font-size: 0.8rem;
        margin: 4px 0;
    }
    .profile-value {
        color: #e8e8e8;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .stage-badge {
        background: #c9a84c22;
        border: 1px solid #c9a84c;
        color: #c9a84c;
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.75rem;
        letter-spacing: 1px;
    }
    .stTextInput input {
        background: #1a2340 !important;
        border: 1px solid #c9a84c44 !important;
        border-radius: 8px !important;
        color: #e8e8e8 !important;
    }
    .stTextInput input:focus {
        border-color: #c9a84c !important;
        box-shadow: 0 0 0 2px #c9a84c22 !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #c9a84c, #b8943d) !important;
        color: #0a0f1e !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
    }
    .stChatMessage {
        background: transparent !important;
    }
    .stChatInputContainer {
        background: #0a0f1e !important;
        border-top: 1px solid #c9a84c44 !important;
    }
    .stChatInput {
        background: #1a2340 !important;
        border: 1px solid #c9a84c44 !important;
        color: #e8e8e8 !important;
        border-radius: 8px !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """