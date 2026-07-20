import streamlit as st

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Odia": "or",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Portuguese": "pt",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
}

def render_sidebar():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    if "output_lang" not in st.session_state:
        st.session_state.output_lang = "en"

    if st.session_state.dark_mode:
        bg, text, card = "#0F172A", "#E2E8F0", "#1E293B"
    else:
        bg, text, card = "#FFFFFF", "#0F172A", "#F1F5F9"

    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {bg};
            color: {text};
        }}
        [data-testid="stSidebar"] {{
            background-color: #0F172A;
        }}
        [data-testid="stSidebar"] * {{
            color: #E2E8F0 !important;
        }}
        [data-testid="stSidebarNav"] li div a {{
            border-radius: 8px;
            margin: 2px 0;
        }}
        [data-testid="stSidebarNav"] li div a:hover {{
            background-color: #1E293B;
        }}
        [data-testid="stSidebar"] hr {{
            border-color: #334155;
        }}
        [data-testid="stMetric"] {{
            background-color: {card};
            padding: 10px;
            border-radius: 10px;
        }}
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("## \U0001FA7A Health Triage AI")
        st.caption("AI-assisted triage \u2014 not a diagnosis")

        mode_label = "\U0001F319 Dark mode" if not st.session_state.dark_mode else "\u2600\uFE0F Light mode"
        st.session_state.dark_mode = st.toggle(mode_label, value=st.session_state.dark_mode)

        selected_lang_name = st.selectbox("\U0001F310 Output language", list(LANGUAGES.keys()))
        st.session_state.output_lang = LANGUAGES[selected_lang_name]

        st.divider()

        if "history" not in st.session_state:
            st.session_state.history = []

        total = len(st.session_state.history)
        emergencies = sum(1 for e in st.session_state.history if e["severity"] == "Emergency")

        col1, col2 = st.columns(2)
        col1.metric("\U0001F9EE Checks", total)
        col2.metric("\U0001F6A8 Alerts", emergencies)

        if st.session_state.history:
            last = st.session_state.history[-1]
            emoji = {"Emergency": "\U0001F534", "See doctor soon": "\U0001F7E1", "Self-care with monitoring": "\U0001F7E2"}.get(last["severity"], "\u26AA")
            st.info(f"{emoji} Last: **{last['severity']}**")
        else:
            st.caption("No checks yet this session")

        st.divider()
        st.caption("Built with FastAPI + XGBoost + Whisper")
