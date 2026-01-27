import streamlit as st
time=st.time_input("Select time")
st.write("Selected hour:",time.hour)
st.write("Selected min:",time.minute)
st.write("Selected sec:",time.second)


