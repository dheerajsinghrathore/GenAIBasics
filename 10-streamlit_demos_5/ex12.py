import streamlit as st
import datetime
obj=st.date_input("Select date",min_value=datetime.date(2020,1,1),max_value=datetime.date(2026,12,31))
st.write("Day:",obj.day)
st.write("Month:",obj.month)
st.write("Year:",obj.year)
