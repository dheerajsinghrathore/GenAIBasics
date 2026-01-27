import streamlit as st
course=st.selectbox("Select a course",["Python","Java","AI","Web Dev"])
st.write("You selected:",course)
