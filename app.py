import streamlit as st
import pandas as pd
import nrfi_model

# Set page config
st.set_page_config(page_title="LineupWire MLB Model", layout="wide")

# Sidebar dropdown to choose model
model_choice = st.sidebar.selectbox(
    "Select Model:",
    ["Daily Predictions", "NRFI Model"]
)

# DAILY MODEL
if model_choice == "Daily Predictions":
    st.title("📊 LineupWire MLB Model — Daily Predictions")

    sheet_url = "https://docs.google.com/spreadsheets/d/1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2/export?format=csv&id=1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2&gid=0"

    try:
        df = pd.read_csv(sheet_url)

        df.columns = [
            "Game", "Game Time", "Win %", "Proj Score", "Model O/U", "Book O/U",
            "Bet", "Confidence", "Starting Pitchers", "Weather"
        ]

        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error("Failed to load Daily Model data. Please check the Google Sheet or URL.")

# NRFI MODEL
elif model_choice == "NRFI Model":
    nrfi_model.render()
