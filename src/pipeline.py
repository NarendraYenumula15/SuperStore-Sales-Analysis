from src.extract import extract_data
from src.transform import transform_data
from src.feature_engineering import add_features
from src.validation import validate_data
from src.load import load_data


def run_pipeline():

    print("🔄 Starting ETL Pipeline...")

    # 1️⃣ Extract
    df = extract_data()

    # 2️⃣ Transform (Cleaning + Preprocessing)
    df = transform_data(df)

    # 3️⃣ Feature Engineering
    df = add_features(df)

    # 4️⃣ Data Validation
    validation_report = validate_data(df)

    # Optional: Stop pipeline if critical issues found
    if validation_report["status"] == "failed":
        print("❌ Validation Failed. Pipeline Stopped.")
        print("Issues Found:", validation_report["issues"])
        return

    # 5️⃣ Load
    load_data(df)

    print("🚀 ETL Completed Successfully")


if __name__ == "__main__":
    run_pipeline()


