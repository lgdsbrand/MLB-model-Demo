import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sample_data.csv")

# Set Streamlit page config
st.set_page_config(layout="wide", page_title="MLB Betting Model")

# Style helpers
def color_pick(pick):
    if pick == "BET THE OVER":
        return "background-color: #d1f7c4;"  # green
    elif pick == "BET THE UNDER":
        return "background-color: #fcd7d7;"  # red
    elif pick == "NO BET":
        return "background-color: #f1f1f1;"  # gray
    return ""

# Title
st.title("MLB Betting Model")

# Game cards
for idx, row in df.iterrows():
    with st.container():
        st.markdown("---")
        st.markdown(f"### 🕒 {row['game_time']} — {row['team_away']} @ {row['team_home']}")

        col1, col2 = st.columns(2)

        with col1:
            st.image(f"https://a.espncdn.com/i/teamlogos/mlb/500/{row['team_away_abbr']}.png", width=80)
            st.markdown(f"**{row['team_away']}**")
            st.markdown(f"Starter: {row['starter_away']}")
            st.markdown(f"Record: {row['record_away']}")
            st.markdown(f"Last 10: {row['last_10_away']}")

        with col2:
            st.image(f"https://a.espncdn.com/i/teamlogos/mlb/500/{row['team_home_abbr']}.png", width=80)
            st.markdown(f"**{row['team_home']}**")
            st.markdown(f"Starter: {row['starter_home']}")
            st.markdown(f"Record: {row['record_home']")
            st.markdown(f"Last 10: {row['last_10_home']}")

        col3, col4 = st.columns(2)

        with col3:
            st.markdown(f"**Score:** {row['score_away']} - {row['score_home']}")
            st.markdown(f"**Over/Under:** {row['sportsbook_total']} (Model: {row['model_total']})")
            st.markdown(f"**Pick:** ")
            st.markdown(f"<div style='{color_pick(row['over_under_pick'])}padding:6px;border-radius:5px'>{row['over_under_pick']}</div>", unsafe_allow_html=True)

        with col4:
            st.markdown(f"**Moneyline Odds:** {row['moneyline_away']} / {row['moneyline_home']}")
            st.markdown(f"**Win Prob:** {row['win_prob_away']} / {row['win_prob_home']}")
            st.markdown(f"**NRFI Confidence:** {row['nrfi_confidence']}/10")
            st.markdown(f"**Weather:** {row['weather']} {row['dome']}")

# NRFI tab
st.markdown("---")
st.header("⚾ NRFI Confidence Rankings")
nrfi_sorted = df.sort_values(by="nrfi_confidence", ascending=False)
st.dataframe(nrfi_sorted[["team_away", "team_home", "starter_away", "starter_home", "nrfi_confidence"]])
