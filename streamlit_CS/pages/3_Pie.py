import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Interactive Pie Chart")

df = pd.read_csv("streamlit_CS/data/pie_demo.csv")

# Show the data
st.subheader("Data Preview")
st.dataframe(df)

# Create pie chart with Plotly
fig = px.pie(df, names=df.columns[0], values=df.columns[1], title="Fruity Pie Chart")

# Display chart
st.subheader("Pie Chart")
st.plotly_chart(fig, use_container_width=True)
