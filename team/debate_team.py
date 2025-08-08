from agents.ruling_party_agent import RulingPartyAgent
from agents.opposition_part_agent import OppositionPartyAgent
from agents.debate_summerizer_agent import DebateSummerizerAgent
from agents.user_proxy_agent import UserProxy
from autogen_agentchat.teams import SelectorGroupChat
from config.prompt_loader import PromptLoader
from config.system_config import TEXT_MENTION,MAX_TURNS
from autogen_agentchat.conditions import TextMentionTermination
from models.openai_model import ModelClient

from typing import Sequence
from autogen_agentchat.messages import BaseAgentEvent,BaseChatMessage

def selector_func(message: Sequence[BaseAgentEvent | BaseChatMessage])->str:
    i = 6
    while i>6:
        if i%2==0:
            i-=1
            return RulingPartyAgent().get_agent().name
        else:
            i-=1
            return OppositionPartyAgent().get_agent().name
        

class DebateTeam:
    def __init__(self):
        self.ruling_party = RulingPartyAgent().get_agent()
        self.opposition_party = OppositionPartyAgent().get_agent()
        self.user_proxy = UserProxy().get_agent()
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("custom_selector_prompt")
        self.debate_summerizer= DebateSummerizerAgent().get_agent()
        self.termination = TextMentionTermination(TEXT_MENTION)
        self.model_client = ModelClient().openai_model()
        self.max_turns = MAX_TURNS
    def get_team(self):
        inner_team_2 = SelectorGroupChat(
            participants=[self.ruling_party,self.opposition_party,self.debate_summerizer,self.user_proxy],
            model_client=self.model_client,
            termination_condition=self.termination,
            max_turns=self.max_turns,
            selector_prompt=self.system_prompt,
            selector_func=selector_func,
            allow_repeated_speaker=False
        )
        return inner_team_2
