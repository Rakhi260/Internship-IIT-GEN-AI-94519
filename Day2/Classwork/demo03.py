import streamlit as st

st.title("Hello everyone!!!")
st.header("Welcome to streamlit demo")
st.subheader("This is subheader")
st.text("This is a text display")

if st.button("Click me",type="primary"):
    st.write("You clicked me!!")