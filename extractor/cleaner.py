import re
from attrs import field
from rapidfuzz import process
from extractor.patterns import VALID_TOPIC_WORDS
from extractor.patterns import VALID_FIELDS

def correct_word(word):
    # skip Marathi words
    if not re.search(r'[a-zA-Z]', word):
        return word

    match = process.extractOne(
        word.lower(),
        VALID_TOPIC_WORDS
    )

    if match and match[1] >= 80:
        return match[0]
    return word

def correct_topic_text(text):

    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = correct_word(word)
        corrected_words.append(corrected_word)
    return " ".join(corrected_words)

def correct_field_name(field):
    match = process.extractOne(
        field,
        VALID_FIELDS
    )

    if match and match[1] >= 75:
        return match[0]
    return field