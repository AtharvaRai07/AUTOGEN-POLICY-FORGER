from autogen_agentchat.agents import AssistantAgent
from models.openai_model import ModelClient
from config.prompt_loader import PromptLoader
from autogen_core.tools import FunctionTool
from tools.tools import Tools

class ReportMakerAgent:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("report_maker")
        self.model_client = ModelClient().openai_model()
        # Wrap the static method with FunctionTool
        self.tool = FunctionTool(
            name="pdf_maker_tool",
            description="Converts a Markdown string into a styled PDF and saves it to a given output path.",
            func=Tools.markdown_to_pdf
        )

    def get_agent(self):
        report_maker = AssistantAgent(
            name="FinalReportGeneratorAgent",
            model_client=self.model_client,
            system_message=self.system_prompt,
            tools=[self.tool],
            reflect_on_tool_use=True
        )
        return report_maker

