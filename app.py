import streamlit as st
from nrfi_model import show_nrfi_model  # This must match the function in nrfi_model.py

# Set page config
st.set_page_config(page_title="LineupWire MLB Models", layout="wide")

# Sidebar navigation
st.sidebar.title("🔘 LineupWire MLB Models")
page = st.sidebar.selectbox("Select a model", ["Daily Predictions", "NRFI Model"])

# Conditional display
if page == "Daily Predictions":
    st.title("📊 LineupWire MLB Model — Daily Predictions")

    # --- Paste your real daily model logic here tomorrow ---
    import pandas as pd

    data = {
        "Game Time": ["3:07 PM", "4:05 PM", "9:10 PM"],
        "Win %": ["44% / 56%", "49% / 51%", "46% / 54%"],
        "Proj Score": ["3.9 - 5.1", "4.1 - 4.2", "4.3 - 4.7"],
        "Model Conf.": [9.0, 8.3, 9.0]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif page == "NRFI Model":
    show_nrfi_model()
