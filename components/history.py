import streamlit as st
import pandas as pd

def show_history():

        st.subheader("📜 Report History")
        try:
            df = pd.read_excel("ngo_reports.xlsx")

            search = st.text_input(
                "🔍 Search Reports"
            )

            col1, col2, col3 = st.columns(3)
            # TRAINING LOCATION FILTER
            with col1:
                locations = ["All"] + list(
                    df["Training Location"].dropna().unique())
                selected_location = st.selectbox(
                    "🏘 Filter by Block",
                    locations)

            # COURSE FILTER
            with col2:
                courses = ["All"] + list(
                    df["Course Name"].dropna().unique())
                selected_course = st.selectbox(
                    "📚 Filter by Course",
                    courses)

            # BATCH ID FILTER
            with col3:
                batch_ids = ["All"] + list(
                    df["Batch ID"].dropna().unique() )
                selected_batch = st.selectbox(
                    "🆔 Filter by Batch ID",
                    batch_ids)

            # APPLY SEARCH
            if search:
                df = df[
                    df.astype(str)
                    .apply(
                        lambda row:
                        row.str.contains(
                            search,
                            case=False
                        ).any(),
                        axis=1
                    )
                ]

            # APPLY FILTERS
            if selected_location != "All":
                df = df[
                    df["Training Location"]
                    == selected_location
                ]
            if selected_course != "All":
                df = df[
                    df["Course Name"]
                    == selected_course
                ]
            if selected_batch != "All":
                df = df[
                    df["Batch ID"]
                    == selected_batch
                ]

            # DATAFRAME
            st.dataframe(
                df,
                use_container_width=True,
                height=500
            )

            # DOWNLOAD BUTTON
            excel_data = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇ Download Reports CSV",
                data=excel_data,
                file_name="filtered_reports.csv",
                mime="text/csv"
            )
        except FileNotFoundError:
            st.warning("⚠ No report history found yet")
        except Exception as e:
            st.error(f"Error loading history: {e}")