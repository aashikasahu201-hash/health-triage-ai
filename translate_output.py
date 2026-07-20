from deep_translator import GoogleTranslator

def translate_output(text, target_lang):
    if not text or target_lang == "en":
        return text
    try:
        return GoogleTranslator(source="en", target=target_lang).translate(text)
    except Exception:
        return text
