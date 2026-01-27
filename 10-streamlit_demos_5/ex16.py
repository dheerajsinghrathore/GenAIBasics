import streamlit as st
import datetime

st.title("📆 Appointment Booking & Cost Calculator")
sel_date=st.date_input("Select appointment date")
sel_time=st.time_input("Select appointment time",value=datetime.time(10,0))
sel_service=st.selectbox("Select service",["Consultation","Premium","Emergency"])
sel_duration=st.number_input("Duration( in hours)",min_value=1,max_value=8,step=1)

prices={"Consultation":500,"Premium":1000,"Emergency":1500}
cost=prices[sel_service]*sel_duration
st.info(f"💰 Estimated Cost : ₹{cost}")
clicked=st.button("Confirm Booking")
if clicked:
    st.success("✅ Booking Confirmed")
    st.write("🧮 Date:",sel_date)
    st.write("⏱️ Time:",sel_time)
    st.write("🔥Service:",sel_service)
    st.write("⌛Duration:",sel_duration)
    st.write("💰Total Cost: ₹",cost)
    
    
    