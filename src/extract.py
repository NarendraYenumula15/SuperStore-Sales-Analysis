import pandas as pd
import os

def extract_data():

    file_path = os.path.join("data", "raw", "Sample_Superstore.csv")

    df = pd.read_csv(file_path, encoding="latin1")

    print("✅ Data Extracted Successfully")
    print("Shape:", df.shape)

    return df
