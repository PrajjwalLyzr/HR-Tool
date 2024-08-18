import streamlit as st
from PIL import Image

def EmployeeEngagement():
    image = Image.open("./logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("Employee Engagement")
    st.write("**Survey Analysis:** Analyze employee survey responses, identify trends, and suggest actionable insights.")
    st.write("**Recognition Programs:** Generate personalized recognition messages or rewards based on employee achievements.")
