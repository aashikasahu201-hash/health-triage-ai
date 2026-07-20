import streamlit as st
from deep_translator import GoogleTranslator

TRANSLATIONS = {
    "en": {
        "app_title": "Symptom Checker",
        "app_caption": "AI-assisted triage guidance - not a medical diagnosis.",
        "patient_info": "Patient Information",
        "name": "Name",
        "age": "Age",
        "gender": "Gender",
        "speak_tab": "Speak",
        "type_tab": "Type",
        "select_tab": "Select",
        "describe_placeholder": "Describe how you feel",
        "check_button": "Check Symptoms",
        "results_placeholder": "Results will appear here after you check your symptoms.",
        "download_pdf": "Download PDF Report",
        "top_conditions": "Top possible conditions",
        "name_required": "Please enter the patient's name.",
        "symptom_required": "Please select at least one symptom.",
        "bmi_title": "BMI Calculator",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "calculate_bmi": "Calculate BMI",
        "dashboard_title": "Dashboard",
        "no_data": "No data yet this session.",
        "total_checks": "Total checks",
        "emergency_flags": "Emergency flags",
        "unique_conditions": "Unique conditions",
        "history_title": "Patient History",
        "no_checks": "No checks yet this session.",
        "clear_history": "Clear history",
        "diagnosis_title": "Diagnosis Details",
        "specialist": "Recommended specialist",
        "about_condition": "About this condition",
        "precautions": "Recommended precautions",
        "diet_tips": "General diet guidance",
        "exercise_tips": "General exercise guidance",
    },
    "hi": {
        "app_title": "\u0932\u0915\u094d\u0937\u0923 \u091c\u093e\u0902\u091a\u0915",
        "app_caption": "\u090f\u0906\u0908-\u0938\u0939\u093e\u092f\u0924\u093e \u092a\u094d\u0930\u093e\u092a\u094d\u0924 \u091f\u094d\u0930\u093f\u092f\u093e\u091c \u092e\u093e\u0930\u094d\u0917\u0926\u0930\u094d\u0936\u0928 - \u092f\u0939 \u091a\u093f\u0915\u093f\u0924\u094d\u0938\u093e \u0928\u093f\u0926\u093e\u0928 \u0928\u0939\u0940\u0902 \u0939\u0948\u0964",
        "patient_info": "\u0930\u094b\u0917\u0940 \u0915\u0940 \u091c\u093e\u0928\u0915\u093e\u0930\u0940",
        "name": "\u0928\u093e\u092e",
        "age": "\u0906\u092f\u0941",
        "gender": "\u0932\u093f\u0902\u0917",
        "speak_tab": "\u092c\u094b\u0932\u0947\u0902",
        "type_tab": "\u091f\u093e\u0907\u092a \u0915\u0930\u0947\u0902",
        "select_tab": "\u091a\u0941\u0928\u0947\u0902",
        "describe_placeholder": "\u0906\u092a \u0915\u0948\u0938\u093e \u092e\u0939\u0938\u0942\u0938 \u0915\u0930 \u0930\u0939\u0947 \u0939\u0948\u0902, \u092c\u0924\u093e\u090f\u0902",
        "check_button": "\u0932\u0915\u094d\u0937\u0923 \u091c\u093e\u0902\u091a\u0947\u0902",
        "results_placeholder": "\u091c\u093e\u0902\u091a \u0915\u0947 \u092c\u093e\u0926 \u092a\u0930\u093f\u0923\u093e\u092e \u092f\u0939\u093e\u0902 \u0926\u093f\u0916\u0947\u0902\u0917\u0947\u0964",
        "download_pdf": "\u092a\u0940\u0921\u0940\u090f\u092b \u0930\u093f\u092a\u094b\u0930\u094d\u091f \u0921\u093e\u0909\u0928\u0932\u094b\u0921 \u0915\u0930\u0947\u0902",
        "top_conditions": "\u0938\u0902\u092d\u093e\u0935\u093f\u0924 \u0936\u0940\u0930\u094d\u0937 \u0938\u094d\u0925\u093f\u0924\u093f\u092f\u093e\u0902",
        "name_required": "\u0915\u0943\u092a\u092f\u093e \u0930\u094b\u0917\u0940 \u0915\u093e \u0928\u093e\u092e \u0926\u0930\u094d\u091c \u0915\u0930\u0947\u0902\u0964",
        "symptom_required": "\u0915\u0943\u092a\u092f\u093e \u0915\u092e \u0938\u0947 \u0915\u092e \u090f\u0915 \u0932\u0915\u094d\u0937\u0923 \u091a\u0941\u0928\u0947\u0902\u0964",
        "bmi_title": "\u092c\u0940\u090f\u092e\u0906\u0908 \u0915\u0948\u0932\u094d\u0915\u0941\u0932\u0947\u091f\u0930",
        "weight": "\u0935\u091c\u0928 (\u0915\u093f\u0932\u094b\u0917\u094d\u0930\u093e\u092e)",
        "height": "\u0932\u0902\u092c\u093e\u0908 (\u0938\u0947\u092e\u0940)",
        "calculate_bmi": "\u092c\u0940\u090f\u092e\u0906\u0908 \u0915\u0940 \u0917\u0923\u0928\u093e \u0915\u0930\u0947\u0902",
        "dashboard_title": "\u0921\u0948\u0936\u092c\u094b\u0930\u094d\u0921",
        "no_data": "\u0907\u0938 \u0938\u0924\u094d\u0930 \u092e\u0947\u0902 \u0905\u092d\u0940 \u0924\u0915 \u0915\u094b\u0908 \u0921\u0947\u091f\u093e \u0928\u0939\u0940\u0902\u0964",
        "total_checks": "\u0915\u0941\u0932 \u091c\u093e\u0902\u091a",
        "emergency_flags": "\u0906\u092a\u093e\u0924\u0915\u093e\u0932\u0940\u0928 \u092e\u093e\u092e\u0932\u0947",
        "unique_conditions": "\u0905\u0932\u0917-\u0905\u0932\u0917 \u0938\u094d\u0925\u093f\u0924\u093f\u092f\u093e\u0902",
        "history_title": "\u0930\u094b\u0917\u0940 \u0907\u0924\u093f\u0939\u093e\u0938",
        "no_checks": "\u0907\u0938 \u0938\u0924\u094d\u0930 \u092e\u0947\u0902 \u0905\u092d\u0940 \u0924\u0915 \u0915\u094b\u0908 \u091c\u093e\u0902\u091a \u0928\u0939\u0940\u0902\u0964",
        "clear_history": "\u0907\u0924\u093f\u0939\u093e\u0938 \u0938\u093e\u092b \u0915\u0930\u0947\u0902",
        "diagnosis_title": "\u0928\u093f\u0926\u093e\u0928 \u0935\u093f\u0935\u0930\u0923",
        "specialist": "\u0905\u0928\u0941\u0936\u0902\u0938\u093f\u0924 \u0935\u093f\u0936\u0947\u0937\u091c\u094d\u091e",
        "about_condition": "\u0907\u0938 \u0938\u094d\u0925\u093f\u0924\u093f \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902",
        "precautions": "\u0905\u0928\u0941\u0936\u0902\u0938\u093f\u0924 \u0938\u093e\u0935\u0927\u093e\u0928\u093f\u092f\u093e\u0902",
        "diet_tips": "\u0938\u093e\u092e\u093e\u0928\u094d\u092f \u0906\u0939\u093e\u0930 \u092e\u093e\u0930\u094d\u0917\u0926\u0930\u094d\u0936\u0928",
        "exercise_tips": "\u0938\u093e\u092e\u093e\u0928\u094d\u092f \u0935\u094d\u092f\u093e\u092f\u093e\u092e \u092e\u093e\u0930\u094d\u0917\u0926\u0930\u094d\u0936\u0928",
    },
}

@st.cache_data(show_spinner=False)
def _live_translate(text, lang):
    try:
        return GoogleTranslator(source="en", target=lang).translate(text)
    except Exception:
        return text

def t(key, lang="en"):
    if lang in TRANSLATIONS and key in TRANSLATIONS[lang]:
        return TRANSLATIONS[lang][key]

    english_text = TRANSLATIONS["en"].get(key, key)
    if lang == "en":
        return english_text

    return _live_translate(english_text, lang)
