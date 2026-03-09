import pandas as pd
import numpy as np


def clean_data(df):

    print("\nChecking Missing Values")
    print(df.isnull().sum())

    # Fill missing values
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())
    df["Profit"] = df["Profit"].fillna(df["Profit"].median())
    df["Discount"] = df["Discount"].fillna(0)

    # Remove duplicates
    df = df.drop_duplicates()

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    print("\nData Cleaning Completed")

    return df


def preprocess_data(df):

    # Convert date column
    df["order date"] = pd.to_datetime(df["order date"])

    # Extract useful features
    df["order_year"] = df["order date"].dt.year
    df["order_month"] = df["order date"].dt.month

    # Create profit ratio
    df["profit_ratio"] = df["profit"] / df["sales"]

    print("\nData Preprocessing Completed")

    return df