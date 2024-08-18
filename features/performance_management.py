import streamlit as st
from PIL import Image


def PerformanceManagement():
    image = Image.open("./logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("Performance Management")
    st.write("**Feedback Generation:** Assist managers in crafting constructive and personalized performance reviews.")
    st.write("**Goal Setting:** Facilitate the creation of professional goals for employees and managers.")
    st.write("**Sentiment Analysis:** Analyze feedback tone to gauge employee satisfaction and highlight areas needing attention.")
