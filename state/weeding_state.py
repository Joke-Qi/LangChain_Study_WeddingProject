from langchain.agents import AgentState
from dataclasses import dataclass

@dataclass
class WeedingState(AgentState):
    origin: str  # 起点
    destination: str  # 目的地
    guest_count: str  # 宾客数量
    genre: str  # 婚礼风格