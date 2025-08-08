from autogen_agentchat.agents import SocietyOfMindAgent
from team.bill_parser_inner_team import BillParserTeam
from team.debate_team import DebateTeam
from team.judicial_voting import JudgeTeam
from team.report_team import ReportMakingTeam
from models.openai_model import ModelClient

class SocietyAgents:
    def __init__(self):
        self.model_client = ModelClient().openai_model()
        self.first_inner_team = BillParserTeam().get_team()
        self.second_inner_team = DebateTeam().get_team()
        self.thrid_inner_team = JudgeTeam().get_team()
        self.fourth_inner_team = ReportMakingTeam().get_team()
    
    def society_bill_parser(self):
        return SocietyOfMindAgent(
            name="society_of_mind_1",
            team= self.first_inner_team,
            model_client=self.model_client
        )
        
    
    def society_debate(self):
        return SocietyOfMindAgent(
            name="society_of_mind_2",
            team= self.second_inner_team,
            model_client=self.model_client
        )
    
    def society_judge(self):
        return SocietyOfMindAgent(
            name="society_of_mind_3",
            team= self.thrid_inner_team,
            model_client=self.model_client
        )
    
    def society_report(self):
        return SocietyOfMindAgent(
            name = "society_of_mind_4",
            team = self.fourth_inner_team,
            model_client = self.model_client
        )

    
    