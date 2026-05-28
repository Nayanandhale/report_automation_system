import streamlit as st

from utils.ocr_handler import extract_text_from_image

from extractor.main_extractor import extract_report

from utils.translator_handler import translate_report_data

from excel_handler import save_to_excel

from sheets.sheets_handler import save_to_google_sheets

from ai.duplicate_extractor import is_duplicate


def show_upload():

    st.subheader("📸 Upload Report Screenshot")

    uploaded_image = st.file_uploader(
        "Upload Report Screenshot",
        type=["png", "jpg", "jpeg"]
    )

    # DEFAULT OCR TEXT
    ocr_text = ""

    if uploaded_image is not None:

        with st.spinner("Extracting text from image..."):

            ocr_text = extract_text_from_image(
                uploaded_image
            )

    # FINAL EDITABLE REPORT
    st.subheader("📝 Review & Edit Report")

    report = st.text_area(
        "You can edit report here...",
        value=ocr_text,
        height=200
    )

    # SUBMIT BUTTON
    if st.button("🚀 Submit Report"):

        st.write("BUTTON CLICKED")

        if report.strip() == "":

            st.error("⚠ Please provide report first")

        else:

            try:

                st.write("STARTING EXTRACTION")

                data = extract_report(report)

                st.write("EXTRACTION DONE")

                data = translate_report_data(data)

                st.write("TRANSLATION DONE")

                if is_duplicate(data):

                    existing_remark = data.get(
                        "Remarks",
                        ""
                    )

                    duplicate_remark = (
                        "Possible Duplicate Report"
                    )

                    if existing_remark == "OK":

                        data["Remarks"] = duplicate_remark

                    else:

                        data["Remarks"] = (
                            existing_remark
                            + " | "
                            + duplicate_remark
                        )

                st.write("DUPLICATE CHECK DONE")

                st.write(data)

                save_to_excel(data)

                st.write("EXCEL SAVE DONE")

                save_to_google_sheets(data)

                st.write("GOOGLE SHEETS SAVE DONE")

                st.success(
                    "✅ Report Submitted Successfully"
                )

            except Exception as e:

                st.error(f"FULL ERROR: {e}")