import os
import pandas as pd

def is_duplicate(data, file_name="ngo_reports.xlsx"):
    """
    Checks if a report is already recorded based on matching Batch ID
    and Training Date (or Day).
    """
    if not os.path.exists(file_name):
        return False

    try:
        df = pd.read_excel(file_name)
        if df.empty:
            return False

        batch_id = str(data.get("Batch ID", "")).strip().lower()
        training_date = str(data.get("Training Date", "")).strip().lower()
        day = str(data.get("Day", "")).strip().lower()

        if not batch_id or batch_id in ["unknown_batch", "none", ""]:
            return False

        for _, row in df.iterrows():
            row_batch = str(row.get("Batch ID", "")).strip().lower()
            row_date = str(row.get("Training Date", "")).strip().lower()
            row_day = str(row.get("Day", "")).strip().lower()

            if row_batch == batch_id:
                # Same Batch ID and same Training Date
                if training_date and row_date and row_date == training_date:
                    return True
                # Or same Batch ID and same Day number
                if day and row_day and row_day == day:
                    return True

        return False
    except Exception as e:
        print(f"Duplicate check error: {e}")
        return False

def check_duplicate_details(data, file_name="ngo_reports.xlsx"):
    """
    Returns (is_duplicate: bool, detail_message: str)
    """
    if not os.path.exists(file_name):
        return False, ""

    try:
        df = pd.read_excel(file_name)
        if df.empty:
            return False, ""

        batch_id = str(data.get("Batch ID", "")).strip()
        training_date = str(data.get("Training Date", "")).strip()
        day = str(data.get("Day", "")).strip()

        if not batch_id:
            return False, ""

        for _, row in df.iterrows():
            row_batch = str(row.get("Batch ID", "")).strip()
            row_date = str(row.get("Training Date", "")).strip()
            row_day = str(row.get("Day", "")).strip()

            if row_batch.lower() == batch_id.lower():
                if training_date and row_date and row_date.lower() == training_date.lower():
                    return True, f"Duplicate entry found: Batch '{batch_id}' already has a report for Date {training_date}."
                if day and row_day and row_day.lower() == day.lower():
                    return True, f"Duplicate entry found: Batch '{batch_id}' already has a report for Day {day}."

        return False, ""
    except Exception as e:
        return False, f"Check error: {e}"
