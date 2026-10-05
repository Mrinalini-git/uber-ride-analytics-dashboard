import streamlit as st
import pandas as pd
import plotly.express as px
import os
import kagglehub

st.set_page_config(
    page_title="Uber Ride Analytics",
    page_icon="🚗",
    layout="wide"
)

st.title("Uber Ride Analytics Dashboard")
st.markdown("Interactive analysis of Uber ride booking data")

# Download dataset
path = kagglehub.dataset_download(
    "yashdevladdha/uber-ride-analytics-dashboard"
)

# Find CSV file
csv_files = [
    file for file in os.listdir(path)
    if file.endswith(".csv")
]

csv_path = os.path.join(path, csv_files[0])

# Load data
df = pd.read_csv(csv_path)

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

st.write("Dataset shape:", df.shape)
st.write("Columns:", list(df.columns))