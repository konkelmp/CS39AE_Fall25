import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Pie Chart Visualization")

# Load CSV from local repo (assuming it's in the 'data' folder)
csv_path = "data/pie_demo.csv"  # Replace with your actual filename
df = pd.read_csv(csv_path)

# Show the data
st.subheader("Data Preview")
st.dataframe(df)

# Select columns for pie chart
category_col = st.selectbox("Select category column", df.columns)
value_col = st.selectbox("Select value column", df.columns)

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(df[value_col], labels=df[category_col], autopct='%1.1f%%')
ax.axis("equal")

st.subheader("Pie Chart")
st.pyplot(fig)
