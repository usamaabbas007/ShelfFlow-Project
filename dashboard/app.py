
import streamlit as st
import pandas as pd

st.title("ShelfFlow Dashboard")
st.markdown("### Daily Inventory & Shortage Insights")

df = pd.read_csv("data/daily_inventory_summary.csv")
df['date'] = pd.to_datetime(df['date'])

selected_store = st.selectbox("Select Store", df['store_id'].unique())
filtered = df[df['store_id'] == selected_store]

st.line_chart(filtered.set_index('date')[['units_sold', 'units_short']])
