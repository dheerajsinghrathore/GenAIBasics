import streamlit as st

st.metric("Temperature", "70 °F", delta="1.2 °F")
st.metric(label="Revenue", value="$1.2M", delta="-5%")
st.metric(label="Profit", value="$1.2M", delta="+5%")
