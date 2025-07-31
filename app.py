import streamlit as st
import nrfi_model  # already added above

# Sidebar for model selection
page = st.sidebar.selectbox("Select a Model", ["Daily Model", "NRFI Model"])

# Conditional routing
if page == "Daily Model":
    # 💡 This is your current MLB daily model logic block
    st.title("LineupWire MLB Model — Daily Predictions")
    
    # (Leave all your current Daily Model table code here...)

elif page == "NRFI Model":
    nrfi_model.run_nrfi_model()  # 🔁 Calls your NRFI table
import streamlit as st
import pandas as pd
import nrfi_model

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
