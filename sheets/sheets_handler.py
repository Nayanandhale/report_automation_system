import os
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

DEFAULT_CREDS_FILE = "credentials.json"
DEFAULT_SPREADSHEET_NAME = "NGO Daily Reports"

HEADERS = [
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

def is_google_sheets_configured(creds_file=DEFAULT_CREDS_FILE):
    """Checks if the service account credentials file exists and is non-empty."""
    return os.path.exists(creds_file) and os.path.getsize(creds_file) > 10

def get_client(creds_file=DEFAULT_CREDS_FILE):
    """Returns an authorized gspread client if credentials exist."""
    if not is_google_sheets_configured(creds_file):
        return None
    creds = Credentials.from_service_account_file(creds_file, scopes=SCOPES)
    return gspread.authorize(creds)

def save_to_google_sheets(data, creds_file=DEFAULT_CREDS_FILE, spreadsheet_name=DEFAULT_SPREADSHEET_NAME):
    """
    Saves a report row to Google Sheets.
    Creates the worksheet tab if it doesn't exist yet.
    Returns (success: bool, message: str).
    """
    if not is_google_sheets_configured(creds_file):
        return False, "Google Sheets sync skipped (credentials.json not found). Saved locally to Excel."

    try:
        client = get_client(creds_file)
        if not client:
            return False, "Could not authorize Google Sheets client."

        spreadsheet = client.open(spreadsheet_name)

        course_name = data.get("Course Name", "General")
        batch_id = data.get("Batch ID", "Batch")

        # Sanitize worksheet tab name (max 100 chars, no illegal characters)
        raw_sheet_name = f"{course_name}_{batch_id}"
        sheet_name = (
            raw_sheet_name
            .strip()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace("?", "")
            .replace("*", "")
            .replace(":", "_")
            .replace("[", "")
            .replace("]", "")
        )[:100]

        try:
            worksheet = spreadsheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(
                title=sheet_name,
                rows="500",
                cols="20"
            )
            worksheet.append_row(HEADERS)
        except Exception:
            # Fallback to first worksheet if creation/lookup errors
            worksheet = spreadsheet.sheet1

        row = [data.get(header, "") for header in HEADERS]
        worksheet.append_row(row)
        return True, f"Report successfully synced to Google Sheet '{spreadsheet_name}' (tab: {sheet_name})."

    except Exception as e:
        error_msg = str(e)
        return False, f"Google Sheets sync notice: {error_msg}"
