import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from tools.song_tool import query_playlist_db

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
agent = create_agent(
    model='deepseek-flash',
    tools=[query_playlist_db],
    system_prompt="""
    你是播放列表专家。查询sql数据库并为给定类型的婚礼策划完美的播放列表。
    一旦你有了你的播放列表，计算播放列表的总时长和成本，每首歌都有一个相关的价格。
    如果在查询数据库时遇到错误，请尝试通过更改查询来修复它们。
    不要空手而归，继续尝试查询数据库，直到你找到一个歌曲列表。
    您可能需要进行多个查询以迭代地找到最佳选项。
    """
)

def get_agent_song(query: str):
    res = agent.invoke({
        'messages':[HumanMessage(query)]
    })
    return res['messages'][-1].content