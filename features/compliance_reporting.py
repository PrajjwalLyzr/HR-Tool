import streamlit as st
from PIL import Image


def ComplianceReporting():
    image = Image.open("./logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("Compliance & Reporting")
    st.write("**Policy Explanation:** Generate clear and concise explanations of HR policies and legal requirements.")
    st.write("**Report Summarization:** Summarize HR data and create reports that highlight key findings.")
