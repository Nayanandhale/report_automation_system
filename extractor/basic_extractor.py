import re
from extractor.patterns import FIELD_MAPPING
from extractor.cleaner import correct_field_name, correct_topic_text
from extractor.validator import NUMERIC_FIELDS, convert_to_number

def extract_basic_fields(report):
    data = {}
    remarks = []

    for line in str(report).split("\n"):
        line = line.strip()
        if not line:
            continue

        # universal separator split (matches ':', ':-', '=', '-', or tab)
        parts = re.split(r'\s*[:=\-]+\s*', line, maxsplit=1)

        if len(parts) < 2:
            continue

        raw_key = parts[0].strip().lower()
        # Remove extra punctuation from key before lookup
        clean_raw_key = re.sub(r'[^a-zA-Z\u0900-\u097F ]', '', raw_key).strip()

        # Check direct mapping or fuzzy corrected mapping
        canonical_pattern = correct_field_name(clean_raw_key)
        if canonical_pattern in FIELD_MAPPING:
            key = FIELD_MAPPING[canonical_pattern]
        elif clean_raw_key in FIELD_MAPPING:
            key = FIELD_MAPPING[clean_raw_key]
        else:
            continue

        value = parts[1].strip()

        # Numeric conversion for counts and numbers
        if key in NUMERIC_FIELDS:
            converted = convert_to_number(value)
            if isinstance(converted, int):
                value = converted
            else:
                remarks.append(f"Invalid number in {key}")

        # Topic spelling correction
        if key == "Topic":
            value = correct_topic_text(value)

        data[key] = value

    return data, remarks