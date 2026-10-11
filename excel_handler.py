import pandas as pd
import os

FILE_NAME = "ngo_reports.xlsx"

STANDARD_COLUMNS = [
    "Batch Start Date",
    "Training Date",
    "Timing",
    "Day",
    "Block Name",
    "Training Location",
    "Course Name",
    "Batch ID",
    "Total Enrolled Candidates",
    "Present",
    "Absent",
    "Topic",
    "Trainer Name",
    "Remarks"
]

def save_to_excel(data, file_name=FILE_NAME):
    """
    Appends report data to the Excel tracker with standardized column ordering.
    """
    new_df = pd.DataFrame([data])

    if os.path.exists(file_name):
        try:
            old_df = pd.read_excel(file_name)
            updated_df = pd.concat([old_df, new_df], ignore_index=True)
        except Exception:
            updated_df = new_df
    else:
        updated_df = new_df

    # Ensure all standard columns exist in proper order
    for col in STANDARD_COLUMNS:
        if col not in updated_df.columns:
            updated_df[col] = ""

    ordered_cols = [c for c in STANDARD_COLUMNS if c in updated_df.columns]
    extra_cols = [c for c in updated_df.columns if c not in STANDARD_COLUMNS]
    final_df = updated_df[ordered_cols + extra_cols]

    final_df.to_excel(file_name, index=False)
    return True
