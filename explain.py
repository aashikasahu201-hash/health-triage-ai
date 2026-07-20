import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = None
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

def rule_based_explanation(result):
    severity = result["severity"]
    condition = result.get("condition")
    confidence = result.get("confidence")

    if severity == "Emergency":
        return (
            "Your symptoms may indicate a serious condition that needs immediate attention. "
            "Please seek emergency care right away. This is not a diagnosis - consult a doctor."
        )

    confidence_pct = int(confidence * 100) if confidence else "unknown"
    text = f"Based on the symptoms you entered, the system's best guess is '{condition}' with {confidence_pct}% confidence. "
    if severity == "See doctor soon":
        text += "It's recommended you see a doctor soon to confirm this and get proper treatment. "
    else:
        text += "This looks manageable with self-care, but monitor your symptoms closely. "
    text += "This is not a diagnosis - consult a doctor for confirmation."
    return text

def explain_result(result):
    if not model:
        return rule_based_explanation(result)

    try:
        prompt = (
            "You are a calm, clear health triage assistant. A user reported symptoms and got this result: "
            f"severity={result['severity']}, condition={result.get('condition')}, "
            f"confidence={result.get('confidence')}. "
            "Write a short, plain-language, reassuring explanation (3-4 sentences) of what this means. "
            "Never invent new conditions or symptoms not given. Always end with a reminder that this is not "
            "a medical diagnosis and to consult a doctor."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return rule_based_explanation(result)
