import streamlit as st
skills=st.multiselect("Select Your Skills",["Python","Java","AI","Web Dev"])
st.write("Selected Skills",skills)