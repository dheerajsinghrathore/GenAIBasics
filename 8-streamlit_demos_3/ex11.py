import streamlit as st
age=st.number_input("Enter your age:",min_value=1,max_value=140)
if age:
    st.write("Age:",age)