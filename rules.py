RED_FLAGS = {
    "chest_pain": "Emergency",
    "breathlessness": "Emergency",
    "slurred_speech": "Emergency",
    "stomach_bleeding": "Emergency",
    "altered_sensorium": "Emergency",
}

def check_red_flags(symptoms):
    for s in symptoms:
        if s in RED_FLAGS:
            return RED_FLAGS[s]
    return None