import streamlit as st
import datetime

st.title("📆 Appointment Booking & Cost Calculator")
if "bookings" not in st.session_state:
    st.session_state.bookings=[]
    
sel_date=st.date_input("Select appointment date")
sel_time=st.time_input("Select appointment time",value=datetime.time(10,0))
sel_service=st.selectbox("Select service",["Consultation","Premium","Emergency"])
sel_duration=st.number_input("Duration( in hours)",min_value=1,max_value=8,step=1)

prices={"Consultation":500,"Premium":1000,"Emergency":1500}
cost=prices[sel_service]*sel_duration
st.info(f"💰 Estimated Cost : ₹{cost}")
clicked=st.button("Confirm Booking")

if clicked:
    booking={
        "date":sel_date,
        "time":sel_time,
        "service":sel_service,
        "duration":sel_duration,
        "cost":cost
    }
    st.session_state.bookings.append(booking)
    st.success("✅ Booking Confirmed")
st.subheader("📅Your Bookings")
if st.session_state.bookings:
    for i,b in enumerate(st.session_state.bookings,start=1):
        st.write(f"{i}. {b['date']} at {b['time']} | " 
                 f"{b['service']} | "
                 f"{b['duration']} h| "
                 f"₹:{b['cost']}")
else:
    st.write("No bookings yet")
    

    
    