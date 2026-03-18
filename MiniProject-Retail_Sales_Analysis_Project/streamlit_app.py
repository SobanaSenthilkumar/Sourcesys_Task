import streamlit as st
import pandas as pd

# Import your project modules
from src.preprocessing import clean_data, preprocess_data

# Page settings
st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Analysis Dashboard")

# =========================
# 📂 File Upload (MANDATORY)
# =========================
st.sidebar.header("Upload Dataset")

uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is None:
    st.warning("Please upload a dataset to continue")
    st.stop()

# Read dataset
df = pd.read_csv(uploaded_file)

st.success("Dataset Uploaded Successfully ✅")

# =========================
# 🧹 Cleaning & Preprocessing
# =========================
df = clean_data(df)
df = preprocess_data(df)

# =========================
# 👀 Show Raw Data
# =========================
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# =========================
# 📊 KPI Metrics
# =========================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df["sales"].sum(), 2))
col2.metric("Average Sales", round(df["sales"].mean(), 2))
col3.metric("Total Profit", round(df["profit"].sum(), 2))


st.subheader("🔍 Filter Data")

min_sales = int(df["sales"].min())
max_sales = int(df["sales"].max())

sales_threshold = st.slider(
    "Select Minimum Sales",
    min_value=min_sales,
    max_value=max_sales,
    value=500
)

filtered_df = df[df["sales"] > sales_threshold]

st.write("Filtered Data")
st.dataframe(filtered_df.head())


st.subheader("📊 Top 10 Sales")

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

# =========================
# 📌 Extra Insight
# =========================
st.subheader("📌 Profit Ratio Distribution")
st.bar_chart(df["profit_ratio"])

# =========================
# 📥 Download Option
# =========================
st.subheader("📥 Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

st.success("Dashboard Loaded Successfully 🚀")