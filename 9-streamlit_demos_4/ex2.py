import streamlit as st
num1=st.number_input("Enter first number:")
num2=st.number_input("Enter secnd number: ")
clicked=st.button("Add")
if clicked:
    st.write("Sum is",num1+num2)