from extractor.basic_extractor import (extract_basic_fields)
from extractor.attendance_extractor import (validate_attendance)
from extractor.validator import (REQUIRED_FIELDS)

def extract_report(report):

    data, remarks = extract_basic_fields(report)

    # REQUIRED FIELD CHECK
    for field in REQUIRED_FIELDS:
        if field not in data:
            remarks.append(f"Missing Field: {field}")

    # ATTENDANCE VALIDATION
    remarks = validate_attendance(data, remarks)

    # FINAL REMARKS
    data["Remarks"] = (" | ".join(remarks) if remarks else "OK")
    return data


