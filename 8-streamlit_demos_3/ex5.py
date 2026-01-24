import streamlit as st
name=st.text_input("Enter your password",type="password")
if name:
    st.write("Hello",name)

