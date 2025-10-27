import pandas as pd
import plotly.express as px
import streamlit as st
import requests
import time

# --- Weather API Setup ---
lat, lon = 39.7392, -104.9903  # Denver
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

@st.cache_data(ttl=600)
def get_weather():
    try:
        r = requests.get(wurl, timeout=10)
        r.raise_for_status()
        j = r.json()["current"]
        df = pd.DataFrame([{
            "time": pd.to_datetime(j["time"]),
            "temperature": j["temperature_2m"],
            "wind": j["wind_speed_10m"]
        }])
        return df, None
    except requests.RequestException as e:
        return None, f"Weather API error: {e}"

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Live Weather Demo", page_icon="🌡️", layout="wide")

st.markdown("""
    <style>
      [data-testid="stPlotlyChart"], .stPlotlyChart, .stElementContainer {
        transition: none !important;
        opacity: 1 !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("🌡️ Open-Meteo: Current Weather in Denver")
st.caption("Live temperature and wind speed from Open-Meteo API.")

# --- Auto Refresh Controls ---
st.subheader("🔁 Auto Refresh Settings")
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

# --- Weather Data ---
st.subheader("Current Weather")
df, err = get_weather()

if err:
    st.warning(err)
else:
    st.dataframe(df, use_container_width=True)

    # --- Plotly Chart ---
    fig = px.bar(
        df.melt(id_vars="time", value_vars=["temperature", "wind"]),
        x="variable",
        y="value",
        color="variable",
        title="Current Temperature and Wind Speed",
        labels={"value": "Measurement", "variable": "Metric"},
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Auto Refresh Logic ---
if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    st.rerun()
