import streamlit as st
from PIL import Image
from hrtools import Recruitment
from utils import utils
import PyPDF2
import os


def RecruitmentApplicantTracking(OPENAI_API_KEY, LYZR_X_KEY):
    resume_data = "ResumeData"
    os.makedirs(resume_data, exist_ok=True)
    utils.remove_existing_files(directory=resume_data)

    image = Image.open("./src/logo/Lyzr_Logo-white.png")
    st.image(image, width=150)
    st.title("Recruitment & Applicant Tracking")
    st.markdown("##### Click any of the button to use that respective tool!")

    try:
        recruit = Recruitment(LyzrKey=LYZR_X_KEY, APIKey=OPENAI_API_KEY)
        # Initialize session state variables
        if 'active_tool' not in st.session_state:
            st.session_state.active_tool = None
        
        # Buttons for each tool
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Get Job Description'):
                st.session_state.active_tool = "Get Job Description"
        with col2:
            if st.button('Resume Parsing'):
                st.session_state.active_tool = "Resume Parsing"
        with col3:
            if st.button('Get Appliers Details'):
                st.session_state.active_tool = "Get Appliers Details"

        
        # Display the relevant UI based on the active tool
        if st.session_state.active_tool == "Get Job Description":
            st.markdown("#### This tool will help you to create job description based on your basic input such as `Role`, `Skills`, `Experience`, and `Working Type`")
            job_brief = st.text_area(label="Job Brief", placeholder='Write about the job and their requirements', height=200)
            if job_brief:
                if st.button('Submit'):
                    with st.spinner('Getting Job Description...'):
                        description = recruit.JobDescriptionCreator(about_job=job_brief)
                        st.code(description)
                        # st.write(description)
            else:
                st.info('Please Provide the Job requirements or role')

        elif st.session_state.active_tool == "Resume Parsing":
            st.markdown("#### This will help you to match the candidate according to the Job description, just provide `Job Description` and `Resume`.")
            jd = st.text_area('Job description', placeholder='Upload JD')
            resume_file = st.file_uploader(label='Upload the resume', type=['pdf'])
            if resume_file and jd:
                utils.save_uploaded_file(directory=resume_data, uploaded_file=resume_file)
                pdf_content = ""
                file_name = utils.get_file_name(directory=resume_data)
                file_path = os.path.join(resume_data, file_name)
                try:
                    with open(file_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        for page in range(len(pdf_reader.pages)):
                            pdf_content += pdf_reader.pages[page].extract_text()
                    
                    if st.button('Match'):
                        with st.spinner('Parsing the Resume...'):
                            resume_response = recruit.ResumeMatching(resume_data=pdf_content, job_desc=jd)
                            st.write(resume_response)
                except FileNotFoundError:
                    st.warning(f"The file '{resume_file}' does not exist in the folder '{resume_data}'.")
            else:
                utils.remove_existing_files(directory=resume_data)
                st.info('Please upload job description and resume to proceed')

        elif st.session_state.active_tool == "Get Appliers Details":
            st.markdown("#### This will help you to extract key details or personal information such as `Name`, `Mail ID`, `Phone Number` from the given resume.")
            resume_file = st.file_uploader(label='Upload the resume', type=['pdf'])
            if resume_file:
                utils.save_uploaded_file(directory=resume_data, uploaded_file=resume_file)
                pdf_content = ""
                file_name = utils.get_file_name(directory=resume_data)
                file_path = os.path.join(resume_data, file_name)
                try:
                    with open(file_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        for page in range(len(pdf_reader.pages)):
                            pdf_content += pdf_reader.pages[page].extract_text()
                    
                    if st.button('Extract'):
                        with st.spinner('Getting the Applier Details...'):
                            details = recruit.GetAppliersDeatils(resume_data=pdf_content)
                            st.code(details)
                except FileNotFoundError:
                    st.warning(f"The file '{resume_file}' does not exist in the folder '{resume_data}'.")
            else:
                utils.remove_existing_files(directory=resume_data)
                st.info('Upload Resume to get the details')

    except Exception as e:
        st.error(f"Error:{str(e)}")


# ---------------------------

# def RecruitmentApplicantTracking():
#     resume_data = "ResumeData"
#     os.makedirs(resume_data, exist_ok=True)
#     utils.remove_existing_files(directory=resume_data)

#     image = Image.open("./src/logo/lyzr-logo.png")
#     st.image(image, width=150)
#     st.title("Recruitment & Applicant Tracking")

#     file = "Keys.txt"
    
#     APIKey = None
#     LyzrAPIKey = None
    
#     try:
#         with open(file, 'r') as f:
#             lines = f.readlines()
#             for line in lines:
#                 if line.startswith('APIKey:'):
#                     APIKey = line.split('APIKey:')[1].strip()
#                 elif line.startswith('LyzrAPIKey:'):
#                     LyzrAPIKey = line.split('LyzrAPIKey:')[1].strip()
#                     recruit = Recruitment(LyzrKey=LyzrAPIKey, APIKey=APIKey)
        

#         tool = st.radio("", ["Get Job Description", 
#                                   "Resume Parsing",
#                                   "Get Appliers Details"])
        
        
#         if tool == "Get Job Description":
#             st.markdown(" #### This tool will help you to create job description based on your basic input such as `Role`, `Skills`, `Experience`, and `Working Type`")
#             job_brief = st.text_area(label="Job Brief", placeholder='Write about the job and their requirements')
#             if job_brief != "":
#                 if st.button('Submit'):
#                     with st.spinner('Getting Job Description.......'):
#                         description = recruit.JobDescriptionCreator(about_job=job_brief)
#                         st.write(description)

#         elif tool == "Resume Parsing":
#             st.markdown(" #### This will help you to match the candiate according to the Job description, just provide `Job Description` and `Resume`.")
#             jd = st.text_area('Job description', placeholder='Upload JD')
#             resume_file = st.file_uploader(label='Upload the resume', type=['pdf'])
#             if (resume_file and jd) is not None:
#                 utils.save_uploaded_file(directory=resume_data, uploaded_file=resume_file)
#                 pdf_content = ""
#                 file_name = utils.get_file_name(directory=resume_data)
#                 file_path = os.path.join(resume_data, file_name)
#                 try:
#                     with open(file_path, 'rb') as file:
#                         pdf_reader = PyPDF2.PdfReader(file)
                        
#                         # Loop through all the pages and extract text
#                         for page in range(len(pdf_reader.pages)):
#                             pdf_content = pdf_content + pdf_reader.pages[page].extract_text()

#                     # st.write(pdf_content)
#                     if st.button('Match'):
#                         with st.spinner('Parsing the Resume.......'):
#                             resume_response = recruit.ResumeMatching(resume_data=pdf_content, job_desc=jd)
#                             st.write(resume_response)

#                 except FileNotFoundError:
#                     st.warning(f"The file '{resume_file}' does not exist in the folder '{resume_data}'.")

#             else:
#                 utils.remove_existing_files(directory=resume_data)
#                 st.info('Please upload job description and resume to proceed')

#         elif tool == "Get Appliers Details":
#             st.markdown(" #### This will help you to extract the key deatails or personal information such as `Name`, `Mail ID`, `Phone Number` from the given resume.")
#             resume_file = st.file_uploader(label='Upload the resume', type=['pdf'])
#             if (resume_file) is not None:
#                 utils.save_uploaded_file(directory=resume_data, uploaded_file=resume_file)
#                 pdf_content = ""
#                 file_name = utils.get_file_name(directory=resume_data)
#                 file_path = os.path.join(resume_data, file_name)
#                 try:
#                     with open(file_path, 'rb') as file:
#                         pdf_reader = PyPDF2.PdfReader(file)
                        
#                         # Loop through all the pages and extract text
#                         for page in range(len(pdf_reader.pages)):
#                             pdf_content = pdf_content + pdf_reader.pages[page].extract_text()

#                     # st.write(pdf_content)
#                     if st.button('Extract'):
#                         with st.spinner('Getting the Applier Deatils.......'):
#                             details = recruit.GetAppliersDeatils(resume_data=pdf_content)
#                             st.write(details)

#                 except FileNotFoundError:
#                     st.warning(f"The file '{resume_file}' does not exist in the folder '{resume_data}'.")
#             else:
#                 utils.remove_existing_files(directory=resume_data)
#                 st.info('Upload Resume to get the details')

#     except FileNotFoundError:
#         st.warning(f"The file '{file}' does not exist.")
#         st.info('Please Submit the APIKey and LyzrAPIKey on Home Page')


