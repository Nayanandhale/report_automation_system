from word2number import w2n

# REQUIRED FIELDS
REQUIRED_FIELDS = {
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
}

#NUMERIC FIELDS
NUMERIC_FIELDS = {
    "Present",
    "Absent",
    "Total Enrolled Candidates"
}

# NUMBER CONVERTER
def convert_to_number(value):
    value = value.strip().lower()
    if value.isdigit():
        return int(value)
    try:
        return w2n.word_to_num(value)
    except:
        return value