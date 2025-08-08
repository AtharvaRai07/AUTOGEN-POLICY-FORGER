from autogen_agentchat.agents import AssistantAgent
from models.openai_model import ModelClient
from config.prompt_loader import PromptLoader
from autogen_agentchat.agents import UserProxyAgent

from autogen_core.tools import FunctionTool
from tools.tools import Tools
from config.system_config import MODEL,API_KEY

class EmailSenderAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("email_sender")

        # Initialize model client
        self.model_client = ModelClient().openai_model()
        self.tool = FunctionTool(
            name="send_email_with_attachment",
            description="Sends an email with subject, body, and PDF attachment to a given recipient email address.",
            func=Tools.send_email_with_attachment
        )
    def get_agent(self):
        email_sender = AssistantAgent(
            name="EmailSenderAgent",
            model_client=self.model_client,
            system_message=self.system_prompt,
            tools=[self.tool],
            reflect_on_tool_use=True
        )
        return email_sender