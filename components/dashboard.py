import streamlit as st
import pandas as pd

def show_dashboard():

        st.subheader("📊 Dashboard")
        try:
            df = pd.read_excel("ngo_reports.xlsx")

            # METRICS
            total_reports = len(df)
            blocks_covered = df["Training Location"].nunique()
            trainers = df["Trainer Name"].nunique()
            courses = df["Course Name"].nunique()

            # METRIC CARDS
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(
                "📄 Total Reports",
                total_reports)
            col2.metric(
                "🏘 Blocks Covered",
                blocks_covered)
            col3.metric(
                "👨‍🏫 Trainers",
                trainers)
            col4.metric(
                "📚 Courses",
                courses)

            # RECENT REPORTS
            st.subheader("📋 Recent Reports")
            st.dataframe(
                df.tail(8),
                use_container_width=True
            )
            st.markdown("---")
        except FileNotFoundError:
            st.warning("⚠ No reports found yet")