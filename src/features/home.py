import streamlit as st
from utils import utils
from PIL import Image

def HomePage():
    path = 'Keys.txt'
    utils.delete_keys_file(file_path=path)    
    image = Image.open("./src/logo/lyzr-logo.png")
    st.image(image, width=150)
    st.title("HR Management System")
    st.markdown("HR Management System powered by Lyzr.ai, a comprehensive solution designed to streamline and enhance human resource processes using advanced AI capabilities.")

    APIKey = st.text_input(label="API Key",placeholder='OpenAI API Key', type="password")
    LyzrAPIKey = st.text_input(label="Lyzr API Key", placeholder='X-API-KEY', type='password')
    if APIKey and LyzrAPIKey:       
        if st.button('Submit Keys'):
            with open(path, 'w') as f:
                f.write(f"APIKey: {APIKey}\n")
                f.write(f"LyzrAPIKey: {LyzrAPIKey}\n")
                st.success("Keys have been saved successfully!")
                          
    else:
        st.info("Please ensure both APIKey and LyzrAPIKey are provided.")
        utils.delete_keys_file(file_path=path)  # Delete the file if keys are not provided

    if st.button('Delete Keys'):
            utils.delete_keys_file(file_path=path)
            st.warning('Keys have been deleted!!')        
    

    st.markdown("---")
    st.subheader('Tools')
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('Resume Parsing & Matching')
        st.write('Job Description Creation')
        st.write('Document Generation')
    
    with col2:
        st.write('Feedback Generation')
        st.write('Sentiment Analysis')
        st.write('Automated Onboarding Assistance')