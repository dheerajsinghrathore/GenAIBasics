import streamlit as st
name=st.text_input("Enter your name",value="guest")
if name:
    st.write("Hello",name)

