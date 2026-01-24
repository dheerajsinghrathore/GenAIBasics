import streamlit as st
age=st.number_input("Enter your age:",min_value=1.0,max_value=140.0,step=1.5)
if age:
    st.write("Age:",age)