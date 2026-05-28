from deep_translator import GoogleTranslator
import re
def contains_marathi(text):
    return bool(
        re.search(r'[\u0900-\u097F]', text)
    )
def translate_text(text):
    if not text:
        return text

    # translate only if Marathi/Hindi exists
    if contains_marathi(text):
        try:
            translated = GoogleTranslator(
                source='auto',
                target='en'
            ).translate(text)

            return translated
        except:
            return text
    return text
def translate_report_data(data):
    fields_to_translate = [
        "Block Name",
        "Training Location",
        "Course Name",
        "Topic",
        "Trainer Name"
    ]

    for field in fields_to_translate:
        if field in data:
            data[field] = translate_text(
                str(data[field])
            )
    return data