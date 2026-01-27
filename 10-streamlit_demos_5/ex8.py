import streamlit as st
file=st.file_uploader("Upload an image",type=["jpg","png"])
if file:
    st.image(file)