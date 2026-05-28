import re
from extractor.patterns import (FIELD_MAPPING)
from extractor.cleaner import (correct_field_name)
from extractor.validator import (NUMERIC_FIELDS,convert_to_number)
def extract_basic_fields(report):

    data = {}

    remarks = []

    for line in report.split("\n"):
        line = line.strip()
        if not line:
            continue

        # universal separator split
        parts = re.split(r'\s*[:=-]+\s*', line, maxsplit=1)

        if len(parts) < 2:
            continue

        raw_key = parts[0].strip().lower()
        raw_key = correct_field_name(raw_key)
        value = parts[1].strip()

        # clean english special chars only
        cleaned_key = re.sub(
            r'[^a-zA-Z\u0900-\u097F ]', '', raw_key)

        if cleaned_key not in FIELD_MAPPING:
            continue
        else:
            key = FIELD_MAPPING[cleaned_key]

        # numeric conversion
        if key in NUMERIC_FIELDS:
            converted = convert_to_number(value)
            if isinstance(converted, int):
                value = converted
            else:
                remarks.append(f"Invalid number in {key}")

        data[key] = value

    return data, remarks