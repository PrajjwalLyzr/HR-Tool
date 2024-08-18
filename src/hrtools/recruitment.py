from lyzragent import LyzrAgent

class Recruitment:
    def __init__(self, LyzrKey, APIKey):
        self.Agent = LyzrAgent(
        x_api_key=LyzrKey,
        llm_api_key=APIKey)

        self.Agent_Environment = self.Agent.create_environment(
            name="Recruitment Tool",
            features=[{
                "type": "TOOL_CALLING",
                "config": {"max_tries": 3},
                "priority": 0
            }],
            tools=["perplexity_search"])
        
    def JobDescriptionCreator(self, about_job):        
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




