import streamlit as st
from utils import utils
from PIL import Image
from lyzragent import LyzrAgent



def HomePage():
    path = 'Keys.txt'
    utils.delete_keys_file(file_path=path)  
    utils.remove_existing_files(directory="ResumeData")  
    image = Image.open("./src/logo/HR-Management-Tool-banner-lyzrAI.png")
    st.image(image)
    # st.title("HR Management System")
    st.markdown('---')
    st.markdown("HR Management System powered by [Lyzr.ai](https://www.lyzr.ai/), a comprehensive solution designed to streamline and enhance human resource processes using advanced AI capabilities.")

    
    # Key Features
    # st.write("## Key Features")
    st.write("# HR Tools")

    col1, col2 = st.columns(2)

    with col1:
        # Recruitment & Applicant Tracking
        st.write("""
        ## Recruitment
        - **Resume Parsing & Matching**
        - **Job Description Creation**
        - **Applier Details Extraction**
        """)

        # Onboarding
        st.write("""
        ## Onboarding
        - **Automated Assistance**
        - **Document Generation**
        """)
    
    with col2:
        # Performance Management
        st.write("""
        ## Performance 
        - **Feedback Generation**
        - **Goal Setting**
        - **Sentiment Analysis**
        """)

        # Learning & Development
        st.write("""
        ## Development
        - **Personalized Learning Pathways**
        - **Content Creation**
        """)