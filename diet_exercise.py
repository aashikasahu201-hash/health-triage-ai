DIET_EXERCISE_MAP = {
    "Diabetes": {
        "diet": "Focus on whole grains, vegetables, and lean protein. Limit refined sugar and processed carbs.",
        "exercise": "Aim for 30 minutes of moderate activity (walking, cycling) most days, as advised by your doctor."
    },
    "Hypertension": {
        "diet": "Reduce salt intake, favor fruits, vegetables, and low-fat dairy (DASH-style eating).",
        "exercise": "Light to moderate cardio (walking, swimming) most days; avoid heavy straining exercise without medical clearance."
    },
    "Bronchial Asthma": {
        "diet": "Stay hydrated; some find anti-inflammatory foods (fruits, vegetables, omega-3s) helpful.",
        "exercise": "Low-intensity activities like walking or swimming; always keep prescribed inhalers accessible."
    },
    "Fungal infection": {
        "diet": "Reduce sugar intake, which can encourage fungal growth. Stay hydrated.",
        "exercise": "Regular activity is fine; keep skin dry and clean, especially after sweating."
    },
    "GERD": {
        "diet": "Avoid spicy, fatty, or acidic foods; eat smaller meals; avoid lying down right after eating.",
        "exercise": "Light activity after meals (like walking) can help; avoid intense exercise right after eating."
    },
    "Migraine": {
        "diet": "Stay hydrated, maintain regular meals, and identify/avoid personal trigger foods (common ones: caffeine, alcohol).",
        "exercise": "Regular, moderate exercise can reduce frequency; avoid overly intense workouts during an active migraine."
    },
    "Osteoarthristis": {
        "diet": "Anti-inflammatory foods (fruits, vegetables, fish) may help; maintain a healthy weight to reduce joint stress.",
        "exercise": "Low-impact activities like swimming or cycling; consult a physiotherapist for joint-specific guidance."
    },
    "Arthritis": {
        "diet": "Anti-inflammatory diet with omega-3s (fish, flaxseed); limit processed foods.",
        "exercise": "Gentle range-of-motion and low-impact exercises; avoid high-impact activity during flare-ups."
    },
}

DEFAULT_TIP = {
    "diet": "Maintain a balanced diet rich in fruits, vegetables, and whole grains, and stay well hydrated.",
    "exercise": "Aim for regular, moderate physical activity as tolerated, and consult your doctor for condition-specific guidance."
}

def get_diet_exercise(condition):
    return DIET_EXERCISE_MAP.get(condition, DEFAULT_TIP)
