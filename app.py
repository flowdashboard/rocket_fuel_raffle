import streamlit as st
from gsheetsdb import connect
import pandas as pd

st.set_page_config("Rocket Fuel Raffle",
                   "🚀",
                   initial_sidebar_state="collapsed",
                   layout="centered")

# Create a connection object.
conn = connect()

# Read secret for google docs access
sheet_url = st.secrets["public_gsheets_url"]

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 5 sec.
@st.cache_data(ttl=5)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

if __name__ == "__main__":
    st.title('🚀 Leaderboard 🚀')

    data_load_state = st.text('Loading data...')
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    df = pd.DataFrame(rows)
    data_load_state.empty()
    
    print(rows)   
    df.show()
