import streamlit as st

page = st.sidebar.radio("Go to", ["Home", "Profile", "Settings"])
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Home Page!")
elif page == "Profile":
    st.title("👤 Profile Page")
    st.write("This is your Profile Page.")
elif page == "Settings":
    st.title("⚙️ Settings Page")
    st.write("Adjust your settings here.")