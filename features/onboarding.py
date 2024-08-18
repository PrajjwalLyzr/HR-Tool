import streamlit as st
from PIL import Image

def Onboarding():
    image = Image.open("./logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("Onboarding")
    st.write("**Automated Onboarding Assistance:** Provide new hires with answers to FAQs and guide them through the onboarding process.")
    st.write("**Document Generation:** Create personalized onboarding documents, including welcome letters and training schedules.")
