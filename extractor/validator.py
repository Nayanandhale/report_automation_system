import re
from word2number import w2n

# REQUIRED FIELDS FOR COMPLETE REPORT
REQUIRED_FIELDS = [
    "Batch Start Date",
    "Training Date",
    "Block Name",
    "Training Location",
    "Course Name",
    "Batch ID",
    "Total Enrolled Candidates",
    "Present",
    "Absent",
    "Topic",
    "Trainer Name"
]

# NUMERIC FIELDS
NUMERIC_FIELDS = {
    "Present",
    "Absent",
    "Total Enrolled Candidates",
    "Day"
}

# DEVANAGARI TO ARABIC DIGITS MAP
DEVANAGARI_DIGITS = str.maketrans('०१२३४५६७८९', '0123456789')

# NUMBER CONVERTER
def convert_to_number(value):
    if value is None:
        return value
    if isinstance(value, int):
        return value

    s = str(value).strip().translate(DEVANAGARI_DIGITS)
    if s.isdigit():
        return int(s)

    # Check for embedded integer like "18 students" or "Day 16"
    match = re.search(r'\b\d+\b', s)
    if match:
        return int(match.group())

    try:
        return w2n.word_to_num(s.lower())
    except Exception:
        return value