import pandas as pd
import os
FILE_NAME = "ngo_reports.xlsx"
def save_to_excel(data):
    new_df = pd.DataFrame([data])
    if os.path.exists(FILE_NAME):
        old_df = pd.read_excel(FILE_NAME)
        updated_df = pd.concat(
            [old_df, new_df],
            ignore_index=True
        )
    else:
        updated_df = new_df
    updated_df.to_excel(
        FILE_NAME,
        index=False
    )