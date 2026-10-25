"""
主Agent，根据用户需求，选择调用其他agent，并将最终结果传递给用户
"""
import asyncio
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from tools.wedding_agent_tools import get_wedding_songs, get_wedding_venues, get_wedding_travel, update_state
from state.weeding_state import WeedingState

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

coordinator = create_agent(
    model="deepseek-flash",
    tools=[get_wedding_songs, get_wedding_venues, get_wedding_travel, update_state],
    state_schema=WeedingState,
    system_prompt="""
    你是婚礼协调员。你负责与用户沟通，找到更新状态所需的所有信息，并更新到state。
    一旦完成，你就可以委派任务了。将查找高铁（该过程比较慢）、搜索场地和策划播放列表的任务委派给您的专家Agent。
    当你收到他们的答案，为我设计一场完美的婚礼方案。
    """
)
async def wedding_main():
    response = await coordinator.ainvoke(
        {
            "messages": [HumanMessage(content="我来自西安，我想在杭州举办一场100人的婚礼，爵士风格的。")],
        }
    )

    for message in response["messages"]:
        message.pretty_print()

if __name__ == '__main__':
    print(asyncio.run(wedding_main()))

