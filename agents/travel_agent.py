import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

from tools.travel_mcp import transport_tool

agent = create_agent(
    model="deepseek-flash",
    tools=transport_tool,
    system_prompt="""
    你是一个旅行助手Agent。你为用户搜索到达婚礼地点的理想车次，您不能再追问任何后续问题。
    您必须根据以下标准找到最佳航班选择：
    - 价格（最低，经济舱）
    - 持续时间（最短）
    - 日期（您认为在该地点举行婚礼的最佳时间）
    为了使事情变得简单，只寻找一张票，单程。
    你不会得到额外的信息，只有出发地和目的地。你的工作是批判性地思考最佳选择。
    一旦你找到了最好的选项，让用户知道你的候选列表。
    调用搜索航班工具时，如果是地点在中国，需要使用zh-cn作为Locale参数。
    """
)

async def get_travel_agent(query: str) -> str:
    res = await agent.ainvoke(
        {
            'messages': HumanMessage(query)
        }
    )
    # for message in res['messages']:
    #     message.pretty_print()
    return res['messages'][-1].content


if __name__ == '__main__':
    # MCP 工具是异步的，agent 必须用 ainvoke 调用，不能用同步的 invoke
    print(asyncio.run(get_travel_agent(
        "帮我查询后天从西安到杭州的车次，时间在10小时内，到达时间不要太晚（晚上11点之后算太晚），在满足以上两个条件下尽可能便宜")))