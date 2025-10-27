# Code generated with assistance from CoPilot AI for plot and debugging

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import requests
import time

lat, lon = 39.7392, -104.9903  # Denver
wurl = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&current=temperature_2m,wind_speed_10m"
    "&temperature_unit=fahrenheit"
    "&wind_speed_unit=mph"
)

@st.cache_data(ttl=600)
def get_weather():
    try:
        r = requests.get(wurl, timeout=10)
        r.raise_for_status()
        j = r.json()["current"]
        return {
            "time": pd.to_datetime(j["time"]),
            "temperature": j["temperature_2m"],
            "wind": j["wind_speed_10m"]
        }, None
    except requests.RequestException as e:
        return None, f"Weather API error: {e}"
        
# Page Set Up
st.set_page_config(page_title="Live Weather Tracker", page_icon="🌡️", layout="wide")
st.title("🌡️ Open-Meteo: Current Weather in Denver")
st.caption("Live temperature and wind speed with short-term history.")

# Auto Refresh Controls
st.subheader("🔁 Auto Refresh Settings")
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

if "weather_history" not in st.session_state:
    st.session_state.weather_history = pd.DataFrame(columns=["time", "temperature", "wind"])

# Fetch New Data
data, err = get_weather()
if err:
    st.warning(err)
else:
    new_row = pd.DataFrame([data])
    st.session_state.weather_history = pd.concat(
        [st.session_state.weather_history, new_row],
        ignore_index=True
    )

    # Keep only last 20 entries
    st.session_state.weather_history = st.session_state.weather_history.tail(20)

    st.subheader("Recent Weather Data")
    st.dataframe(st.session_state.weather_history, use_container_width=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=st.session_state.weather_history["time"],
        y=st.session_state.weather_history["temperature"],
        name="Temperature (°F)",
        mode="lines+markers",
        line=dict(color="firebrick"),
        yaxis="y1"
    ))

    fig.add_trace(go.Scatter(
        x=st.session_state.weather_history["time"],
        y=st.session_state.weather_history["wind"],
        name="Wind Speed (mph)",
        mode="lines+markers",
        line=dict(color="royalblue"),
        yaxis="y2"
    ))

    fig.update_layout(
        title="Weather Trends Over Time",
        xaxis=dict(title="Time"),
        yaxis=dict(title="Temperature (°F)", side="left", range=[0, 100]),
        yaxis2=dict(title="Wind Speed (mph)", overlaying="y", side="right", range=[0, 40]),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    st.rerun()
