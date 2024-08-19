import streamlit as st
from PIL import Image
from features import ComplianceReporting, RecruitmentApplicantTracking
from features import LearningDevelopment, PerformanceManagement
from features import OnboardingEmployee, EmployeeEngagement
from features import HomePage
from utils import utils
from dotenv import load_dotenv; load_dotenv()

utils.page_config()
utils.style_app()

image = "./src/logo/HR-Management-Tool-banner-lyzrAI.png"
st.sidebar.image(image=image)
utils.social_media(justify="space-evenly")
st.sidebar.markdown("---")

# st.sidebar.title("HR Management by Lyzr.ai")
# Initialize session state for active page
if 'active_page' not in st.session_state:
    st.session_state.active_page = "Home"

# Function to handle button clicks
def set_page(page_name):
    st.session_state.active_page = page_name

# Sidebar title and Home button
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
    if st.button("Engagement", key="engagement_button"):
        set_page("Employee Engagement")

# Place buttons in the second column
with col2:
    if st.button("Onboarding", key="onboarding_button"):
        set_page("Onboarding")
    if st.button("Development", key="learning_button"):
        set_page("Learning & Development")
    if st.button("Reporting", key="compliance_button"):
        set_page("Compliance & Reporting")

# Navigate to respective pages based on session state
if st.session_state.active_page == "Home":
    HomePage()
elif st.session_state.active_page == "Recruitment & Applicant Tracking":
    RecruitmentApplicantTracking()
elif st.session_state.active_page == "Onboarding":
    OnboardingEmployee()
elif st.session_state.active_page == "Performance Management":
    PerformanceManagement()
elif st.session_state.active_page == "Learning & Development":
    LearningDevelopment()
elif st.session_state.active_page == "Employee Engagement":
    EmployeeEngagement()
elif st.session_state.active_page == "Compliance & Reporting":
    ComplianceReporting()



#------------
# page = st.sidebar.radio("Features", ["Home", 
#                                   "Recruitment & Applicant Tracking", 
#                                   "Onboarding", 
#                                   "Performance Management", 
#                                   "Learning & Development", 
#                                   "Employee Engagement", 
#                                   "Compliance & Reporting"])

# # Home page content
# if page == "Home":
#     HomePage()

# # Navigate to respective pages based on selection
# if page == "Recruitment & Applicant Tracking":
#     RecruitmentApplicantTracking()

# elif page == "Onboarding":
#     OnboardingEmployee()

# elif page == "Performance Management":
#     PerformanceManagement()

# elif page == "Learning & Development":
#     LearningDevelopment()

# elif page == "Employee Engagement":
#     EmployeeEngagement()

# elif page == "Compliance & Reporting":
#     ComplianceReporting()

# sidebar
st.markdown('---')
st.sidebar.markdown('---')
utils.template_end()
# utils.social_media()


# Footer
utils.footer()


    


