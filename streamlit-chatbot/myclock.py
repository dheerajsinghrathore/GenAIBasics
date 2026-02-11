import streamlit as st
from datetime import datetime
import time

# Create a placeholder for the clock
clock_placeholder = st.empty()

while True:
    curr_time = datetime.now()
    # Update the placeholder with a single string (not multiple arguments)
    clock_placeholder.write(f"Current Time: {curr_time.strftime('%H:%M:%S')}")
    time.sleep(1)
    st.rerun()