import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page title
st.title("📊 Pie Chart Demo")

# Load CSV data
csv_path = os.path.join("data", "pie_demo.csv")
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"Could not find file at {csv_path}")
    st.stop()

# Validate expected columns
if 'Category' not in df.columns or 'Value' not in df.columns:
    st.error("CSV must contain 'Category' and 'Value' columns.")
    st.stop()

# Display data
st.subheader("Raw Data")
st.dataframe(df)

# Pie chart
st.subheader("Pie Chart")
fig, ax = plt.subplots()
ax.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures pie is circular
st.pyplot(fig)
