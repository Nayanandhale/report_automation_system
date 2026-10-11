from extractor.validator import convert_to_number

def validate_attendance(data, remarks=None):
    if remarks is None:
        remarks = []

    present = convert_to_number(data.get("Present"))
    absent = convert_to_number(data.get("Absent"))
    total = convert_to_number(data.get("Total Enrolled Candidates"))

    if isinstance(present, int) and isinstance(absent, int) and isinstance(total, int):
        data["Present"] = present
        data["Absent"] = absent
        data["Total Enrolled Candidates"] = total

        if present + absent != total:
            remarks.append(f"Attendance mismatch detected (Present {present} + Absent {absent} != Total {total})")

    return remarks