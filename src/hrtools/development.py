from lyzragent import LyzrAgent

class Development:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

        self.Agent_Environment = self.Agent.create_environment(
            name="Development Tool",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["perplexity_search"])
    
    def PersonalizedLearningPathways(self, employeeInfo, carrerGoal, currentSkills, skillGap, preferedLearningStyle, timeFrame, senderName='AI Agent',senderPosition='AI HR Head'):
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