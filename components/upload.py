import streamlit as st
import pandas as pd
from utils.ocr_handler import extract_text_from_image
from extractor.main_extractor import extract_report
from excel_handler import save_to_excel
from sheets.sheets_handler import save_to_google_sheets, is_google_sheets_configured
from extractor.duplicate_extractor import check_duplicate_details

def show_upload():
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #DCE7E0; border-radius:14px; padding:20px; margin-bottom:20px;">
        <h3 style="color:#005A36; margin:0 0 6px 0; font-size:18px; font-weight:700;">
            📤 Ingest & Process Daily Training Report
        </h3>
        <p style="color:#52635B; margin:0; font-size:13px;">
            Upload a training report screenshot or paste text. The system automatically extracts attributes, verifies attendance, and records data in the Excel master database.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if "raw_report_textarea" not in st.session_state:
        st.session_state["raw_report_textarea"] = ""

    col_upload, col_text = st.columns([1, 1])

    with col_upload:
        st.markdown("##### 📸 Upload Screenshot / Photo")
        uploaded_image = st.file_uploader(
            "Upload image (PNG, JPG, JPEG)",
            type=["png", "jpg", "jpeg"],
            key="report_image_uploader"
        )

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Report Screenshot", width=260)
            if st.button("🔍 Extract Text from Image (OCR)", key="btn_run_ocr", use_container_width=True):
                with st.spinner("Extracting text from image..."):
                    extracted_text = extract_text_from_image(uploaded_image)
                    if extracted_text and not extracted_text.startswith("[Error"):
                        st.session_state["raw_report_textarea"] = extracted_text
                        st.session_state["parsed_data"] = extract_report(extracted_text)
                        st.success("✅ Text extracted from screenshot successfully!")
                        st.rerun()
                    else:
                        st.error(extracted_text)

    with col_text:
        st.markdown("##### 📝 Report Text Editor")
        report_text = st.text_area(
            "Raw Report Text:",
            value=st.session_state.get("raw_report_textarea", ""),
            height=260,
            placeholder="Paste raw WhatsApp message or report text here...",
            key="raw_report_textarea"
        )

        parse_btn = st.button("⚡ Extract & Review Fields", key="btn_parse_text", use_container_width=True)
        if parse_btn:
            if not report_text.strip():
                st.warning("Please paste report text or upload an image first.")
            else:
                with st.spinner("Extracting fields..."):
                    st.session_state["parsed_data"] = extract_report(report_text)
                    st.rerun()

    # REVIEW & EDIT FORM
    if "parsed_data" in st.session_state and st.session_state["parsed_data"]:
        extracted = st.session_state["parsed_data"]
        st.markdown("---")
        st.markdown("#### 📋 Review & Confirm Structured Fields")

        # Attendance Check
        present = extracted.get("Present", 0)
        absent = extracted.get("Absent", 0)
        total = extracted.get("Total Enrolled Candidates", 0)
        is_num = isinstance(present, int) and isinstance(absent, int) and isinstance(total, int)

        if is_num and total > 0:
            if present + absent == total:
                st.success(f"✅ **Attendance Verified**: Present ({present}) + Absent ({absent}) = Total ({total})")
            else:
                st.warning(f"⚠️ **Attendance Mismatch**: Present ({present}) + Absent ({absent}) = {present + absent}, which does NOT match Total Enrolled ({total})!")

        # Duplicate Check
        is_dup, dup_msg = check_duplicate_details(extracted)
        if is_dup:
            st.warning(f"⚠️ **Duplicate Warning**: {dup_msg}")

        # Form
        with st.form("review_report_form"):
            form_col1, form_col2, form_col3 = st.columns(3)

            with form_col1:
                st.markdown("###### 📚 Course & Batch")
                edit_course = st.text_input("Course Name", value=str(extracted.get("Course Name", "")))
                edit_batch_id = st.text_input("Batch ID", value=str(extracted.get("Batch ID", "")))
                edit_start_date = st.text_input("Batch Start Date", value=str(extracted.get("Batch Start Date", "")))
                edit_training_date = st.text_input("Training Date", value=str(extracted.get("Training Date", "")))

            with form_col2:
                st.markdown("###### 📍 Location & Schedule")
                edit_block = st.text_input("Block Name", value=str(extracted.get("Block Name", "")))
                edit_location = st.text_input("Training Location", value=str(extracted.get("Training Location", "")))
                edit_timing = st.text_input("Timing", value=str(extracted.get("Timing", "")))
                edit_day = st.text_input("Day", value=str(extracted.get("Day", "")))

            with form_col3:
                st.markdown("###### 👥 Attendance & Trainer")
                edit_total = st.number_input("Total Enrolled", min_value=0, max_value=200, value=int(total) if (is_num and total > 0) else int(present + absent))
                edit_present = st.number_input("Present", min_value=0, max_value=200, value=int(present) if isinstance(present, int) else 0)
                edit_absent = st.number_input("Absent", min_value=0, max_value=200, value=int(absent) if isinstance(absent, int) else 0)
                edit_trainer = st.text_input("Trainer Name", value=str(extracted.get("Trainer Name", "")))

            edit_topic = st.text_area("Topic Covered", value=str(extracted.get("Topic", "")), height=70)

            # Auto calculate remark
            calc_remarks = []
            if edit_present + edit_absent != edit_total and edit_total > 0:
                calc_remarks.append(f"Attendance mismatch (Present {edit_present} + Absent {edit_absent} != Total {edit_total})")
            if is_dup:
                calc_remarks.append("Possible Duplicate Report")
            default_remark = " | ".join(calc_remarks) if calc_remarks else "OK"

            edit_remarks = st.text_input("Status / Remarks", value=default_remark)

            save_submitted = st.form_submit_button("💾 Save Report to Excel Tracker", use_container_width=True)

        if save_submitted:
            with st.spinner("Saving report to Excel..."):
                final_record = {
                    "Batch Start Date": edit_start_date,
                    "Training Date": edit_training_date,
                    "Timing": edit_timing,
                    "Day": int(edit_day) if str(edit_day).isdigit() else edit_day,
                    "Block Name": edit_block,
                    "Training Location": edit_location,
                    "Course Name": edit_course,
                    "Batch ID": edit_batch_id,
                    "Total Enrolled Candidates": int(edit_total),
                    "Present": int(edit_present),
                    "Absent": int(edit_absent),
                    "Topic": edit_topic,
                    "Trainer Name": edit_trainer,
                    "Remarks": edit_remarks
                }

                # 1. Primary storage: Local Excel
                save_to_excel(final_record)

                # 2. Secondary storage: Google Sheets if configured
                if is_google_sheets_configured():
                    save_to_google_sheets(final_record)

                st.success("✅ **Report Saved to Master Excel Database (`ngo_reports.xlsx`)**")

                try:
                    df = pd.read_excel("ngo_reports.xlsx")
                    csv_data = df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="⬇️ Download Updated Excel Data (CSV)",
                        data=csv_data,
                        file_name="ngo_reports.csv",
                        mime="text/csv",
                        key="btn_download_after_save"
                    )
                except Exception:
                    pass