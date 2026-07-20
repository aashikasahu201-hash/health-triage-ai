import joblib
from rules import check_red_flags
from explain import explain_result

model = joblib.load("model.pkl")
symptom_columns = joblib.load("symptom_columns.pkl")
le = joblib.load("label_encoder.pkl")

def get_triage(symptoms):
    flag = check_red_flags(symptoms)
    if flag:
        result = {"severity": flag, "condition": None, "action": "Seek emergency care immediately", "top_predictions": []}
        result["explanation"] = explain_result(result)
        return result

    input_vector = [[1 if col in symptoms else 0 for col in symptom_columns]]
    probabilities = model.predict_proba(input_vector)[0]

    top_indices = probabilities.argsort()[-3:][::-1]
    top_predictions = [
        {"condition": le.inverse_transform([idx])[0], "confidence": round(float(probabilities[idx]), 2)}
        for idx in top_indices
    ]

    best = top_predictions[0]
    severity = "See doctor soon" if best["confidence"] > 0.6 else "Self-care with monitoring"

    result = {
        "severity": severity,
        "condition": best["condition"],
        "confidence": best["confidence"],
        "top_predictions": top_predictions,
    }
    result["explanation"] = explain_result(result)
    return result
