import streamlit as st
from datetime import date, time  # date is calss and time is class

st.title("Booking Application")
with st.form("booking_form"):
    name = st.text_input("Enter your name")
    service = st.selectbox("Select service", ["Hair cut", "Therapy Session", "Facial"])
    booking_date = st.date_input("Select booking date", min_value=date.today())
    booking_time = st.time_input("Select booking time", value=time(10, 0))
    agree = st.checkbox("I agree to the terms and conditions")
    submit_button = st.form_submit_button("Book Now")

if submit_button:
    if not agree:
        st.error("You must agree to the terms and conditions to proceed.")
    else:
        st.success(
            f"Thank you {name}! Your {service} is booked for {booking_date} at {booking_time}."
        )
