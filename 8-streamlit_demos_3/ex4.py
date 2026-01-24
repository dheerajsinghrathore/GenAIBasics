import streamlit as st
name=st.text_input("Enter your name",placeholder="guest")
if name:
    st.write("Hello",name)

