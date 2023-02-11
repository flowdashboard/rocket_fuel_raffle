import streamlit as st
import gspread
import pandas as pd

st.set_page_config("Rocket Fuel Raffle",
                   "🚀",
                   initial_sidebar_state="collapsed",
                   layout="centered")

# Create a connection object.
gc = gspread.service_account()

# Read secret for google docs access
sheet_url = st.secrets["public_gsheets_url"]

# Uses st.cache_data to only rerun when the query changes or after 10 sec.
@st.cache_data(ttl=10)
def load_data(query):
    sheet = gc.open_by_url(sheet_url).sheet1
    df = pd.DataFrame(sheet.get_all_records())
    return df

if __name__ == "__main__":
    st.title('🚀 Leaderboard 🚀')

    data_load_state = st.text('Loading data...')
    df = load_data()
    data_load_state.empty()
    
    df.show()
