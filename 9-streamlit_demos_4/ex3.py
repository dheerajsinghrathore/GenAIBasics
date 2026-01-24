import streamlit as st
count=0
clicked=st.button("Click Me")
if clicked:
    count+=1
st.write("Count:",count)