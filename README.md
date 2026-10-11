# 🌱 Report Automation & Tracker System

### *Unnatva Foundation · Nashik Center*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Excel](https://img.shields.io/badge/Storage-Excel%20%2B%20SQLite-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://pandas.pydata.org/)
[![OCR](https://img.shields.io/badge/OCR-WinOCR%20%2B%20Tesseract-F05032?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/tesseract-ocr/tesseract)
[![NGO](https://img.shields.io/badge/Built%20For-Unnatva%20Foundation-005A36?style=for-the-badge)](https://unnatva.org)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)](https://github.com)

> **Eliminating repetitive manual data entry for NGO field trainers.**

[🚀 Quick Start](#-quick-start-guide) · [✨ Features](#-features--capabilities)
---

## 📌 The Problem We Solved

Field trainers at **Unnatva Foundation** conduct daily skill-development sessions across multiple districts. Every day, they send session reports via **WhatsApp** — as text messages or photo screenshots. Previously, a staff member had to:

1. Read each WhatsApp message manually
2. Re-type all data into a tracking spreadsheet
3. Cross-check attendance math by hand
4. Detect and resolve duplicate entries manually

This and introduced frequent errors and inconsistencies, takes time.

**This system automates the entire pipeline.** ✅

---

## ✨ Features & Capabilities

| Feature | Description | Status |
|:---|:---|:---:|
| 📸 **Screenshot OCR** | Native Windows OCR + Tesseract fallback extracts text from photos | ✅ Active |
| 📝 **Text Parser** | 14-field intelligent extraction from WhatsApp-style freeform text | ✅ Active |
| 🔢 **Attendance Validator** | Auto-checks `Present + Absent == Total Enrolled` with inline alert | ✅ Active |
| 🔁 **Duplicate Detector** | Flags if same Batch ID + Training Date already recorded | ✅ Active |
| ✏️ **Human Review Form** | Staff can edit any extracted field before saving | ✅ Active |
| 💾 **Excel Master Tracker** | Zero-config local database written to `ngo_reports.xlsx` | ✅ Active |
| 📊 **Analytics Dashboard** | Live KPIs — attendance rates, location coverage, course charts | ✅ Active |
| 📜 **Master History** | Full-text search, multi-filter, 1-click CSV + Excel export | ✅ Active |
| 🌐 **Google Sheets Sync** | Optional mirror to Google Sheets if `credentials.json` is configured | ⚙️ Optional |
| 🔐 **Secure Auth** | bcrypt-hashed passwords + admin approval workflow | ✅ Active |
| 🌍 **Multilingual Text** | Hindi/Marathi terms in direct text input (Devanagari numerals supported) | ✅ Active |

---

## 📂 Project Structure

```
report_automation_system/
│
├── app.py                      ← Main Streamlit entry point & router
├── excel_handler.py            ← Master Excel storage & schema
├── requirements.txt            ← All Python dependencies
├── Dockerfile                  ← Container deployment config
├── Procfile                    ← PaaS (Render/Heroku) config
├── run_app.bat                 ← 1-Click Windows launcher
│
├── assets/
│   ├── ngo_logo.png            ← Official Unnatva "U" logo
│
├── components/                 ← Streamlit UI modules
│   ├── auth.py                 ← Login portal (Sign In / Create Account)
│   ├── upload.py               ← Ingestion, OCR, review form & save
│   ├── dashboard.py            ← Analytics KPIs + distribution charts
│   ├── history.py              ← Searchable table + export tools
│   ├── design.py               ← Top header + sidebar layout
│   └── styles.py               ← Unnatva CSS design system
│
├── extractor/                  ← Parsing & intelligence core
│   ├── main_extractor.py       ← Orchestrator
│   ├── basic_extractor.py      ← Universal key-value pattern parser
│   ├── attendance_extractor.py ← Attendance math validator
│   ├── duplicate_extractor.py  ← Duplicate detection engine
│   ├── cleaner.py              ← RapidFuzz typo correction
│   ├── patterns.py             ← English + bilingual field synonyms
│   └── validator.py            ← Numeric conversions & field checks
│
├── sheets/                     ← Google Sheets integration (Optional)
│   ├── sheets_handler.py       ← Resilient Google Sheets sync
│   └── admin_fetcher.py        ← Admin fetch utilities
│
└── utils/
    ├── db_handler.py           ← SQLite auth & admin approvals
    ├── ocr_handler.py          ← WinOCR + Tesseract dual-engine OCR
    └── translator_handler.py   ← Regional translation fallback
```

---

## 🚀 Quick Start Guide

### Prerequisites

- **Python 3.10+** — [Download here](https://www.python.org/downloads/)
- **Windows 10/11** recommended (for native WinOCR) — or any OS with Tesseract installed

---

### ▶ Option 1 — One-Click Windows Launch *(Recommended)*

```
Double-click:  run_app.bat
```

The launcher auto-installs all dependencies and opens the app in your browser automatically.

---

### ▶ Option 2 — Manual Terminal Launch

```powershell
Navigate to project folder

# Install dependencies (first time only)
py -m pip install -r requirements.txt

# Start the application
py -m streamlit run app.py
```

Open your browser at: **http://localhost:8501**

---

### 🔑 Default Login Credentials

| Field | Value |
|:---|:---|
| **Username** | `admin` |
| **Password** | `admin123` |

> Change your password anytime using the **"🔑 Change Password"** expander in the sidebar.

## 🌐 Google Sheets Sync *(Optional)*

By default the system operates entirely offline using `ngo_reports.xlsx`. To optionally also mirror data to Google Sheets:

1. Create a **Google Cloud Service Account** and download the JSON key file
2. Save as **`credentials.json`** in the project root (see [`credentials.example.json`](credentials.example.json))
3. Create a Google Sheet named **`NGO Daily Reports`**
4. Share the sheet with the service account email address
5. Restart the app — sync activates automatically on save

---

## ⚙️ Key Configuration Files

| File | Purpose |
|:---|:---|
| `requirements.txt` | Python package dependencies |
| `.streamlit/config.toml` | Streamlit server + theme settings |
| `Dockerfile` | Docker containerization |
| `Procfile` | PaaS deployment command |
| `run_app.bat` | Windows one-click launcher |
| `credentials.json` | *(Optional)* Google Sheets service account key |
| `database.db` | SQLite auth database (auto-created on first run) |
| `ngo_reports.xlsx` | Master Excel tracker (auto-created on first save) |

---

## 🔐 User Management

| Role | Capabilities |
|:---|:---|
| **Admin** | Full access + approve/reject new staff registrations |
| **Staff** | Upload reports, view history & analytics, export data |

New staff register via the **"📝 Create Account"** tab on the login page. Accounts require admin approval before they can log in.

---

## 📄 License & Attribution

Developed for **Unnatva Foundation, Nashik** as part of the Social Internship Initiative.
