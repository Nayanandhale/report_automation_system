import streamlit as st
import pandas as pd
import io
import os

def show_history():
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #DCE7E0; border-radius:14px; padding:20px; margin-bottom:20px;">
        <h3 style="color:#005A36; margin:0 0 6px 0; font-size:18px; font-weight:700;">
            📜 Master Report History & Search
        </h3>
        <p style="color:#52635B; margin:0; font-size:13px;">
            Search, filter, inspect, and export all recorded training reports across batches and centers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not os.path.exists("ngo_reports.xlsx"):
        st.warning("⚠️ No report history found yet. Reports will appear here once saved.")
        return

    try:
        df = pd.read_excel("ngo_reports.xlsx")
        if df.empty:
            st.warning("⚠️ The reports database is currently empty.")
            return

        # SEARCH BAR
        search = st.text_input("🔍 Search reports by any keyword (Trainer, Topic, Batch, Location...)", placeholder="Type to search...")

        # FILTER CONTROLS
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            locations = ["All"] + sorted([str(x) for x in df["Training Location"].dropna().unique()]) if "Training Location" in df.columns else ["All"]
            selected_location = st.selectbox("🏘 Filter by Location", locations)

        with col2:
            courses = ["All"] + sorted([str(x) for x in df["Course Name"].dropna().unique()]) if "Course Name" in df.columns else ["All"]
            selected_course = st.selectbox("📚 Filter by Course", courses)

        with col3:
            batch_ids = ["All"] + sorted([str(x) for x in df["Batch ID"].dropna().unique()]) if "Batch ID" in df.columns else ["All"]
            selected_batch = st.selectbox("🆔 Filter by Batch ID", batch_ids)

        with col4:
            status_opts = ["All", "OK Only", "Mismatches / Warnings"]
            selected_status = st.selectbox("⚠️ Status Filter", status_opts)

        filtered_df = df.copy()

        # APPLY SEARCH
        if search:
            mask = filtered_df.astype(str).apply(lambda row: row.str.contains(search, case=False).any(), axis=1)
            filtered_df = filtered_df[mask]

        # APPLY LOCATION FILTER
        if selected_location != "All" and "Training Location" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Training Location"].astype(str) == selected_location]

        # APPLY COURSE FILTER
        if selected_course != "All" and "Course Name" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Course Name"].astype(str) == selected_course]

        # APPLY BATCH FILTER
        if selected_batch != "All" and "Batch ID" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Batch ID"].astype(str) == selected_batch]

        # APPLY STATUS FILTER
        if selected_status == "OK Only" and "Remarks" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Remarks"].astype(str).str.upper() == "OK"]
        elif selected_status == "Mismatches / Warnings" and "Remarks" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Remarks"].astype(str).str.upper() != "OK"]

        # SUMMARY BADGE
        st.markdown(f"**Showing {len(filtered_df)} of {len(df)} total reports**")

        # DATAFRAME VIEW
        st.dataframe(
            filtered_df,
            width='stretch',
            height=400,
            hide_index=True
        )

        # EXPORT CONTROLS
        exp_col1, exp_col2, _ = st.columns([1, 1, 2])

        with exp_col1:
            csv_data = filtered_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Export as CSV",
                data=csv_data,
                file_name="unnatva_reports.csv",
                mime="text/csv",
                key="download_csv_history"
            )

        with exp_col2:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                filtered_df.to_excel(writer, index=False, sheet_name="Reports")
            st.download_button(
                label="⬇️ Export as Excel (.xlsx)",
                data=buffer.getvalue(),
                file_name="unnatva_reports.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_xlsx_history"
            )

    except Exception as e:
        st.error(f"Error loading report history: {e}")