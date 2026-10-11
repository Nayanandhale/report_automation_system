from extractor.basic_extractor import extract_basic_fields
from extractor.attendance_extractor import validate_attendance
from extractor.validator import REQUIRED_FIELDS
from extractor.cleaner import correct_topic_text

def extract_report(report):
    """
    Parses unstructured / semi-structured daily training reports.
    Extracts canonical fields, validates attendance, and computes status remarks.
    """
    data, remarks = extract_basic_fields(report)

    # Clean topic text if present
    if "Topic" in data and data["Topic"]:
        data["Topic"] = correct_topic_text(data["Topic"])

    # Required field verification
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] is None or str(data[field]).strip() == "":
            remarks.append(f"Missing Field: {field}")

    # Attendance consistency check (Present + Absent == Total)
    remarks = validate_attendance(data, remarks)

    # Set composite Remarks
    data["Remarks"] = " | ".join(remarks) if remarks else "OK"
    return data
