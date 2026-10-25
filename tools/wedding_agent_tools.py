"""
agent工具类
"""
import asyncio

from langchain_core.messages import ToolMessage
from langgraph.types import Command

from agents.travel_agent import get_travel_agent
from agents.venue_agent import get_search_venue
from agents.song_agent import get_agent_song
from langchain.tools import tool, ToolRuntime

@tool(description="输入要获取的歌曲类型描述，返回对应歌单信息")
def get_wedding_songs(query: str) -> str:
    return get_agent_song(query)

@tool(description="输入婚礼基本情况描述，返回推荐婚礼地点推荐信息")
def get_wedding_venues(query: str) -> str:
    return get_search_venue(query)

@tool(description="输入要去的目的地和出发地，以及出行偏好，返回推荐的交通信息")
def get_wedding_travel(query: str) -> str:
    return asyncio.run(get_travel_agent(query))

@tool(description="当你询问用户，知道下列所有值时更新State：origin、destination、guest_count、genre")
def update_state(origin: str, destination: str, guest_count: str, genre: str, runtime: ToolRuntime) -> str:
    return Command(update={
        "origin": origin,
        "destination": destination,
        "guest_count": guest_count,
        "genre": genre,
        "messages": [ToolMessage("Successfully updated state", tool_call_id=runtime.tool_call_id)]}
        )