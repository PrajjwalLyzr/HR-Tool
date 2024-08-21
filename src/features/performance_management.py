import streamlit as st
from PIL import Image
from hrtools import Performance, HelperTool


def PerformanceManagement(OPENAI_API_KEY, LYZR_X_KEY):
    image = Image.open("./src/logo/Lyzr_Logo-white.png")
    st.image(image, width=150)
    st.title("Performance Management")
    st.markdown("##### Click any of the button to use that respective tool!")
    # file = "Keys.txt"
    
    # APIKey = None
    # LyzrAPIKey = None
    
    # try:
    #     with open(file, 'r') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             if line.startswith('APIKey:'):
    #                 APIKey = line.split('APIKey:')[1].strip()
    #             elif line.startswith('LyzrAPIKey:'):
    #                 LyzrAPIKey = line.split('LyzrAPIKey:')[1].strip()
    #                 performaceManagement = Performance(LyzrKey=LyzrAPIKey, APIKey=APIKey)
    try:
        performaceManagement = Performance(LyzrKey=LYZR_X_KEY, APIKey=OPENAI_API_KEY)
        mail = HelperTool(LyzrKey=LYZR_X_KEY, APIKey=OPENAI_API_KEY)
        # Initialize session state variables
        if 'active_tool' not in st.session_state:
            st.session_state.active_tool = None
        
        # Buttons for each tool
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Feedback Generation'):
                st.session_state.active_tool = "Feedback Generation"
        with col2:
            if st.button('Goal Setting'):
                st.session_state.active_tool = "Goal Setting"
        with col3:
            if st.button('Sentiment Analysis'):
                st.session_state.active_tool = "Sentiment Analysis"
        
        # Display the relevant UI based on the active tool
        if st.session_state.active_tool == "Feedback Generation":
            st.markdown("#### This tool helps you generate constructive and personalized performance reviews based on inputs such as `Employee Information`, `Performance Metrics`, `Manager's Notes`, and `Feedback Focus Areas`.")
            col1, col2 = st.columns(2)
            with col1:
                employee_info = st.text_area(label='Employee Information', placeholder="Name, role, department, tenure, and past performance reviews.", height=100)
                performance_metrics = st.text_area(label='Performance Metrics', placeholder="Key performance indicators (KPIs), targets, and the employee's actual performance against those targets.", height=100)
            with col2:
                company_values = st.text_area(label="Company Values", placeholder="Core values, goals, and competencies that the feedback should align with.", height=100)
                feedback_focus_areas = st.text_area(label='Feedback Focus Areas', placeholder="Areas to emphasize, such as teamwork, innovation, or technical skills.", height=100)
                
            manager_notes = st.text_area(label='Manager Notes', placeholder="Observations, comments, and examples of the employee's work behavior, achievements, and areas for improvement.", height=100)
            desired_tone = st.text_input(label="Desired Tone", placeholder="Indication of whether the feedback should be formal, encouraging, or neutral.")
            email = st.text_input(label='Provide Recievers Mail')

            if (employee_info and performance_metrics and company_values and feedback_focus_areas and manager_notes and desired_tone and email):
                if st.button('Generate Feedback'):
                    with st.spinner('Generating Employee Feedback...'):
                        feedback = performaceManagement.FeedbackGeneration(employeeInfo=employee_info,
                                                                        performanceMetrics=performance_metrics,
                                                                        companyValues=company_values,
                                                                        sepcificFeedbackFocusAreas=feedback_focus_areas,
                                                                        managersNote=manager_notes,
                                                                        desiredTone=desired_tone)
                        
                        if feedback:
                            # Store the generated feedback in session state
                            st.session_state.feedback = feedback
                            st.success("Feedback generated successfully! You can now view or send the feedback.")

                # Check if feedback has been generated and stored in session state
                if 'feedback' in st.session_state:
                    feedback = st.session_state.feedback

                    if st.button('See Feedback'):
                        st.write(feedback)

                    if st.button('Send Mail'):
                        with st.spinner('Sending the Mail...'):
                            # mail = HelperTool(LyzrKey=LyzrAPIKey, APIKey=APIKey)
                            response = mail.MailSender(mail=feedback, mail_id=email)
                            if response:
                                st.write(response)
                
            else:
                st.info('Please Provide Details')

        elif st.session_state.active_tool == "Goal Setting":
            st.markdown("#### This tool helps you create professional goals for employees and managers by using inputs like `Employee/Manager Information`, `Company Objectives`, `Current Performance`, `Development Areas`, `Time Frame`, and `Desired Outcomes`.")

            col4, col5 = st.columns(2)
            with col4:
                employee_manager_info = st.text_area(label='Employee/Manager Information', placeholder="", height=100)
                company_objective = st.text_area(label='Company Objectives', placeholder="", height=100)
            with col5:
                current_perfromance = st.text_area(label="Currnet Performance", placeholder="", height=100)
                development_area = st.text_area(label="Development Area", placeholder="", height=100)

            desired_output = st.text_area(label="Desired Output", placeholder="", height=100)
            time_frame = st.text_input(label="Time Frame")  
            email = st.text_input(label='Provide Recievers Mail')


            if (employee_manager_info and company_objective and current_perfromance and development_area and time_frame and desired_output):
                if st.button('Generate Goal'):
                    with st.spinner('Generating Goal Setting...'):
                        goal = performaceManagement.GoalSetting(employeeManagerInfo=employee_manager_info,
                                                                companyObjective=company_objective,
                                                                currentPerformace=current_perfromance,
                                                                developmentArea=development_area,
                                                                timeFrame=time_frame,
                                                                desiredOutput=desired_output)
                        
                        if goal:
                            # Store the generated goal in session state
                            st.session_state.goal = goal
                            st.success("Goal generated successfully! You can now view or send the Goal.")

                if 'goal' in st.session_state:
                    goal = st.session_state.goal

                    if st.button('See Goal'):
                        st.write(goal)

                    if st.button('Send Mail'):
                        with st.spinner('Sending the Mail...'):
                            # mail = HelperTool(LyzrKey=LyzrAPIKey, APIKey=APIKey)
                            response = mail.MailSender(mail=goal, mail_id=email)
                            if response:
                                st.write(response)

            else:
                st.info('Please Provide Details')

        elif st.session_state.active_tool == "Sentiment Analysis":
            st.markdown("#### This will help you analyze employee satisfaction by processing `Employee Feedback Data`, `Contextual Information`, `Sentiment Categories`, `Keywords/Indicators`, and `Historical Data` to highlight areas needing attention.")
            
            col6, col7 = st.columns(2)
            with col6:
                employee_feedback = st.text_area(label="Employee Feedback Data", placeholder="Written feedback, comments, or survey responses from employees", height=100)
                contextual_info = st.text_area(label="Contextual Information", placeholder="Details such as the department, role, or specific event related to the feedback.", height=100)
            with col7:
                keyword_indicators = st.text_area(label="Keywords Indicators", placeholder="Specific words or phrases that might indicate satisfaction or dissatisfaction.", height=100)
                historical_data = st.text_area(label="Historical Data", placeholder="Previous feedback or sentiment analysis results to compare trends over time. (Optional)", height=100)

            email = st.text_input(label="Provide Recievers Mail ")

            if (employee_feedback and contextual_info and keyword_indicators and email):
                if st.button('Get Sentiment'):
                    with st.spinner('Getting Sentimental Analysis...'):
                        sentiment = performaceManagement.SentimentAnalysis(
                            employeeFeedbackData=employee_feedback,
                            contextualInformation=contextual_info,
                            keywordsIndicators=keyword_indicators)
                        
                        if sentiment:
                            # Store the generated goal in session state
                            st.session_state.sentiment = sentiment
                            st.success("Sentiment generated successfully! You can now view or send the Analysis.")

                if 'sentiment' in st.session_state:
                    sentiment = st.session_state.sentiment

                    if st.button('See sentiment analysis'):
                        st.write(sentiment)

                    if st.button('Send Mail'):
                        with st.spinner('Sending the Mail...'):
                            # mail = HelperTool(LyzrKey=LyzrAPIKey, APIKey=APIKey)
                            response = mail.MailSender(mail=sentiment, mail_id=email)
                            if response:
                                st.write(response)

            elif (employee_feedback and contextual_info and keyword_indicators and historical_data and email):
                if st.button('Get Sentiment'):
                    with st.spinner('Getting Sentimental Analysis...'):
                        sentiment = performaceManagement.SentimentAnalysis(
                            employeeFeedbackData=employee_feedback,
                            contextualInformation=contextual_info,
                            keywordsIndicators=keyword_indicators, 
                            historicalData=historical_data)
                        
                        if sentiment:
                            # Store the generated goal in session state
                            st.session_state.sentiment = sentiment
                            st.success("Sentiment generated successfully! You can now view or send the Analysis.")

                if 'sentiment' in st.session_state:
                    sentiment = st.session_state.sentiment

                    if st.button('See sentiment analysis'):
                        st.write(sentiment)

                    if st.button('Send Mail'):
                        with st.spinner('Sending the Mail...'):
                            # mail = HelperTool(LyzrKey=LyzrAPIKey, APIKey=APIKey)
                            response = mail.MailSender(mail=sentiment, mail_id=email)
                            if response:
                                st.write(response)

    # except FileNotFoundError:
    #     # st.warning(f"The file '{file}' does not exist.")
    #     st.info('Please submit the APIKey and LyzrAPIKey on the Home Page')
    except Exception as e:
        st.error(f"Error:{str(e)}")