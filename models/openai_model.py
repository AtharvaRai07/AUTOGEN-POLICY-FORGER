from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.system_config import MODEL,API_KEY
class ModelClient:
    def __init__(self):
        self.model = MODEL
        self.api_key = API_KEY

    def openai_model(self):
        model = OpenAIChatCompletionClient(
            model=self.model,
            api_key=self.api_key
        )
        return model
    # def openai_model(self):
    #     xai_client = OpenAIChatCompletionClient(
    #     base_url="https://api.x.ai/v1",  # xAI's API endpoint
    #     model="grok-3",  # Use a valid xAI model (e.g., grok-4, grok-3, grok-beta)
    #     api_key="",  # Load API key from environment variable
    #     model_info={
    #         "family": "xai",
    #         "vision": False,  # Set to True for vision-enabled models like grok-2-vision
    #         "function_calling": True,  # Check xAI documentation for model capabilities
    #         "json_output": False  # Adjust based on model support
    #     }
    # )
    #     return xai_client