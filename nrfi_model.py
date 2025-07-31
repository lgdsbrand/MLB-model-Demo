import streamlit as st
import pandas as pd
import requests
from datetime import datetime

def fetch_nrfi_data():
    # Replace with your real NRFI model logic
    data = [
        {
            "Time (ET)": "1:05 PM",
            "Matchup": "PHI vs NYY",
            "Pitchers": "Wheeler vs Rodón",
            "Model NRFI %": "76%",
            "Recommended Bet": "NRFI ✅"
        },
        {
            "Time (ET)": "4:10 PM",
            "Matchup": "PIT vs ARI",
            "Pitchers": "Jones vs Gallen",
            "Model NRFI %": "78%",
            "Recommended Bet": "NRFI ✅"
        },
        {
            "Time (ET)": "7:10 PM",
            "Matchup": "BOS vs DET",
            "Pitchers": "Bello vs Skubal",
            "Model NRFI %": "62%",
            "Recommended Bet": "YRFI ❌"
        }
    ]
    return pd.DataFrame(data)

def render():
    st.title("🚫 NRFI Model (No Run First Inning)")

    df = fetch_nrfi_data()

    def highlight_bets(val):
        if "NRFI" in val:
            return "background-color: lightgreen; color: black"
        elif "YRFI" in val:
            return "background-color: lightcoral; color: black"
        return ""

    st.dataframe(
        df.style.applymap(highlight_bets, subset=["Recommended Bet"]),
        use_container_width=True
    )
