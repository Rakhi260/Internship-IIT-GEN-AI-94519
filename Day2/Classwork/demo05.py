import streamlit as st

if 'messages' not in  st.session_state:
    st.session_state.messages = []
    
with st.sidebar:
    st.header("Settings")
    choices = ["Lower","Upper","Toggle"]
    mode = st.selectbox("Select Mode",choices)
    count = st.slider("Select count",min_value=2,max_value=10,step=1,value=5)
    
    st.subheader("Config")
    st.json({"mode":mode,"count":count})
    
st.title("Chatbot")
msg = st.chat_input("Start conversation")
if msg:
    outmsg = msg
    if mode == "Lower":
        outmsg = msg.lower()
    elif mode == "Upper":
        outmsg = msg.upper()
    elif mode == "Toggle":
        outmsg = msg.swapcase() 
        
    st.session_state.messages.append(msg)
    st.session_state.messages.append(outmsg)
    
    msglist = st.session_state.messages
    for idx,message in enumerate(msglist):
        role = "human" if idx%2 == 0 else "Assistant"
        with st.chat_message(role):
            st.write(message)