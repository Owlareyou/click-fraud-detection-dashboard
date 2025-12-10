"""
Configuration and styling for the Click Fraud Detection dashboard.
"""

# Page configuration
PAGE_CONFIG = {
    "page_title": "Click Fraud Detection Analysis",
    "page_icon": "🔍",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Custom CSS styling
CUSTOM_CSS = """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .team-info {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    </style>
"""

# Team information
TEAM_MEMBERS = ["Ching Chuang", "Jia-Ning Hu", "Yu-Chieh Chen"]
TEAM_STRING = " | ".join(TEAM_MEMBERS)

# Project information
PROJECT_TITLE = "TalkingData AdTracking Fraud Detection"
PROJECT_ICON = "🔍"