import streamlit as st
feedback=st.text_area("Your views about us:",height=300)
if feedback:
    st.write("You wrote:")
    st.write(feedback)