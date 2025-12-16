import streamlit as st
import pandas as pd
from datetime import datetime
import os

#Below code tells if user is logged in or not
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "userid" not in st.session_state:
    st.session_state.userid = None
    
#sidebar
st.sidebar.title("Menu")

if not st.session_state.logged_in:
    menu = st.sidebar.radio("Select",["Home","Login","Register"])
else:
    menu = st.sidebar.radio("Select",["Explore CSV","See History","Logout"])
    
#creating home page
if menu == "Home":
    st.title("Welcome")
    st.write("Please login or register to continue")
    
#creating register page
if menu == "Register":
    st.subheader("Register")
    
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    
    if st.button("Register"):
        users = pd.read_csv("users.csv")
        
        if username in users["username"].values:
            st.error("User already exists")
        else:
            new_user = {
                 "userid":len(users) + 1,
                 "username": username,
                 "password":password
        }
        
        users = pd.concat([users, pd.DataFrame([new_user])], ignore_index=True)
        users.to_csv("users.csv",index=False)
        st.success("Registration sucessfull!!!!!") 
        
#creating login page
if menu == "Login":
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    
    if st.button("Login"):
        users = pd.read_csv("users.csv")
        
        user = users[
            (users["username"] == username) &
            (users["password"] == password)
            
        ]
    
        if not user.empty:
             st.session_state.logged_in = True
             st.session_state.userid = int(user.iloc[0]["userid"])
             st.success("Login successful")
             st.rerun()
        else:
            st.error("Invalid Credentials")
        
    #creating explore csv
if menu == "Explore CSV":
        st.subheader("Upload CSV")
        
        uploaded_file = st.file_uploader("Upload CSV",type=["csv"])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
            
            history = pd.read_csv("userfiles.csv")
            new_entry = {
                "userid": st.session_state.userid,
                "filename": uploaded_file.name,
                "upload_time":datetime.now()
            }
            
            history = pd.concat([history, pd.DataFrame([new_entry])], ignore_index=True)
            history.to_csv("userfiles.csv", index=False)
            
#see upload history
if menu =="See History":
    st.subheader("Your Upload History")
    
    history =  pd.read_csv("userfiles.csv")
    user_history = history[history["userid"] == st.session_state.userid]
    
    if user_history.empty:
        st.info("No uploads yet")
    else:
        st.dataframe(user_history)
        
#logout

if menu == "Logout":
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.success("Logged out successfully")
    st.rerun()