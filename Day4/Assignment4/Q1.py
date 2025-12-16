import streamlit as st
import time

st.title("My Chatbot")

#To store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
user_msg = st.chat_input("Type you message")

def stream_text(text):
    for ch in text:
        yield ch
        time.sleep(0.05)
        
if user_msg:
    st.write("You:")
    st.write(user_msg)

    st.write("Bot:")
    st.write_stream(stream_text(user_msg))