import streamlit as st
empId=st.text_input("Enter your emp Id",max_chars=5)
if empId:
    st.write("Hello",empId)

