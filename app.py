import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("covid_data.csv")

# Page config
st.set_page_config(page_title="India COVID-19 Dashboard", layout="wide")
st.title("India COVID-19 Dashboard (All States Combined)")

# National totals
total_cases = df["Total Cases"].sum()
active_cases = df["Active"].sum()
discharged = df["Discharged"].sum()
deaths = df["Deaths"].sum()

# Metrics display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases", f"{total_cases:,}")
col2.metric("Active Cases", f"{active_cases:,}")
col3.metric("Discharged", f"{discharged:,}")
col4.metric("Deaths", f"{deaths:,}")

st.markdown("---")

# Pie Chart - Share of total cases by state
st.subheader("State-wise Share of Total Cases")
pie = px.pie(df, names="State", values="Total Cases", title="Total Cases by State")
st.plotly_chart(pie, use_container_width=True)

# Bar Chart - State-wise Active/Discharged/Deaths
st.subheader("State-wise Breakdown")
bar = px.bar(
    df,
    x="State",
    y=["Active", "Discharged", "Deaths"],
    barmode="group",
    title="Cases by Category",
    height=500
)
st.plotly_chart(bar, use_container_width=True)

# Optional Filter
with st.expander("Show State-Wise Data"):
    state_filter = st.multiselect("Filter States", df["State"].unique(), default=df["State"].unique())
    filtered = df[df["State"].isin(state_filter)]
    st.dataframe(filtered.sort_values("Total Cases", ascending=False), use_container_width=True)
