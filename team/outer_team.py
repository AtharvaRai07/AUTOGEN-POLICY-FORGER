from team.society_teams import SocietyAgents
from agents.user_proxy_agent import UserProxy
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.email_sender_agent import EmailSenderAgent
from config.system_config import MAX_TURNS,TEXT_MENTION

society_bill_parser_team = SocietyAgents().society_bill_parser()
society_debate_team = SocietyAgents().society_debate()
society_judge_team = SocietyAgents().society_judge()
society_report_team = SocietyAgents().society_report()


class OuterTeam:
    def __init__(self):
        self.termination = TextMentionTermination(TEXT_MENTION)
        self.max_turns = MAX_TURNS
        self.email_sender = EmailSenderAgent().get_agent()
        self.user_proxy = UserProxy().get_agent()
    def Team(self):
        team = RoundRobinGroupChat(
            participants=[society_bill_parser_team,society_debate_team,society_judge_team,society_report_team,self.email_sender,self.user_proxy],
            max_turns=self.max_turns,
            termination_condition=self.termination
        )
        return team



