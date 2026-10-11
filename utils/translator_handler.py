import re
from deep_translator import GoogleTranslator

def contains_devanagari(text):
    """Checks if string contains Devanagari (Hindi / Marathi) script."""
    return bool(re.search(r'[\u0900-\u097F]', str(text)))

def translate_text(text):
    if not text:
        return text

    text_str = str(text).strip()
    if contains_devanagari(text_str):
        try:
            translated = GoogleTranslator(
                source='auto',
                target='en'
            ).translate(text_str)
            return translated if translated else text_str
        except Exception:
            # If network error or rate limit, preserve original text safely
            return text_str
    return text_str

def translate_report_data(data):
    """
    Translates regional language fields to English if network translator is available.
    Preserves original data safely upon network failure.
    """
    fields_to_translate = [
        "Block Name",
        "Training Location",
        "Course Name",
        "Topic",
        "Trainer Name"
    ]

    translated_data = dict(data)
    for field in fields_to_translate:
        if field in translated_data and translated_data[field]:
            translated_data[field] = translate_text(translated_data[field])

    return translated_data