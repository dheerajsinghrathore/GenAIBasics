import streamlit as st
name=st.text_input("Enter your name:")
if name:
    st.session_state.name=name
if "name" in st.session_state:
        st.write("Hello",st.session_state.name)
    