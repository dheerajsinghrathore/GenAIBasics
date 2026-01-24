import streamlit as st
st.title("Emp Management System")
st.header("Employee Details")
name="Amit"
expr=25
st.write("Emp Name",name)
st.write("Experience",expr)
skills=["Python","Spring Boot","AI"]
st.subheader("Skills")
st.write(skills)
st.markdown("**Status:** 🔴 Active" )