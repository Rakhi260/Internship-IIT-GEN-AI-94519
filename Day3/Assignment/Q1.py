import pandas as pd
import pandasql as ps
import streamlit as st

st.title("CSV File uploader")
data_file = st.file_uploader("upload csv",type = ["csv"])
if data_file:
    df = pd.read_csv(data_file)
    st.write("Uploaded Data: ")
    st.dataframe(df)
    
query = st.text_area("Enter your query",value = "Select * from df")

if st.button("Execute Query"):
    try:
        result = ps.sqldf(query,locals())
        print("Results: ")
        st.dataframe(result)
    except Exception as e:
            st.error(f"Please upload file")