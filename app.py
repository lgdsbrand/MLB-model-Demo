import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="LineupWire MLB Model — Daily Predictions", layout="centered")

st.title("📊 LineupWire MLB Model — Daily Predictions")

# Sample data (replace with your real model data)
data = [
    {
        "Time": "3:07 PM",
        "Matchup": "Giants @ Blue Jays",
        "Pitchers": "Webb vs Gausman",
        "Model Score": "3.6 - 4.2",
        "ML Winner": "Blue Jays",
        "ML Win %": "56%",
        "Book O/U": 8.5,
        "Model O/U": 7.8,
        "O/U Bet": "BET THE UNDER"
    },
    {
        "Time": "4:05 PM",
        "Matchup": "Orioles @ Yankees",
        "Pitchers": "Bradish vs Rodón",
        "Model Score": "4.1 - 4.3",
        "ML Winner": "Yankees",
        "ML Win %": "51%",
        "Book O/U": 9,
        "Model O/U": 8.4,
        "O/U Bet": "NO BET"
    },
    {
        "Time": "9:10 PM",
        "Matchup": "Rangers @ Mariners",
        "Pitchers": "Eovaldi vs Gilbert",
        "Model Score": "4.2 - 4.6",
        "ML Winner": "Mariners",
        "ML Win %": "54%",
        "Book O/U": 7.5,
        "Model O/U": 9.3,
        "O/U Bet": "BET THE OVER"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Show table
st.dataframe(df, use_container_width=True)
