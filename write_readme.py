content = """# \U0001FA7A Health Triage Assistant

An AI-assisted symptom triage web app built as a first end-to-end machine learning project. Users describe symptoms by voice, text, or manual selection, and the app returns an urgency level, a likely condition, and general guidance - clearly framed as triage assistance, not a medical diagnosis.

## \U0001F4F8 Screenshots

| Symptom Checker | Emergency Detection |
|---|---|
| ![Home](screenshots/home.png) | ![Emergency](screenshots/emergency.png) |

| Diagnosis Details | Dashboard |
|---|---|
| ![Diagnosis](screenshots/diagnosis.png) | ![Dashboard](screenshots/dashboard.png) |

## \u2728 Features

- \U0001F3A4 Multi-modal symptom input - speak (Whisper, auto-translated), type (any language), or manually select from 131 symptoms
- \U0001F6A8 Safety-first triage - a deterministic rules layer catches red-flag symptoms and immediately recommends emergency care, bypassing the ML model entirely
- \U0001F52C ML-based prediction - XGBoost classifier returning the top 3 most likely conditions with confidence scores
- \U0001F916 AI explanations - Gemini-generated, plain-language explanations with a rule-based fallback
- \U0001F4AC Health chatbot - general health Q&A powered by Gemini
- \U0001FA7A Diagnosis details - description, precautions, recommended specialist, diet/exercise guidance
- \U0001F310 Multi-language support - 19+ languages
- \U0001F3E5 Nearby hospitals - Google Places-powered search
- \u2696\uFE0F BMI calculator, \U0001F4CA dashboard, \U0001F4DD patient history, \U0001F4C4 PDF report export
- \U0001F319 Dark/light mode

## \U0001F9E9 Architecture

Input (voice/text/manual) -> Rules layer (red flag check) -> if emergency, stop here
If no red flag -> ML layer (XGBoost) -> Top 3 predicted conditions with confidence
-> Explanation layer (Gemini) -> Diagnosis page (description, precautions, specialist, diet/exercise)

Backend: FastAPI serving a single /get-triage endpoint
Frontend: Streamlit, multi-page app with a shared sidebar

## \U0001F6E0\uFE0F Tech stack

Python, FastAPI, XGBoost, scikit-learn, Streamlit, OpenAI Whisper, Google Gemini API, Google Places API, deep-translator, fpdf2

## \U0001F5C3\uFE0F Dataset

Disease-Symptom Prediction dataset (Kaggle).

Data quality note: the original dataset (4920 rows) contained approximately 4600 duplicate rows, producing a suspicious 100% accuracy before cleaning. After deduplication (304 unique rows), the model achieved a more honest 92% accuracy.

## \U0001F4CA Model details

- Algorithm: XGBoost
- Symptoms recognized: 131
- Conditions covered: 41
- Test accuracy: 92% (post-deduplication)

## \u2699\uFE0F Setup

python -m venv venv
venv\\Scripts\\Activate.ps1
pip install -r requirements.txt

Create a .env file with:
GEMINI_API_KEY=your_key_here
GOOGLE_PLACES_API_KEY=your_key_here

Run:
uvicorn main:app --reload
streamlit run app.py

## \u26A0\uFE0F Limitations

- Triage guidance only - not a medical diagnosis
- Trained on limited public data, not clinical records
- Keyword-based symptom matching may miss unusual phrasing
- Always consult a qualified healthcare professional

## \U0001F4DD Disclaimer

Educational/portfolio demonstration of an ML + LLM application pipeline. Not certified for real-world medical use.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Length:", len(content))
