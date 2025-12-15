import pandas as pd
import pandasql as ps
import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv() 
st.title("Login Page")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if not st.session_state.logged_in:
    st.subheader("Login")    
    username = st.text_input("username")
    password = st.text_input("password", type = "password")

    if st.button("Login"):
       if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()   # refresh app
       else:
            st.error("Invalid username or password")

else:
     st.subheader("Weather App")
     city = st.text_input("Enter city name")

if st.button("Get Weather"):
        api_key= os.getenv("API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        st.write("status:", response.status_code)
        weather = response.json()
        st.write("Temperature: ", weather["main"]["temp"])
        st.write("Humidity: ", weather["main"]["humidity"])
        st.write("Wind Speed:EMONICALLY", weather["wind"]["speed"])
        
if st.button("Logout"):
          st.session_state.logged_in = False
          st.rerun()
     










