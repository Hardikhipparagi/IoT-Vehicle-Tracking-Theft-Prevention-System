import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

st.set_page_config(
    page_title="Vehicle Tracker",
    layout="wide"
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "gps_data.csv"
)

data = pd.read_csv(csv_path)

latest = data.iloc[-1]

st.title("🚗 IoT Vehicle Tracking & Theft Prevention System")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Current Speed",
        f"{latest['speed']} km/h"
    )

with c2:
    st.metric(
        "Latitude",
        latest["latitude"]
    )

with c3:
    st.metric(
        "Longitude",
        latest["longitude"]
    )

st.subheader("Vehicle Location")

m = folium.Map(
    location=[
        latest["latitude"],
        latest["longitude"]
    ],
    zoom_start=15
)

folium.Marker(
    [
        latest["latitude"],
        latest["longitude"]
    ],
    popup="Vehicle Location"
).add_to(m)

st_folium(
    m,
    width=1000,
    height=500
)

st.subheader("GPS History")

st.dataframe(data)