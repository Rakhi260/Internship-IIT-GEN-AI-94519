import streamlit as st
st.title("The Jaggery comapany")
    
def show_aboutus_page():
    st.header("About Us")
    st.write("At our Jaggery company , we are dedicated to preserving the authentic taste and goodness of traditional jaggery. Sourced directly from carefully selected sugarcane farms, our jaggery is produced using time-honored methods that retain its natural nutrients, rich flavor, and golden color.")
    st.write("We believe in purity, quality, and sustainability. Our process avoids harmful chemicals and artificial additives, ensuring that every block of jaggery is wholesome, safe, and packed with natural energy. By working closely with local farmers, we support rural livelihoods while delivering a product you can trust.")
    st.write("Whether used in everyday cooking or festive preparations, [Your Company Name] jaggery brings health, tradition, and taste together—just the way nature intended.")
    
def show_home_page():
    st.header("Home page")
    st.write("At our jaggery company, we craft 100% pure, chemical-free jaggery using traditional methods and the finest sugarcane. Our jaggery retains its natural minerals, rich taste, and wholesome goodness—making it a healthier alternative to refined sugar.")
    st.write("We work closely with local farmers to ensure quality at every step, from farm to kitchen. Whether for daily use or festive cooking, our jaggery brings authentic sweetness, nutrition, and tradition to your home.")
    
    if st.button("Shop now",type="primary"):
       st.toast("sdre")
    st.button("Learn more",type="primary")
    st.button("Our Products",type="primary")
    
    
def why_Choose_Us():
    st.header("Why Choose us")
    st.write("🌿 Why Choose Us At our Company, we don’t just make jaggery—we preserve tradition, purity, and trust in every batch.")
    st.write("🌱 100% Natural & Chemical-Free Our jaggery is made without chemicals, artificial colors, or preservatives, ensuring natural sweetness and authentic taste.")
    st.write("🔥 Traditional Production Methods We follow time-honored techniques that retain essential minerals, rich aroma, and the true flavor of sugarcane.")
    st.write("🌾 Ethically Sourced We work directly with local farmers to ensure fair trade practices and sustainable sourcing.")
    st.write("💚 Healthier Alternative Our jaggery is rich in iron, calcium, and other essential minerals, making it a healthier choice than refined sugar.")

def show_conatact_us():
    st.header("Contact Us")
    st.markdown("jaggery company")
    st.write("Sangli")

if 'page' in st.session_state:
    st.session_state.page = "About Us"
    
with st.sidebar:
    if st.button("About Us", width="stretch"):
        st.session_state.page = "About Us"
    if st.button("Home Page", width="stretch"):
        st.session_state.page = "Home Page"
    if st.button("Why Choose Us", width="stretch"):
        st.session_state.page = "Why Choose Us"
    if st.button("Contact Us", width="stretch"):
        st.session_state.page = "Contact Us"
    
    
    
if st.session_state.get("page") == "About Us":
     show_aboutus_page()
elif st.session_state.get("page") == "Home Page":
    show_home_page()
elif st.session_state.get("page") == "Why Choose Us":
    why_Choose_Us()
elif st.session_state.get("page") == "Contact Us":
    show_conatact_us()
    
