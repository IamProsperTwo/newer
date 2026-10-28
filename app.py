import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sample Hackathon Project", layout="wide")

st.title("Crop Yield Dashboard")
st.write(
    "A demo project to show how to submit to the NISR Big Data Hackathon. "
    "The data is synthetic (made up) and only for demonstration."
)


@st.cache_data
def load_data():
    return pd.read_csv("data/sample_crop_yield.csv")


df = load_data()

# Sidebar filter
crop = st.sidebar.selectbox("Select crop", sorted(df["crop"].unique()))
filtered = df[df["crop"] == crop]

col1, col2 = st.columns(2)

# Graph 1: average yield by district
with col1:
    st.subheader(f"Average {crop} yield by district")
    by_district = filtered.groupby("district")["yield_kg_per_ha"].mean()
    st.bar_chart(by_district)

# Graph 2: average yield by season
with col2:
    st.subheader(f"Average {crop} yield by season")
    by_season = filtered.groupby("season")["yield_kg_per_ha"].mean()
    st.bar_chart(by_season)

with st.expander("View the data"):
    st.dataframe(filtered)
