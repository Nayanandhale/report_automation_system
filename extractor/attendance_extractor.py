def validate_attendance(data, remarks):
    if all(k in data for k in [
        "Present",
        "Absent",
        "Total Enrolled Candidates"
    ]):

        if (
            isinstance(data["Present"], int) and isinstance(data["Absent"], int) and isinstance(data["Total Enrolled Candidates"], int) ):

            if (
                data["Present"] + data["Absent"] != data["Total Enrolled Candidates"] ):

                remarks.append("Attendance mismatch detected")

    return remarks