import streamlit as st

st.title("Sidebar Settings")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, step=1)
st.write(f"Hello {name}")
st.write(f"Your age is {age}")