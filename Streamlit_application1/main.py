import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="Streamlit Full Demo", layout="wide")

st.title("Streamlit Feature Demonstration App")

st.header("1. Text and Formatting")

st.text("This is plain text")
st.write("Streamlit supports writing many types of objects")
st.markdown("**Markdown Bold Text**")
st.success("Success message")
st.warning("Warning message")
st.error("Error message")
st.info("Information message")

st.divider()

st.header("2. User Input Widgets")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 1, 100)
gender = st.radio("Gender", ["Male", "Female", "Other"])
hobby = st.selectbox("Select hobby", ["Reading", "Gaming", "Sports"])
skills = st.multiselect("Select skills", ["Python", "SQL", "ML", "Data Science"])

agree = st.checkbox("I agree to terms")

if agree:
    st.write("Welcome", name)

st.divider()

st.header("3. Sliders and Buttons")

value = st.slider("Select a value", 0, 100)

if st.button("Show Value"):
    st.write("Selected Value:", value)

st.divider()

st.header("4. File Upload")

file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)
    st.dataframe(df)

st.divider()

st.header("5. Data Display")

data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["A","B","C"]
)

st.table(data)
st.dataframe(data)

st.divider()

st.header("6. Charts")

chart_data = pd.DataFrame(
    np.random.randn(50,3),
    columns=["A","B","C"]
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

st.divider()

st.header("7. Images")

try:
    image = Image.open("sample.jpg")
    st.image(image, caption="Sample Image")
except:
    st.write("Add an image named sample.jpg to display")

st.divider()

st.header("8. Layout")

col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")
    st.button("Button 1")

with col2:
    st.write("Column 2")
    st.button("Button 2")

st.divider()

st.header("9. Sidebar")

st.sidebar.title("Sidebar Menu")

option = st.sidebar.selectbox(
    "Choose page",
    ["Home","Analytics","Settings"]
)

st.sidebar.write("You selected:", option)

st.divider()

st.header("10. Progress and Spinner")

import time

progress = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i+1)

with st.spinner("Processing..."):
    time.sleep(2)

st.success("Done!")

st.divider()

st.header("11. Download Button")

csv = data.to_csv().encode()

st.download_button(
    "Download Data",
    csv,
    "data.csv",
    "text/csv"
)