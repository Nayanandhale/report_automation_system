import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES)
client = gspread.authorize(CREDS)

SPREADSHEET_NAME = "NGO Daily Reports"
spreadsheet = client.open(SPREADSHEET_NAME)

def save_to_google_sheets(data):
    try:
        course_name = data.get(
            "Course Name",
            "General")

        batch_id = data.get(
            "Batch ID",
            "Unknown_Batch")

        sheet_name = f"{course_name}_{batch_id}"
        sheet_name = (
            sheet_name
            .strip()
            .replace(" ", "_")
            .replace("/", "_") )

        headers = [
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
            "Trainer Name",
            "Remarks"
        ]
        try:
            worksheet = spreadsheet.worksheet(
                sheet_name)
        except:
            worksheet = spreadsheet.add_worksheet(
                title=sheet_name,
                rows="1000",
                cols="50"
            )
            worksheet.append_row(headers)
        row = []
        for header in headers:
            value = data.get(header, "")
            row.append(value)
        worksheet.append_row(row)
        print(f"Data saved to sheet: {sheet_name}")
    except Exception as e:
        print(f"Google Sheets Error: {e}")