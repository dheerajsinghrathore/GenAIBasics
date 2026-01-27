import streamlit as st
msg=st.chat_input("What's in your mind ?")
if msg:
    st.write("You said:",msg)