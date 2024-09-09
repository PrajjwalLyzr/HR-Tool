from lyzragent import LyzrAgent

class HRToolAgents:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

        self.Agent_Environment = self.Agent.create_environment(
            name="HR Tool",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["perplexity_search"])
        
    def JobDescriptionCreator(self, about_job):    
        """This function will call a agent to create job Description based on the given info"""    
        agent_prompt = """ Create a comprehensive job description based on the following job brief and requirements. Ensure it includes the job title, responsibilities, qualifications, skills, and any other relevant details to attract the right candidates. The job description should be clear, concise, and aligned with industry standards."""

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Job Description Creator")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="jobDescription-HRTool",
        message=about_job)


        return response['response']


    def ResumeMatching(self, resume_data, job_desc):
        """This function will a agent to match the resume based on job description"""
        agent_prompt =f""" Analyze the provided resume data:{resume_data} and compare it with the given job description: {job_desc}. Determine if the candidate is suitable for the role by assessing their qualifications, experience, skills, and any other relevant factors. Provide a clear conclusion on the candidate's suitability for the position, along with key reasons for your assessment. """

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Resume Parser")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="ResumeMatching-HRTool",
        message=f"Match the resume: {resume_data} with the given Job Decription: {job_desc}")


        return response['response']
    

    def GetAppliersDeatils(self, resume_data):
        """This function will calls the agent to get the appliers data from their resume"""
        agent_prompt =f""" Extract the key details from the provided resume data, including the candidate's name, contact information such as Email and Phone [!Important] Don't Extract other things apart from Given. Ensure the extracted data is well-organized and easy to reference."""

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Deatail Scrapper")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="GetAppliersDeatils-HRTool",
        message=resume_data)


        return response['response']
    
    def OnboardingAssistance(self, professional_mail, temp_password, sendername="Lyzr's AI Agent", designation='AI HR Head', sendermail='ai.agent@lyzr.ai'):
        """This function will call an agent to onoard the new hire"""
        agent_prompt = f"Compose an onboarding assistance email that welcomes the new employee and provides essential company information. Include the employee's professional email address:{professional_mail} and temporary password: {temp_password}. Provide clear instructions on how to log in, set up their account into google, and access important company resources. Ensure the tone is friendly, informative, and supportive. Include these details as sender: name:{sendername}, position in company:{designation} and contact information:{sendermail}"

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Onboarding Assistance")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="OnboardingAssistant-HRTool",
        message=f'Use these as the user Professional Email:{professional_mail} and Temporary Password: {temp_password}, sender datails are name:{sendername}, position:{designation} and contact information:{sendermail}')

        return response['response']
    

    def DocumentGeneration(self,employee_name, employee_role, employee_deptartment, start_date, companyname='AI Agents'):
        """This function call an agent to generate documents such as welcome letter and training schedule for new hire"""
        agent_prompt = f"""Generate personalized onboarding documents for a new employee:{employee_name}, including a welcome letter and a detailed training schedule. Tailor the content to reflect the employee's role:{employee_role}, department:{employee_deptartment}, and start date:{start_date}. Ensure the documents are professional, welcoming, and provide clear guidance on what the employee can expect during their onboarding process of company:{companyname}."""

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Document Generation")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="DocumentGeneration-HRTool",
        message=f'Use these details:{employee_name}, {employee_deptartment}, {employee_role} and {start_date} to create welcome letter and a detailed training schedule')

        return response['response']
    

    def PersonalizedLearningPathways(self, employeeInfo, carrerGoal, currentSkills, skillGap, preferedLearningStyle, timeFrame, senderName='AI Agent',senderPosition='AI HR Head'):
        """This function call an agent to create personalizes learning path for the emplpoyee"""
        agent_prompt = f"Generate personalized learning pathways by recommending training modules based on inputs such as Employee Inforamtion: {employeeInfo}, Carrer Goal: {carrerGoal}, Current Skills: {currentSkills}, Skill Gap: {skillGap}, Prefered learing style: {preferedLearningStyle}, and Time frame: {timeFrame} to align with the employee’s career ambitions."
        
        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Personalized Learning Pathways")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="PersonalizedLearningPathways-HRTool",
        message=f'Generate personalized learning pathways by recommending training modules based on the provided details. [!Important] make the personalised learning pathway in mail format, use these on sender side name:{senderName}, and position:{senderPosition}')

        return response['response']

    
    def ContentCreation(self, trainingObjective, targetAudience, coreContent, interactiveElements, assesmentCriteria, designPreference, timeFrame):
        """This function call an agent to create training material/quizess for employee based on training objective"""
        agent_prompt = f"Create interactive training materials and quizzes using inputs like Training Objectives: {trainingObjective}, Target Audience: {targetAudience}, Core Content: {coreContent}, Interactive Elements:{interactiveElements}, Assessment Criteria:{assesmentCriteria}, Design Preferences:{designPreference}, and Time Frame: {timeFrame} to ensure effective learning and engagement."
        
        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Content Creation")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="ContentCreation-HRTool",
        message=f'Create interactive training materials and quizzes using provided details')

        return response['response']
    

    def FeedbackGeneration(self, employeeInfo, performanceMetrics, managersNote, companyValues, desiredTone, sepcificFeedbackFocusAreas, senderName='AI Agent',senderPosition='AI HR Head'):
        """This function will call an agent to generate performace review"""
        agent_prompt = f"Using the provided employee information:{employeeInfo}, performance metrics:{performanceMetrics}, manager's notes:{managersNote}, company values:{companyValues}, desired tone:{desiredTone}, and specific feedback focus areas:{sepcificFeedbackFocusAreas}, generate a constructive and personalized performance review. The feedback should be clear, actionable, and aligned with the company’s goals, highlighting both strengths and areas for improvement. Ensure the tone matches the desired approach and is appropriate for the employee's role and performance level. [!Important] make sure feedback should not be lenghty make feedback as crips and informative mail."

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Feedback Generation")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="FeedbackGeneration-HRTool",
        message=f'Generate a personalized and constructive performance review using the provided details. [!Important] make the generated feedback in mail format, use these on sender side name:{senderName}, and position:{senderPosition}')

        return response['response']


    def GoalSetting(self, employeeManagerInfo, companyObjective, currentPerformace, developmentArea, timeFrame, desiredOutput, senderName='AI Agent',senderPosition='AI HR Head'):
        """This function will call an agent to generate professional goals for employee based on their preference"""
        agent_prompt = f"Generate professional goals for an employee or manager:{employeeManagerInfo} based on their role, current performance:{currentPerformace}, development areas:{developmentArea}, company objectives:{companyObjective}, desired outcomes:{desiredOutput}, and time frame:{timeFrame}. Ensure the goals are specific, achievable, and aligned with both individual and organizational priorities.[!Important] make the goal in mail format, use these on sender side name:{senderName}, and position:{senderPosition}"

        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Goal Setting")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="GoalSetting-HRTool",
        message=f'Create specific and aligned professional goals based on the provided role, performance, and company objectives. [!Important] make the goal in mail format, use these on sender side name:{senderName}, and position:{senderPosition}')

        return response['response']
    

    def SentimentAnalysis(self, employeeFeedbackData, contextualInformation, keywordsIndicators, historicalData=None, senderName='AI Agent',senderPosition='AI HR Head'):
        """This function call an agent to perform sentiment analysis on emplyoee"""
        if historicalData is None:
            agent_prompt = f"Analyze the provided employee feedback data:{employeeFeedbackData} to gauge overall sentiment, classify it into categories such as positive, neutral, or negative, and identify key areas:{keywordsIndicators} that need attention. Use contextual information:{contextualInformation} to ensure accurate insights into employee satisfaction. [!Important] make the sentiment analysis in mail format, use these on sender side name:{senderName}, and position:{senderPosition}"
            
            agent = self.Agent.create_agent(
            env_id=self.Agent_Environment['env_id'],
            system_prompt=agent_prompt,
            name="Sentiment Analysis")

            response = self.Agent.send_message(
            agent_id=agent['agent_id'],
            user_id="default_user",
            session_id="SentimentAnalysis-HRTool",
            message=f'Perform sentiment analysis on the provided employee feedback to assess satisfaction and identify areas needing attention. [!Important] make the sentiment analysis in mail format, use these on sender side name:{senderName}, and position:{senderPosition}')

            return response['response']
    
        else:
            agent_prompt = f"Analyze the provided employee feedback data:{employeeFeedbackData} to gauge overall sentiment, classify it into categories such as positive, neutral, or negative, and identify key areas:{keywordsIndicators} that need attention. Use contextual information:{contextualInformation} and historical data:{historicalData} to ensure accurate insights into employee satisfaction. [!Important] make the sentiment analysis in mail format, use these on sender side name:{senderName}, and position:{senderPosition}"

            agent = self.Agent.create_agent(
            env_id=self.Agent_Environment['env_id'],
            system_prompt=agent_prompt,
            name="Sentiment Analysis")

            response = self.Agent.send_message(
            agent_id=agent['agent_id'],
            user_id="default_user",
            session_id="FSentimentAnalysis-HRTool",
            message=f'Perform sentiment analysis on the provided employee feedback to assess satisfaction and identify areas needing attention. [!Important] make the sentiment analysis in mail format, use these on sender side name:{senderName}, and position:{senderPosition}')

            return response['response']




