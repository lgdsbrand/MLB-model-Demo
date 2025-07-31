import streamlit as st
import pandas as pd

def run_nrfi_model():
    # Load NRFI data from Google Sheet
    sheet_url = "https://docs.google.com/spreadsheets/d/1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2/export?format=csv&gid=1931554076"

    # Set page config and title
    st.set_page_config(page_title="LineupWire MLB Model – NRFI")
    st.title("🔒 LineupWire MLB Model – NRFI Projections")

    try:
        df = pd.read_csv(sheet_url)

        # Rename columns if needed
        df.columns = ["Time", "Matchup", "NRFI %"]

        # Apply conditional coloring
        def color_nrfi(val):
            if isinstance(val, str) and val.endswith('%'):
                pct = int(val.strip('%'))
                if pct >= 65:
                    return 'background-color: lightgreen; color: black'
                elif pct < 50:
                    return 'background-color: lightcoral; color: black'
            return ''

        styled_df = df.style.applymap(color_nrfi, subset=["NRFI %"])
        st.dataframe(styled_df, use_container_width=True)

    except Exception as e:
        st.error(f"Failed to load NRFI data: {e}")
        def render():
    import streamlit as st
    import pandas as pd

    st.title("🚫 NRFI Model — No Run First Inning Predictions")

    sheet_url = "https://docs.google.com/spreadsheets/d/1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2/export?format=csv&id=1hUxaRjULzP6C6xkMw4Pw9qhVONtNe5I2&gid=771829288"

    try:
        df = pd.read_csv(sheet_url)

        df.columns = ["Time", "Matchup", "Pitchers", "NRFI %"]

        def color_nrfi(val):
            if isinstance(val, str) and val.endswith('%'):
                pct = int(val.strip('%'))
                if pct >= 65:
                    return 'background-color: lightgreen; color: black'
                elif pct < 50:
                    return 'background-color: lightcoral; color: black'
            return ''

        styled_df = df.style.applymap(color_nrfi, subset=["NRFI %"])
        st.dataframe(styled_df, use_container_width=True)

    except Exception as e:
        st.error("Failed to load NRFI data.")
