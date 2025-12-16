import streamlit as st

#registration form

with st.form(key = "reg form"):
    st.header("Registration Form")
    First_name = st.text_input(key="fname",label="First name")
    last_name = st.text_input(key="lname",label="Last name")
    age = st.slider("Age",10,100,25,1)
    addr = st.text_area("Address")
    submit_btn = st.form_submit_button("Submit",type="primary")
    
    if submit_btn:
        err_message = ""
        is_error = False
        if not First_name:
            is_error = True
            err_message = "First name is required"
        if not last_name:
            is_error = True
            err_message = "Last name is required"
        if not addr:
            is_error = True
            err_message ="Address is required"
        if is_error:
            st.error(err_message)
        else:
            message = f"Successfully registered: {st.session_state['fname']} {st.session_state['lname']}.\nAge: {age}. Living at {addr}"
            st.success(message)