from agents.judge_agent import JudgeAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.system_config import MAX_TURNS_VOTING,TEXT_MENTION

class JudgeTeam:
    def __init__(self):
        self.judge = JudgeAgent().get_agent()
        self.termination = TextMentionTermination(TEXT_MENTION)
        self.max_turns = MAX_TURNS_VOTING

    def get_team(self):
        inner_team_3 = RoundRobinGroupChat(
            participants=[self.judge],
            termination_condition=self.termination,
            max_turns=self.max_turns
        )
        return inner_team_3