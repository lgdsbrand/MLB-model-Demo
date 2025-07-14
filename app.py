import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLB Betting Model", layout="wide")

st.title("MLB Betting Model")

# Load sample data
df = pd.read_csv("sample_data.csv")

# Show raw data
st.subheader("Sample Game Predictions")
st.dataframe(df)
