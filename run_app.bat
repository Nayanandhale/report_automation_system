@echo off
title Unnatva Foundation - Report Automation System
cd /d "%~dp0"
echo =======================================================
echo Starting Unnatva Foundation Report Automation System...
echo =======================================================
echo Checking Python environment...
py -m streamlit run app.py
if errorlevel 1 (
    echo.
    echo Trying python command directly...
    python -m streamlit run app.py
)
pause
