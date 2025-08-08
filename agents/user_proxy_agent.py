from autogen_agentchat.agents import UserProxyAgent
from config.system_config import USER_PROXY_NAME


class UserProxy:
        def __init__(self,name = USER_PROXY_NAME):
            self.name = name
        def get_agent(self):
            user_proxy = UserProxyAgent(
                name=self.name,
                input_func=input
            )
            return user_proxy
