import streamlit as st
import pandas as pd

# Import your modules
from src.data_loader import load_dataset
from src.preprocessing import clean_data, preprocess_data
from src.analysis import filtering_data, sorting_data


st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Analysis Dashboard")


st.sidebar.header("⚙️ Settings")

uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset Uploaded Successfully ✅")
else:
    st.warning("Using default dataset...")
    df = load_dataset("superstore.csv")

df = clean_data(df)
df = preprocess_data(df)


if st.checkbox("Show Raw Data"):
    st.dataframe(df)


st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df["sales"].sum(), 2))
col2.metric("Average Sales", round(df["sales"].mean(), 2))
col3.metric("Total Profit", round(df["profit"].sum(), 2))


st.subheader("🔍 Filter Data")

sales_threshold = st.slider("Select Minimum Sales", 0, int(df["sales"].max()), 500)

filtered_df = df[df["sales"] > sales_threshold]

st.write("Filtered Data")
st.dataframe(filtered_df.head())


st.subheader("📊 Top Sales")

sorted_df = df.sort_values(by="sales", ascending=False)
st.dataframe(sorted_df.head(10))



st.subheader("📈 Sales by Region")
region_sales = df.groupby("region")["sales"].sum()
st.bar_chart(region_sales)

st.subheader("📈 Profit by Category")
category_profit = df.groupby("category")["profit"].sum()
st.bar_chart(category_profit)

st.subheader("📈 Monthly Sales Trend")
monthly_sales = df.groupby("order_month")["sales"].sum()
st.line_chart(monthly_sales)


st.subheader("📌 Profit Ratio Distribution")
st.histogram = st.bar_chart(df["profit_ratio"])

st.success("Dashboard Loaded Successfully 🚀")