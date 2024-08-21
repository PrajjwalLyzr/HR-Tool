from lyzragent import LyzrAgent

class HelperTool:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

    def MailSender(self, mail, mail_id):
        self.Agent_Environment = self.Agent.create_environment(
            name="Mail Sender",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["send_email"])
        
        agent_prompt = f"Use this mail:{mail}, and your job is to send this mail to this mail id:{mail_id}"


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