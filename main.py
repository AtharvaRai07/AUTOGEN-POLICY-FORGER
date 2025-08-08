from autogen_agentchat.base import TaskResult
from team.outer_team import OuterTeam
import asyncio
from config.system_config import SAMPLE_TASK
from autogen_agentchat.messages import TextMessage
from tools.tools import Tools

async def main():
    task = SAMPLE_TASK
    team = OuterTeam().Team()
    try:
        async for message in team.run_stream(task=task):
            print("-"*40)
            if isinstance(message,TextMessage):
                print(f"{message.source} : {message.content}")
            elif isinstance(message,TaskResult):
                print("-"*40)
                print(f"TERMINATION REASON : {message.stop_reason}")
    except Exception as e:
        print("Exception : ",e)
    finally:
        print("Task Completed")

if __name__ == "__main__":
    asyncio.run(main())
