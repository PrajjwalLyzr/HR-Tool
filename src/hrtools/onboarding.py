from lyzragent import LyzrAgent

class Onboarding:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

        self.Agent_Environment = self.Agent.create_environment(
            name="Onboarding Tool",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["perplexity_search"])
        
    def OnboardingAssistance(self, professional_mail, temp_password, sendername="Lyzr's AI Agent", designation='AI HR Head', sendermail='ai.agent@lyzr.ai'):
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
    
    def MailSender(self, mail, mail_id):
        self.Agent_Environment = self.Agent.create_environment(
            name="Onboarding Tool - Mail Sender",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["send_email"])
        
        agent_prompt = f"Use this mail:{mail} fine tune it if needed, and your job is to send this mail to this mail id:{mail_id}"


        agent = self.Agent.create_agent(
        env_id=self.Agent_Environment['env_id'],
        system_prompt=agent_prompt,
        name="Mail Sender")

        response = self.Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="MailSender-HRTool",
        message=f'Send a mail:{mail} to this email:{mail_id}')

        return response['response']