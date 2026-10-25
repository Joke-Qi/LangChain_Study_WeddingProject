from langchain.tools import tool
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")

@tool(description="查询数据库获取对应数据信息")
def query_playlist_db(query: str) -> str:
    try:
        return db.run(query)
    except Exception as e:
        return f"Error querying database: {e}"

if __name__ == '__main__':
    # 测试，查询歌单数据
    print(query_playlist_db.invoke({"query": "SELECT * FROM Playlist"}))
