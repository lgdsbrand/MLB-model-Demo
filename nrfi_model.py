import streamlit as st
import pandas as pd

# Load NRFI data from Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2/export?format=csv&gid=2014899825"  # Replace with your actual NRFI sheet gid

st.set_page_config(page_title="LineupWire NRFI Model", layout="wide")

st.title("🔒 LineupWire MLB Model — NRFI Predictions")

try:
    df = pd.read_csv(sheet_url)

    # Format columns
    df.columns = ["Time", "Matchup", "Pitchers", "NRFI %"]
    df["NRFI %"] = df["NRFI %"].apply(lambda x: f"{round(x * 100)}%")

    # Apply coloring
    def color_nrfi(val):
        if isinstance(val, str) and val.endswith('%'):
            pct = int(val.strip('%'))
            if pct >= 65:
                return 'background-color: green; color: black'
            elif pct < 50:
                return 'background-color: red; color: black'
        return ''

    styled_df = df.style.applymap(color_nrfi, subset=["NRFI %"])

    st.dataframe(styled_df, use_container_width=True)

except Exception as e:
    st.error(f"Failed to load NRFI data: {e}")
