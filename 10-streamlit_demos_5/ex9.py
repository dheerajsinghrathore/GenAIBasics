import streamlit as st
obj=st.date_input("Select date")
print(type(obj))
st.write("Selected date:",obj)