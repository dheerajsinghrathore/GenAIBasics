import streamlit as st
obj=st.date_input("Select date")
st.write("Day:",obj.day)
st.write("Month:",obj.month)
st.write("Year:",obj.year)
