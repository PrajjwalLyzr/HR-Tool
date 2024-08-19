import streamlit as st
from PIL import Image
from hrtools import Onboarding

def OnboardingEmployee():
    image = Image.open("./src/logo/Lyzr_Logo-white.png")
    st.image(image, width=150)
    st.title("Onboarding")
    
    file = "Keys.txt"
    
    APIKey = None
    LyzrAPIKey = None
    
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('APIKey:'):
                    APIKey = line.split('APIKey:')[1].strip()
                elif line.startswith('LyzrAPIKey:'):
                    LyzrAPIKey = line.split('LyzrAPIKey:')[1].strip()
                    onboard = Onboarding(LyzrKey=LyzrAPIKey, APIKey=APIKey)

        # Initialize session state variables
        if 'active_tool' not in st.session_state:
            st.session_state.active_tool = None


        if 'generated_mail' not in st.session_state:
            st.session_state.generated_mail = None

        # Buttons for each tool
        col1, col2= st.columns(2)
        with col1:
            if st.button('Onboarding Assistant'):
                st.session_state.active_tool = "Onboarding Assistant"
        with col2:
            if st.button('Document Generator'):
                st.session_state.active_tool = "Document Generator"
        
        # Display the relevant UI based on the active tool
        if st.session_state.active_tool == "Onboarding Assistant":
            st.markdown("#### This tool will help you to create a mail having `Onboarding Procedure` and send that mail to new `Employee`")
            new_employee_mail = st.text_input(label='Proivde personal mail', placeholder='Paste their personal mail')
            new_professional_mail = st.text_input(label='Provide professional mail', placeholder='Write their new professional mail')
            new_temp_password = st.text_input(label='Provide temporary password', placeholder='Give the temporary password')

            if (new_employee_mail and new_professional_mail and new_temp_password):
                if st.button('Get Mail'):
                    with st.spinner('Generating the Mail...'):
                        st.session_state.generated_mail = onboard.OnboardingAssistance(
                            professional_mail=new_professional_mail,
                            temp_password=new_temp_password
                        )
                        st.write(st.session_state.generated_mail)

            if st.session_state.generated_mail:
                if st.button('Send Mail'):
                    with st.spinner('Sending the Mail...'):
                        mail_response = onboard.MailSender(
                            mail=st.session_state.generated_mail, 
                            mail_id=new_employee_mail
                        )
                        st.write(mail_response)
                        st.session_state.generated_mail = None
            else:
                st.info('Provide the necessary details')

        elif st.session_state.active_tool == "Document Generator":
            st.markdown("#### This will help you to create documents such as `Welcome Letter` or `Detaild Training Schedule`.")
            col3, col4 = st.columns(2)
            
            with col3:
                employeeName = st.text_input('Provide Employee Name', placeholder='Write their full name')
                employeeRole = st.text_input('Provide Employee Role', placeholder='Write down their role in company')

            with col4:
                employeeDepartment = st.text_input('Provide Employee Department', placeholder='Write their deparment, he/she will work under')
                employeeStartdate = st.date_input(label='Provide Employee Start Data')


            if (employeeName and employeeDepartment and employeeRole and employeeStartdate):
                if st.button('Generate'):
                    with st.spinner('Generating Documents...'):
                        docs = onboard.DocumentGeneration(
                            employee_name=employeeName,
                            employee_role=employeeRole,
                            employee_deptartment=employeeDepartment,
                            start_date=employeeStartdate)
                        
                        st.write(docs)

            else:
                st.warning('Please provide the necessary details')

    except FileNotFoundError:
        st.info('Please submit the APIKey and LyzrAPIKey on the Home Page')