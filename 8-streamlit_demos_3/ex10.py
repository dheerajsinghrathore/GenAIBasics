import streamlit as st
age=st.number_input("Enter your age:")
if age:
    st.write("Age:",age)