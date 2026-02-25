import pandas as pd
import numpy as np

def transform_data(df):

    print("🔄 Starting Data Cleaning...")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df = df.drop_duplicates()

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

    df = df.dropna(subset=['order_date', 'ship_date'])

    df = df[df['sales'] >= 0]

    df['postal_code'] = df['postal_code'].fillna(0)
    df['discount'] = df['discount'].fillna(0)
    df['profit'] = df['profit'].fillna(0)

    df['customer_name'] = df['customer_name'].str.strip()
    df['city'] = df['city'].str.title()
    df['state'] = df['state'].str.title()

    print("✅ Cleaning Completed")
    return df
