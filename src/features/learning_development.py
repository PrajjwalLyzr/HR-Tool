import streamlit as st
from PIL import Image
from hrtools import Development, HelperTool


def LearningDevelopment(OPENAI_API_KEY, LYZR_X_KEY):
    image = Image.open("./src/logo/Lyzr_Logo-white.png")
    st.image(image, width=150)
    st.title("Learning & Development")
    st.markdown("##### Click any of the button to use that respective tool!")
    try:
        learningDevelopment = Development(LyzrKey=LYZR_X_KEY, APIKey=OPENAI_API_KEY)
        mailSender = HelperTool(LyzrKey=LYZR_X_KEY, APIKey=OPENAI_API_KEY)

        if 'active_tool' not in st.session_state:
            st.session_state.active_tool = None
        
        # Buttons for each tool
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Personalized Learning Pathways'):
                st.session_state.active_tool = "Personalized Learning Pathways"
        with col2:
            if st.button('Content Creation'):
                st.session_state.active_tool = "Content Creation"
        
        # Display the relevant UI based on the active tool
        if st.session_state.active_tool == "Personalized Learning Pathways":
            st.markdown("#### This tool helps you recommend personalized training modules based on inputs such as `Employee Information`, `Career Goals`, `Current Skills`, `Skill Gaps`, `Preferred Learning Style`, and `Time Frame`.")
            
            col1, col2 = st.columns(2)        
            with col1:
                employee_info = st.text_area(label='Employee Information', placeholder="Name, role, department, and current position.", height=100)
                carrer_goal = st.text_area(label='Career Goal', placeholder="Short-term and long-term professional aspirations of the employee.", height=100)
                
            with col2:
                skill_gap = st.text_area(label="Skill Gap", placeholder="Areas where the employee needs improvement or additional training.", height=100)
                current_skills = st.text_area(label="Current Skills", placeholder="A detailed list of the employee’s existing skills and competencies.", height=100)
                
            prefered_learning_style = st.text_input(label='Prefered Learning Style', placeholder="Information on how the employee prefers to learn (e.g., online courses, workshops, hands-on training")
            time_frame = st.text_area(label='Time Frame', placeholder="The period within which the employee wants to achieve these career goals.", height=100)
            email = st.text_input(label='Provide Recievers Mail')

            if (employee_info and carrer_goal and skill_gap and current_skills and prefered_learning_style and time_frame and email):
                if st.button('Generate Path'):
                    with st.spinner('Generating Learning Path...'):
                        learning = learningDevelopment.PersonalizedLearningPathways(employeeInfo=employee_info,
                                                                                   carrerGoal=carrer_goal,
                                                                                   skillGap=skill_gap,
                                                                                   currentSkills=current_skills,
                                                                                   preferedLearningStyle=prefered_learning_style)
                        

                        
                        if learning:
                            # Store the generated feedback in session state
                            st.session_state.learning = learning
                            st.success("Learning path generated successfully! You can now view or send the path.")

                # Check if feedback has been generated and stored in session state
                if 'learning' in st.session_state:
                    learning = st.session_state.learning

                    if st.button('See Learning Path'):
                        st.write(learning)

                    if st.button('Send Mail'):
                        with st.spinner('Sending the Mail...'):
                            response = mailSender.MailSender(mail=learning, mail_id=email)
                            if response:
                                st.write(response)
            

        elif st.session_state.active_tool == "Content Creation":
            st.markdown("#### This will help you create engaging and effective training materials by processing `Training Objectives`, `Target Audience`, `Core Content`, `Interactive Elements`, `Assessment Criteria`, `Design Preferences`, and `Time Frame` to develop interactive materials and quizzes.")
            
            col6, col7 = st.columns(2)
            with col6:
                training_objective = st.text_area(label="Training Objectives", placeholder="Clear goals and learning outcomes for the training session.", height=100)
                target_audience = st.text_area(label="Target Audience", placeholder="Information about the learners, including their roles, experience levels, and learning preferences.", height=100)
                interactive_element = st.text_area(label="Interactive Element", placeholder="Types of interactions to include, such as quizzes, simulations, or case studies.", height=100)           
            with col7:
                assesment_criteria = st.text_area(label="Assesment Criteria", placeholder="The standards or metrics to evaluate learner understanding and engagement.", height=100)
                core_content = st.text_area(label="Core Content", placeholder="The key concepts, skills, or knowledge that need to be conveyed in the training materials.", height=100)
                design_preference = st.text_area(label="Design Preference", placeholder="Any specific preferences for the format, style, or medium of the training content (e.g., video, text, interactive modules).", height=100)

            
            time_frame = st.text_area(label='Time Frame', placeholder="The duration or timeline for completing the training and associated assessments.", height=100)
            # email = st.text_input(label="Provide Recievers Mail ")

            if (training_objective and target_audience and assesment_criteria and core_content and design_preference and time_frame and interactive_element):
                if st.button('Get Content'):
                    with st.spinner('Getting Content...'):
                        content = learningDevelopment.ContentCreation(trainingObjective=training_objective,
                                                                      targetAudience=target_audience,
                                                                      coreContent=core_content,
                                                                      interactiveElements=interactive_element,
                                                                      assesmentCriteria=assesment_criteria,
                                                                      designPreference=design_preference,
                                                                      timeFrame=time_frame)
                        
                        if content:
                            st.session_state.content = content
                            st.success("Content generated successfully! You can now view or send the Content.")

                if 'content' in st.session_state:
                    content = st.session_state.content

                    if st.button('See Content'):
                        st.write(content)

                    # if st.button('Send Mail'):
                    #     with st.spinner('Sending the Mail...'):
                    #         response = mailSender.MailSender(mail=content, mail_id=email)
                    #         if response:
                    #             st.write(response)

   
    except Exception as e:
        st.error(f"Error:{str(e)}")