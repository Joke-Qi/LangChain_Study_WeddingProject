import os
from langchain.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

tavily_search = TavilySearch(
    max_results=5,
    topic="general"
)

@tool(description="使用搜索工具，查询相关信息")
def get_search_tool(query: str):
    return tavily_search.invoke(query)

