import streamlit as st
from utils import utils
from PIL import Image
from lyzragent import LyzrAgent



def HomePage():
    path = 'Keys.txt'
    utils.delete_keys_file(file_path=path)    
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

    # APIKey = st.text_input(label="API Key",placeholder='OpenAI API Key', type="password")
    # LyzrAPIKey = st.text_input(label="Lyzr API Key", placeholder='X-API-KEY', type='password')
    # if APIKey and LyzrAPIKey:  
    #     col1, col2 = st.columns(2)
    #     with col1:     
    #         if st.button('Submit Keys'):
    #             agent = LyzrAgent(x_api_key=LyzrAPIKey, llm_api_key=APIKey)
    #             response = agent.create_environment(
    #                     name="Test",
    #                     features=[{
    #                         "type": "TOOL_CALLING",
    #                         "config": {"max_tries": 1},
    #                         "priority": 0
    #                     }],
    #                     tools=["perplexity_search"])
                
    #             if response is not None:
    #                 with open(path, 'w') as f:
    #                     f.write(f"APIKey: {APIKey}\n")
    #                     f.write(f"LyzrAPIKey: {LyzrAPIKey}\n")
    #                     st.success("Keys have been saved successfully!")

    #     with col2:
    #         if st.button('Delete Keys'):
    #             utils.delete_keys_file(file_path=path)
    #             st.warning('Keys have been deleted!!')
                          
    # else:
    #     st.info("Please ensure both APIKey and LyzrAPIKey are provided.")
    #     utils.delete_keys_file(file_path=path)  # Delete the file if keys are not provided
          
    # st.markdown("---")
    # st.subheader('Tools')
    # col1, col2 = st.columns(2)
    
    # with col1:
    #     st.write('Resume Parsing & Matching')
    #     st.write('Job Description Creation')
    #     st.write('Document Generation')
    
    # with col2:
    #     st.write('Feedback Generation')
    #     st.write('Sentiment Analysis')
    #     st.write('Automated Onboarding Assistance')