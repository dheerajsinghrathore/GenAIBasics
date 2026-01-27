import streamlit as st
obj=st.date_input("Select date")
st.write("Selected date:",obj.strftime("%d-%m-%Y"))