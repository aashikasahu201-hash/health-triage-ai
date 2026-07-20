import joblib
from deep_translator import GoogleTranslator

symptom_columns = joblib.load("symptom_columns.pkl")

def match_symptoms(text):
    try:
        text = GoogleTranslator(source="auto", target="en").translate(text)
    except Exception:
        pass

    text = text.lower().replace(",", " ").replace(".", " ")
    matched = []
    for symptom in symptom_columns:
        symptom_words = symptom.replace("_", " ")
        if symptom_words in text:
            matched.append(symptom)
    return matched
