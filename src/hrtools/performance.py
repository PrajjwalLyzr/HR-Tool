from lyzragent import LyzrAgent

class Performance:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

        self.Agent_Environment = self.Agent.create_environment(
            name="Performance Tool",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["perplexity_search"])
        

    def FeedbackGeneration(self, employeeInfo, performanceMetrics, managersNote, companyValues, desiredTone, sepcificFeedbackFocusAreas, senderName='AI Agent',senderPosition='AI HR Head'):
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