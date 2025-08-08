from autogen_agentchat.agents import AssistantAgent
from models.openai_model import ModelClient
from config.prompt_loader import PromptLoader

class JudgeAgent:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("judge_agent")
        self.model_client = ModelClient().openai_model()

    def get_agent(self):
        judge_agent = AssistantAgent(
            name="JudgeAgent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return judge_agent
