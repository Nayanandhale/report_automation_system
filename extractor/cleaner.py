import re
from rapidfuzz import process
from extractor.patterns import VALID_TOPIC_WORDS, VALID_FIELDS

def correct_word(word):
    # Strip surrounding punctuation for matching
    cleaned = re.sub(r'^[^\w]+|[^\w]+$', '', word)
    if not cleaned or not re.search(r'[a-zA-Z]', cleaned):
        return word

    match = process.extractOne(
        cleaned.lower(),
        VALID_TOPIC_WORDS
    )

    if match and match[1] >= 80:
        # Preserve original trailing/leading punctuation
        return word.replace(cleaned, match[0])
    return word

def correct_topic_text(text):
    if not text:
        return text
    words = str(text).split()
    corrected_words = []
    for word in words:
        corrected_words.append(correct_word(word))
    return " ".join(corrected_words)

def correct_field_name(field):
    if not field:
        return field
    cleaned = field.strip().lower()
    match = process.extractOne(
        cleaned,
        VALID_FIELDS
    )

    if match and match[1] >= 75:
        return match[0]
    return field