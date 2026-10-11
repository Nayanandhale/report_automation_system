import streamlit as st
import pandas as pd
import os

def show_dashboard():
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #DCE7E0; border-radius:14px; padding:20px; margin-bottom:20px;">
        <h3 style="color:#005A36; margin:0 0 6px 0; font-size:18px; font-weight:700;">
            📊 Training Reports Analytics Dashboard
        </h3>
        <p style="color:#52635B; margin:0; font-size:13px;">
            Overview of training operations, center coverage, attendance rates, and recent field submissions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not os.path.exists("ngo_reports.xlsx"):
        st.warning("⚠️ No reports found yet. Upload or ingest a report first to view analytics.")
        return

    try:
        df = pd.read_excel("ngo_reports.xlsx")
        if df.empty:
            st.warning("⚠️ The reports database is currently empty.")
            return

        # Core Metrics Calculations
        total_reports = len(df)
        total_enrolled = df["Total Enrolled Candidates"].sum() if "Total Enrolled Candidates" in df.columns else 0
        total_present = df["Present"].sum() if "Present" in df.columns else 0
        
        avg_attendance = 0
        if total_enrolled > 0:
            avg_attendance = round((total_present / total_enrolled) * 100, 1)

        blocks_covered = df["Training Location"].nunique() if "Training Location" in df.columns else 0
        trainers_count = df["Trainer Name"].nunique() if "Trainer Name" in df.columns else 0
        courses_count = df["Course Name"].nunique() if "Course Name" in df.columns else 0

        # Metric Cards Row
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("📄 Total Reports", total_reports)
        col2.metric("👥 Total Enrolled", total_enrolled)
        col3.metric("📈 Avg Attendance", f"{avg_attendance}%")
        col4.metric("🏘 Centers / Locations", blocks_covered)
        col5.metric("📚 Active Courses", courses_count)

        st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

        # Charts Section
        chart_col1, chart_col2 = st.columns([1, 1])

        with chart_col1:
            st.markdown("##### 📊 Reports by Course")
            if "Course Name" in df.columns:
                course_counts = df["Course Name"].value_counts().reset_index()
                course_counts.columns = ["Course Name", "Reports"]
                st.bar_chart(data=course_counts.set_index("Course Name"))

        with chart_col2:
            st.markdown("##### 📍 Reports by Location / Block")
            if "Training Location" in df.columns:
                loc_counts = df["Training Location"].value_counts().reset_index()
                loc_counts.columns = ["Location", "Reports"]
                st.bar_chart(data=loc_counts.set_index("Location"))

        st.markdown("---")

        # RECENT REPORTS TABLE
        st.markdown("##### 📋 Recent Report Submissions")
        display_cols = [
            "Training Date", "Course Name", "Batch ID", "Training Location",
            "Present", "Absent", "Total Enrolled Candidates", "Trainer Name", "Remarks"
        ]
        available_cols = [c for c in display_cols if c in df.columns]
        recent_df = df[available_cols].tail(10)

        st.dataframe(
            recent_df,
            width='stretch',
            hide_index=True
        )

    except Exception as e:
        st.error(f"Error loading dashboard metrics: {e}")