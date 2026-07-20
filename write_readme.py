content = """# Health Triage Assistant

An AI-assisted symptom triage web app built as a first end-to-end machine learning project. Users describe symptoms by voice, text, or manual selection, and the app returns an urgency level, a likely condition, and general guidance - all clearly framed as triage assistance, not a medical diagnosis.

## Features

- Multi-modal symptom input - speak (Whisper, auto-translated to English), type (any language), or manually select from 131 symptoms
- Safety-first triage - a deterministic rules layer checks for red-flag symptoms (chest pain, breathlessness, etc.) and immediately recommends emergency care, bypassing the ML model entirely
- ML-based prediction - an XGBoost classifier trained on a public symptom-disease dataset, returning the top 3 most likely conditions with confidence scores
- AI explanations - Gemini-generated, plain-language explanations of each result (with a rule-based fallback if the API is unavailable)
- Health chatbot - general health Q&A powered by Gemini, with guardrails against diagnosis or dosage advice
- Diagnosis details - condition description, precautions, recommended specialist, and general diet/exercise guidance
- Multi-language support - UI and results available in 19+ languages
- Nearby hospitals - Google Places-powered search for hospitals near a given location
- BMI calculator, session dashboard, patient history, and PDF report export
- Dark/light mode

## Architecture

Input (voice/text/manual) -> Rules layer (red flag check) -> if emergency, stop here
If no red flag -> ML layer (XGBoost) -> Top 3 predicted conditions with confidence
-> Explanation layer (Gemini, with rule-based fallback)
-> Diagnosis page (description, precautions, specialist, diet/exercise)

Backend: FastAPI serving a single /get-triage endpoint
Frontend: Streamlit, multi-page app with a shared sidebar (session stats, language, theme)

## Tech stack

Python, FastAPI, XGBoost, scikit-learn, Streamlit, OpenAI Whisper, Google Gemini API, Google Places API, deep-translator, fpdf2

## Dataset

Disease-Symptom Prediction dataset (Kaggle) - includes symptom-disease mappings, condition descriptions, and precaution lists.

Data quality note: the original dataset (4920 rows) contained approximately 4600 duplicate rows. Training on the raw data produced a suspicious 100% accuracy score - a clear sign of data leakage from duplicates appearing in both train and test splits. After deduplication (down to 304 unique rows), the model achieved a more honest 92% accuracy. This is documented deliberately: recognizing and fixing that leakage was a more valuable exercise than the metric itself.

## Model details

- Algorithm: XGBoost (gradient boosted trees)
- Symptoms recognized: 131
- Conditions covered: 41
- Test accuracy: 92% (post-deduplication)
- Known limitation: with only ~304 unique training rows across 41 classes, several conditions have very few test examples, so per-class reliability varies.

## Setup

python -m venv venv
venv\\Scripts\\Activate.ps1
pip install -r requirements.txt

Create a .env file in the project root with:
GEMINI_API_KEY=your_key_here
GOOGLE_PLACES_API_KEY=your_key_here

Run the backend and frontend in separate terminals:
uvicorn main:app --reload
streamlit run app.py

## Limitations

- This tool provides triage guidance only - it is not a medical diagnosis and should never be treated as one
- Trained on a limited, publicly available dataset, not real clinical records
- Voice/text symptom matching uses keyword matching after translation - may miss unusual phrasing
- Diet, exercise, and specialist recommendations are general wellness information, not personalized medical advice
- Always consult a qualified healthcare professional for actual medical concerns

## Disclaimer

This project is an educational/portfolio demonstration of an ML + LLM application pipeline. It is not certified for real-world medical use.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Length:", len(content))
