import streamlit as st
course=st.selectbox("Select a course",["--Select--","Python","Java","AI","Web Dev"])
if course !="--Select--":
    st.write("You selected:",course)
