import streamlit as st
import datetime
time=st.time_input("Office opening time",value=datetime.time(9,0))
st.write("Selected hour:",time.hour)
st.write("Selected min:",time.minute)
st.write("Selected sec:",time.second)


