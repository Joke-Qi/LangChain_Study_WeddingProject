import os
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tools.venue_tool import get_search_tool
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

agent = create_agent(
    model='deepseek-flash',
    tools=[get_search_tool],
    system_prompt="""
    你是场地专家，你在指定的位置搜索满足要求的场地。
    你不能再追问任何后续问题，你必须根据以下标准找到最佳的场地选择：
    - 价格（最低）
    - 容量（完全匹配）
    - 评价（最高）
    您可能需要进行多次搜索以迭代地找到最佳选项。展示时要说明具体的价格
    """
)

def get_search_venue(query: str):
    res = agent.invoke({
        'messages': [HumanMessage(query)]
    })
    return res['messages'][-1].content

if __name__ == '__main__':
    print(get_search_venue("西安市有哪些推荐点,我结婚需要，100人左右"))