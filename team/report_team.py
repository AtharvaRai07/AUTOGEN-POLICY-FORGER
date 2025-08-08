from autogen_agentchat.teams import RoundRobinGroupChat
from agents.voting_aggregator_agent import VotingAggregatorAgent
from agents.amendment_writer import AmendmentWriterAgent
from agents.report_maker_agent import ReportMakerAgent
from autogen_agentchat.conditions import TextMentionTermination
from agents.user_proxy_agent import UserProxy
from config.system_config import MAX_TURNS,TEXT_MENTION

class ReportMakingTeam:
    def __init__(self):
        
        self.user_proxy = UserProxy().get_agent()
        self.termination = TextMentionTermination(TEXT_MENTION)
        self.voting_count = VotingAggregatorAgent().get_agent()
        self.amendment = AmendmentWriterAgent().get_agent()
        self.report = ReportMakerAgent().get_agent()
        self.max_turns = MAX_TURNS

    def get_team(self):
        inner_team_4 = RoundRobinGroupChat(
            participants=[self.voting_count,self.amendment,self.report,self.user_proxy],
            termination_condition=self.termination,
            max_turns=self.max_turns

        )
        return inner_team_4