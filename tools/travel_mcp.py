import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
  {
    "mcp_tool_12306": {
      "transport": "streamable_http",
      "url": "https://mcp.api-inference.modelscope.net/XXX/mcp"
    },
    "time": {
      "transport": "stdio",
      "command": "uvx",
      "args": [
          "mcp-server-time",
          "--local-timezone=Asia/Shanghai"
      ]
    }
  }
)

async def _load_tools():
    return await client.get_tools()

# 普通 .py 文件不支持顶层 await，必须用 asyncio.run() 驱动异步调用
transport_tool = asyncio.run(_load_tools())