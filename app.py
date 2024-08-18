import streamlit as st
from features import ComplianceReporting, RecruitmentApplicantTracking
from features import LearningDevelopment, PerformanceManagement
from features import Onboarding, EmployeeEngagement
from features import HomePage
from PIL import Image
from utils import utils
import os
from dotenv import load_dotenv; load_dotenv()

utils.page_config()
utils.style_app()


st.sidebar.title("HR Management")
page = st.sidebar.radio("Features", ["Home", 
                                  "Recruitment & Applicant Tracking", 
                                  "Onboarding", 
                                  "Performance Management", 
                                  "Learning & Development", 
                                  "Employee Engagement", 
                                  "Compliance & Reporting"])

# Home page content
if page == "Home":
    HomePage()

# Navigate to respective pages based on selection
if page == "Recruitment & Applicant Tracking":
    RecruitmentApplicantTracking()

elif page == "Onboarding":
    Onboarding()

elif page == "Performance Management":
    PerformanceManagement()

elif page == "Learning & Development":
    LearningDevelopment()

elif page == "Employee Engagement":
    EmployeeEngagement()

elif page == "Compliance & Reporting":
    ComplianceReporting()

# sidebar
st.markdown('---')
utils.template_end()
utils.social_media()


# Footer
utils.footer()




# if __name__ == "__main__":
#     if (APIKey and LyzrAPIKey) != "":
#         job_description()
    


