from agents.bill_parser_agent import BillParserAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.user_proxy_agent import UserProxy
from config.system_config import MAX_TURNS,TEXT_MENTION

class BillParserTeam:
    def __init__(self):
        self.bill_parser = BillParserAgent().get_agent()
        self.user_proxy = UserProxy().get_agent()
        self.termination = TextMentionTermination(TEXT_MENTION)
        self.max_turns = MAX_TURNS
    def get_team(self):
        inner_team_1 = RoundRobinGroupChat(
            participants=[self.bill_parser,self.user_proxy],
            termination_condition=self.termination,
            max_turns=self.max_turns
        )
        return inner_team_1