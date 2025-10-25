import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Interactive Pie Chart")

df = pd.read_csv("streamlit_CS/data/pie_demo.csv")

# Show the data
st.subheader("Data Preview")
st.dataframe(df)

# Select columns for pie chart
category_col = st.selectbox("Select category column", df.columns)
value_col = st.selectbox("Select value column", df.columns)

# Create pie chart with Plotly
fig = px.pie(df, names=category_col, values=value_col, title="Fruity Pie Chart")

# Display chart
st.subheader("Pie Chart")
st.plotly_chart(fig, use_container_width=True)
