import pandas as pd
import plotly.graph_objects as go

lat, lon = 39.7392, -104.9903  # Denver
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
@st.cache_data(ttl=600)
def get_weather():
    r = requests.get(wurl, timeout=10); r.raise_for_status()
    j = r.json()["current"]
    return pd.DataFrame([{"time": pd.to_datetime(j["time"]),
                          "temperature": j["temperature_2m"],
                          "wind": j["wind_speed_10m"]}])

df = get_weahter()

# Create figure
fig = go.Figure()

# Temperature trace
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['temperature'],
    name='Temperature (°F)',
    mode='lines+markers',
    line=dict(color='firebrick'),
    yaxis='y1'
))

# Wind trace
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['wind'],
    name='Wind Speed (mph)',
    mode='lines+markers',
    line=dict(color='royalblue'),
    yaxis='y2'
))

# Layout with dual y-axes
fig.update_layout(
    title='Weather Data Over Time',
    xaxis=dict(title='Time'),
    yaxis=dict(title='Temperature (°F)', side='left'),
    yaxis2=dict(title='Wind Speed (mph)', overlaying='y', side='right'),
    legend=dict(x=0.01, y=0.99),
    margin=dict(l=40, r=40, t=40, b=40)
)

# Show chart
fig.show()
