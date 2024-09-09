import streamlit as st
import os
from features import RecruitmentApplicantTracking
from features import LearningDevelopment
from features import PerformanceManagement
from features import OnboardingEmployee
from features import HomePage
from utils import utils
from dotenv import load_dotenv; load_dotenv()

utils.page_config()
utils.style_app()


openai_api_key = os.getenv('OPENAI_API_KEY')
lyzr_x_key = os.getenv('X_API_Key')

image = "./src/logo/HR-Management-Tool-banner-lyzrAI.png"
st.sidebar.image(image=image)
utils.social_media(justify="space-evenly")
st.sidebar.markdown("---")

# Initialize session state for active page
if 'active_page' not in st.session_state:
    st.session_state.active_page = "Home"

# Function to handle button clicks
def set_page(page_name):
    st.session_state.active_page = page_name

if st.sidebar.button("Home", key="home_button"):
    set_page("Home")


st.sidebar.subheader("HR Features")
# Create two columns for the buttons
col1, col2 = st.sidebar.columns(2, gap="small")  # Adding a small gap between columns


# Place buttons in the first column
with col1:
    if st.button("Recruitment", key="recruitment_button"):
        set_page("Recruitment & Applicant Tracking")
    if st.button("Performance", key="performance_button"):
        set_page("Performance Management")
   
# Place buttons in the second column
with col2:
    if st.button("Onboarding", key="onboarding_button"):
        set_page("Onboarding")
    if st.button("Development", key="learning_button"):
        set_page("Learning & Development")
   
# Navigate to respective pages based on session state
if st.session_state.active_page == "Home":
    HomePage()
elif st.session_state.active_page == "Recruitment & Applicant Tracking":
    RecruitmentApplicantTracking(OPENAI_API_KEY=openai_api_key, LYZR_X_KEY=lyzr_x_key)
elif st.session_state.active_page == "Onboarding":
    OnboardingEmployee(OPENAI_API_KEY=openai_api_key, LYZR_X_KEY=lyzr_x_key)
elif st.session_state.active_page == "Performance Management":
    PerformanceManagement(OPENAI_API_KEY=openai_api_key, LYZR_X_KEY=lyzr_x_key)
elif st.session_state.active_page == "Learning & Development":
    LearningDevelopment(OPENAI_API_KEY=openai_api_key, LYZR_X_KEY=lyzr_x_key)


# sidebar
st.markdown('---')
st.sidebar.markdown('---')
utils.template_end()


# Footer
utils.footer()


    


