import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Risk Dashboard", layout="wide")

df = pd.read_csv("data/risk_logs.csv")

from models.scorer import score

if 'risk_level' not in df.columns:
    df['risk_level'] = df.apply(score, axis=1)


st.title("🔍 AI Risk Log Explorer")

# Sidebar filters
departments = df['department'].unique().tolist()
risk_levels = df['risk_level'].unique().tolist()

selected_depts = st.sidebar.multiselect("Filter by Department", departments, default=departments)
selected_risks = st.sidebar.multiselect("Filter by Risk Level", risk_levels, default=risk_levels)

filtered_df = df[
    df['department'].isin(selected_depts) &
    df['risk_level'].isin(selected_risks)
]

st.subheader("📊 Risk Level Distribution")
risk_counts = filtered_df['risk_level'].value_counts()
st.bar_chart(risk_counts)

st.subheader("📋 Filtered Data")
st.dataframe(filtered_df)

import io

st.subheader("📥 Download Filtered Results")

csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='filtered_risk_data.csv',
    mime='text/csv'
)


st.markdown("---")
st.caption(f"Showing {len(filtered_df)} out of {len(df)} records.")

