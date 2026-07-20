content = """import streamlit as st
import requests
import whisper
from streamlit_mic_recorder import mic_recorder
from match_symptoms import match_symptoms
import joblib

st.title("Health Triage Assistant")
st.warning("This tool provides triage guidance only, not a diagnosis.")

symptom_columns = joblib.load("symptom_columns.pkl")

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

whisper_model = load_whisper()

st.subheader("Option 1: Speak your symptoms")
audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", key="recorder")

voice_symptoms = []
if audio:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio["bytes"])
    transcription = whisper_model.transcribe("temp_audio.wav")
    text = transcription["text"]
    st.write(f"Transcribed: {text}")
    voice_symptoms = match_symptoms(text)
    st.write(f"Matched symptoms: {voice_symptoms}")

st.subheader("Option 2: Select symptoms manually")
manual_symptoms = st.multiselect("Select your symptoms", options=symptom_columns, default=voice_symptoms)

if st.button("Check"):
    all_symptoms = list(set(manual_symptoms))
    if not all_symptoms:
        st.error("Please select at least one symptom.")
    else:
        res = requests.post("http://127.0.0.1:8000/get-triage", json={"symptoms": all_symptoms})
        data = res.json()
        st.markdown(f"### {data['severity']}")
        if data.get("condition"):
            st.write(f"**Predicted condition:** {data['condition']}")
        st.write(data.get("explanation", ""))
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Length:", len(content))
