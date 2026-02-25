import numpy as np
import pandas as pd

def add_features(df):

    print("⚙ Adding Features...")

    # 📅 Date Features
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['quarter'] = df['order_date'].dt.quarter

    # 🚚 Shipping Days
    df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days

    # 💰 1️⃣ Raw Profit Margin (Mathematical Truth)
    df['profit_margin_raw'] = np.where(
        df['sales'] == 0,
        0,
        (df['profit'] / df['sales']) * 100
    )

    # 💰 2️⃣ Adjusted Profit Margin (Analysis-Safe)

    # Step A: Ignore very small sales
    df['profit_margin_adjusted'] = np.where(
        df['sales'] < 10,
        np.nan,
        df['profit_margin_raw']
    )

    # Step B: Cap extreme values
    df['profit_margin_adjusted'] = df['profit_margin_adjusted'].clip(-200, 200)

    # Step C: Round values
    df['profit_margin_raw'] = df['profit_margin_raw'].round(2)
    df['profit_margin_adjusted'] = df['profit_margin_adjusted'].round(2)

    # 🏷 Sales Category
    df['sales_category'] = pd.cut(
        df['sales'],
        bins=[0, 100, 500, float('inf')],
        labels=['Low', 'Medium', 'High']
    )

    print("✅ Feature Engineering Completed")

    return df
