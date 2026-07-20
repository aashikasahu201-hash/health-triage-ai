import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from sidebar_ui import render_sidebar

st.set_page_config(page_title="Health Chatbot", page_icon="\U0001F916")
render_sidebar()
lang = st.session_state.get("output_lang", "en")

LANG_NAMES = {
    "en": "English", "hi": "Hindi", "bn": "Bengali", "ta": "Tamil", "te": "Telugu",
    "mr": "Marathi", "gu": "Gujarati", "kn": "Kannada", "ml": "Malayalam", "pa": "Punjabi",
    "ur": "Urdu", "or": "Odia", "es": "Spanish", "fr": "French", "de": "German",
    "pt": "Portuguese", "ar": "Arabic", "zh-CN": "Chinese", "ja": "Japanese", "ru": "Russian",
}
lang_name = LANG_NAMES.get(lang, "English")

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.title("\U0001F916 Health Chatbot")
st.caption("Ask general health questions \u2014 not a substitute for medical advice.")
st.divider()

if not api_key:
    st.error("Gemini API key not configured. Add GEMINI_API_KEY to your .env file to enable the chatbot.")
    st.stop()

genai.configure(api_key=api_key)

SYSTEM_INSTRUCTION = (
    f"You are a friendly, careful health information assistant. Understand the user's "
    f"message in whatever language they write it in. Always respond in {lang_name}, "
    f"regardless of the language the user used. You are NOT a doctor and must never "
    f"diagnose, prescribe medication, or give specific dosages. For anything serious, "
    f"urgent, or personal, tell the user to consult a qualified healthcare professional. "
    f"Keep answers concise (3-5 sentences) unless the user asks for more detail."
)

if "chat_session" not in st.session_state or st.session_state.get("chat_lang") != lang:
    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=SYSTEM_INSTRUCTION)
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.chat_messages = []
    st.session_state.chat_lang = lang

for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a health question...")

if user_input:
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                reply = response.text
            except Exception as e:
                reply = f"Sorry, something went wrong: {e}"
        st.write(reply)

    st.session_state.chat_messages.append({"role": "assistant", "content": reply})

st.divider()
st.caption("\u26A0\uFE0F This chatbot provides general information only, not medical advice or diagnosis.")

if st.button("\U0001F5D1\uFE0F Clear conversation"):
    st.session_state.chat_messages = []
    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=SYSTEM_INSTRUCTION)
    st.session_state.chat_session = model.start_chat(history=[])
    st.rerun()
