import streamlit as st
agree=st.checkbox("I agree to terms")
if agree:
    st.info("Thank you for agreeing to us")