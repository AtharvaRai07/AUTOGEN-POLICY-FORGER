from autogen_agentchat.agents import AssistantAgent
from models.openai_model import ModelClient
from config.prompt_loader import PromptLoader

class DebateSummerizerAgent:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("debate_summariser")
        self.model_client = ModelClient().openai_model()

    def get_agent(self):
        debate_summeriser = AssistantAgent(
            name="DebateRecorderAgent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return debate_summeriser
    