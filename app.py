import streamlit as st
import whisper
from datetime import datetime
from streamlit_mic_recorder import mic_recorder
from match_symptoms import match_symptoms
from pdf_utils import generate_pdf
from sidebar_ui import render_sidebar
from translate_output import translate_output
from translations import t
import joblib

st.set_page_config(page_title="Health Triage Assistant", page_icon="\U0001FA7A", layout="wide")
render_sidebar()

lang = st.session_state.get("output_lang", "en")

symptom_columns = joblib.load("symptom_columns.pkl")

if "history" not in st.session_state:
    st.session_state.history = []

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

whisper_model = load_whisper()

SEVERITY_STYLE = {
    "Emergency": ("\U0001F534", "#FEE2E2", "#B91C1C"),
    "See doctor soon": ("\U0001F7E1", "#FEF3C7", "#B45309"),
    "Self-care with monitoring": ("\U0001F7E2", "#DCFCE7", "#15803D"),
}

st.title(f"\U0001FA7A {t('app_title', lang)}")
st.caption(t("app_caption", lang))
st.divider()

st.subheader(f"\U0001F464 {t('patient_info', lang)}")
p1, p2, p3 = st.columns(3)
with p1:
    patient_name = st.text_input(t("name", lang), placeholder="e.g. Anshika")
with p2:
    patient_age = st.number_input(t("age", lang), min_value=0, max_value=120, value=25, step=1)
with p3:
    patient_gender = st.selectbox(t("gender", lang), ["Male", "Female", "Other"])

st.divider()

col_input, col_output = st.columns([1, 1], gap="large")

with col_input:
    tab1, tab2, tab3 = st.tabs([f"\U0001F3A4 {t('speak_tab', lang)}", f"\u2328\uFE0F {t('type_tab', lang)}", f"\u2705 {t('select_tab', lang)}"])

    with tab1:
        audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", key="recorder")

    with tab2:
        typed_text = st.text_area(t("describe_placeholder", lang), placeholder="e.g. I have itching and a skin rash", label_visibility="collapsed")

    voice_symptoms, typed_symptoms = [], []
    if audio:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio["bytes"])
        transcription = whisper_model.transcribe("temp_audio.wav", task="translate")
        text = transcription["text"]
        if text.strip():
            st.info(f"Heard: \"{text}\"")
        voice_symptoms = match_symptoms(text)

    if typed_text:
        typed_symptoms = match_symptoms(typed_text)

    with tab3:
        combined_defaults = list(set(voice_symptoms + typed_symptoms))
        manual_symptoms = st.multiselect("Symptoms", options=symptom_columns, default=combined_defaults, label_visibility="collapsed")

    check_clicked = st.button(t("check_button", lang), type="primary", use_container_width=True)

with col_output:
    if check_clicked:
        all_symptoms = list(set(manual_symptoms))
        if not patient_name.strip():
            st.error(t("name_required", lang))
        elif not all_symptoms:
            st.error(t("symptom_required", lang))
        else:
            with st.spinner("Analyzing..."):
                from triage import get_triage
                data = get_triage(all_symptoms)

            display_severity = translate_output(data["severity"], lang)
            display_explanation = translate_output(data.get("explanation", ""), lang)

            emoji, bg, fg = SEVERITY_STYLE.get(data["severity"], ("\u26AA", "#F1F5F9", "#334155"))
            st.markdown(
                f"""<div style="background-color:{bg}; padding:20px; border-radius:12px; border-left:6px solid {fg};">
                <h3 style="color:{fg}; margin:0;">{emoji} {display_severity}</h3>
                </div>""",
                unsafe_allow_html=True,
            )
            st.write("")

            if data.get("top_predictions"):
                st.write(f"**\U0001F52C {t('top_conditions', lang)}:**")
                for pred in data["top_predictions"]:
                    st.progress(pred["confidence"], text=f"{pred['condition']} \u2014 {pred['confidence']*100:.0f}%")

            st.write(display_explanation)

            entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "patient_name": patient_name,
                "patient_age": patient_age,
                "patient_gender": patient_gender,
                "symptoms": all_symptoms,
                "severity": data["severity"],
                "condition": data.get("condition"),
                "confidence": data.get("confidence"),
                "top_predictions": data.get("top_predictions", []),
            }
            st.session_state.history.append(entry)
            st.session_state.last_entry = entry

    if "last_entry" in st.session_state:
        pdf_bytes = generate_pdf(st.session_state.last_entry)
        st.download_button(f"\U0001F4C4 {t('download_pdf', lang)}", data=pdf_bytes, file_name="triage_report.pdf", mime="application/pdf", use_container_width=True)
    else:
        st.info(t("results_placeholder", lang))
