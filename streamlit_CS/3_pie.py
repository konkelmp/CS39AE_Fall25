import streamlit as st
import pandas as pd

st.title("New Page Test")

df = pd.read_csv("data/pie_demo.csv")
st.write(df.head())
