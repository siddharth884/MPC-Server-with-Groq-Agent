from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()
async def main():
    client=MultiServerMCPClient(
        {
            "finder":{
                "command":"python",
                "args":["FinderServer.py"],
                "transport":"stdio",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] =  os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model=ChatGroq(model="llama-3.1-8b-instant")
    agent=create_agent(
        model, tools
    )
    response = await agent.ainvoke(
        {

    "messages": [
        {
            "role": "user",
            "content": "Use the KeywordFinder tool to search for 'adapters' inside the path C:/Users/amishr/TestProject/Task2/requirements.txt"
        }
    ]
}
    )
    print("response:", response['messages'][-1].content)

asyncio.run(main())    