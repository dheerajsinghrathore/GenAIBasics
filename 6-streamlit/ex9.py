import streamlit as st

st.title("Hello, Dheeraj!")
st.header("Welcome to My Streamlit App")

name = "Dheeraj"
experience = 5
st.write(f"My name is {name} and I am {experience} years old.")
skills = ["Python", "Machine Learning", "Data Science"]
st.subheader("My Skills")
st.write(skills)
st.markdown("**Status:** 🟢")