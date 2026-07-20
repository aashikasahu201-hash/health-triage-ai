import streamlit as st
from sidebar_ui import render_sidebar

st.set_page_config(page_title="About", page_icon="\u2139\uFE0F", layout="wide")
render_sidebar()

st.markdown("""
    <div style="text-align:center; padding: 30px 0;">
        <h1>\U0001FA7A Health Triage Assistant</h1>
        <p style="font-size:18px; color:#64748B;">AI-assisted symptom triage \u2014 built as a first end-to-end ML project</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("\U0001F3AF Accuracy", "92%")
col2.metric("\U0001FA7A Symptoms", "131")
col3.metric("\U0001F52C Conditions", "41")
col4.metric("\u26A1 Input methods", "3")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["\U0001F3AF What it does", "\U0001F9E9 How it works", "\U0001F4CA The model", "\u26A0\uFE0F Limitations"])

with tab1:
    st.write("")
    st.write(
        "This app takes your symptoms \u2014 spoken, typed, or manually selected \u2014 "
        "and gives you an urgency level plus a likely condition, powered by a "
        "machine learning model trained on a public symptom-disease dataset."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### \U0001F3A4 Speak")
        st.caption("Record your symptoms out loud, transcribed with OpenAI Whisper")
    with c2:
        st.markdown("#### \u2328\uFE0F Type")
        st.caption("Describe how you feel in your own words")
    with c3:
        st.markdown("#### \u2705 Select")
        st.caption("Pick exact symptoms from a searchable list")

with tab2:
    st.write("")
    st.markdown("""
    | Step | Layer | What it does |
    |---|---|---|
    | 1\ufe0f\u20e3 | **Rules** | Checks for red-flag symptoms (chest pain, breathlessness, etc). If found \u2192 immediate emergency recommendation, ML is skipped entirely. |
    | 2\ufe0f\u20e3 | **ML Model** | XGBoost classifier predicts the most likely condition from your symptoms. |
    | 3\ufe0f\u20e3 | **Explanation** | Converts the raw prediction into a plain-language summary with confidence. |
    | 4\ufe0f\u20e3 | **Diagnosis** | Looks up a description and precautions for the predicted condition. |
    """)
    st.info("\U0001F6E1\uFE0F Safety-critical symptoms always bypass the ML model \u2014 they're never left to a probabilistic guess.")

with tab3:
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Algorithm:** XGBoost (gradient boosted trees)")
        st.markdown("**Dataset:** Disease-Symptom Prediction (Kaggle)")
        st.markdown("**Test accuracy:** 92%")
    with c2:
        st.markdown("**Known data issue:** original dataset had ~4,600 duplicate rows out of 4,920")
        st.markdown("**Fix applied:** duplicates removed before training to avoid inflated, leaked accuracy")
    st.warning("\U0001F4A1 A perfect 100% score before cleaning was the signal that something was wrong \u2014 not a win. This is documented here deliberately as part of the model-building process.")

with tab4:
    st.write("")
    st.error("\U0001F6A8 This tool provides **triage guidance only** \u2014 it is not a medical diagnosis.")
    st.markdown("""
    - Trained on a limited, publicly available dataset, not real clinical records
    - Voice/text symptom matching uses keyword matching \u2014 may miss unusual phrasing
    - Some conditions have very few training examples, reducing reliability per class
    - Always consult a qualified healthcare professional for real medical concerns
    """)

st.divider()
st.markdown("<p style='text-align:center; color:#94A3B8;'>Built with Python \u00b7 FastAPI \u00b7 XGBoost \u00b7 scikit-learn \u00b7 Streamlit \u00b7 OpenAI Whisper \u00b7 fpdf2</p>", unsafe_allow_html=True)
