import streamlit as st
import pandas as pd

# Optional: Set Streamlit page config
st.set_page_config(page_title="MLB Daily Model", layout="wide")

# Title
st.title("MLB Daily Model – Table View")

# Load data from published Google Sheet CSV
csv_url = "https://docs.google.com/spreadsheets/d/1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2/export?format=csv&gid=0"
df = pd.read_csv(csv_url)

# Convert time to 12-hour format if needed
try:
    df["Time"] = pd.to_datetime(df["Time"]).dt.strftime("%-I:%M %p")
except:
    pass  # If already formatted correctly

# Style win % column based on value
def highlight_win_pct(val):
    try:
        pct = int(str(val).replace("%", ""))
        if pct >= 65:
            return "background-color: lightgreen; font-weight: bold;"
    except:
        pass
    return ""

# Display styled DataFrame
st.dataframe(
    df.style.applymap(highlight_win_pct, subset=["ML Win %"]),
    use_container_width=True
)
