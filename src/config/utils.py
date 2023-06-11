import os

import pandas as pd


def save_dataframe_as_csv(df, filename):
    data_folder = "data"  # Specify the data folder path here

    # Create the data folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    csv_path = os.path.join(data_folder, filename)

    if os.path.exists(csv_path):
        # If the CSV file already exists, append the DataFrame to it
        existing_df = pd.read_csv(csv_path)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.to_csv(csv_path, index=False)
        print(f"DataFrame appended to existing CSV file: {csv_path}")
    else:
        # If the CSV file doesn't exist, save the DataFrame as a new file
        df.to_csv(csv_path, index=False)
        print(f"New CSV file created: {csv_path}")
