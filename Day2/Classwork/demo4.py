import pandas as pd
import streamlit as st

st.title("CSV Explorer")
data_file = st.file_uploader("Upload a CSV file",type=["csv","pdf"])

if data_file:
    df = pd.read_csv(data_file)
    st.dataframe(df)
