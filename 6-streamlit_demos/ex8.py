import streamlit as st

class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def __str__(self):
        return f"Roll:{self.roll},Name:{self.name}"
s=Student(101,"Piyush")
st.write(s)