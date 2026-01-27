import streamlit as st
skills=st.multiselect("Select Your Skills",["Python","Java","AI","Web Dev"],default=["Python","Java"])
st.write("Selected Skills",skills)