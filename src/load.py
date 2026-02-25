from sqlalchemy import create_engine

def load_data(df):

    print("📥 Connecting to MySQL...")

    # 🔐 Replace password with yours
    engine = create_engine(
        "mysql+pymysql://root:admin123@localhost:3306/analysis_db"
    )

    print("📦 Loading data into fact_sales table...")

    df.to_sql(
        name="fact_sales",
        con=engine,
        if_exists="replace",   # replace table each run
        index=False
    )

    print("✅ Data Loaded Successfully into MySQL")

#import os

#def load_data(df):

 #   os.makedirs("data/processed", exist_ok=True)
#### print("📁 Processed file saved successfully")
