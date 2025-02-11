from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="""Open two tabs: Wikipedia and GitHub. On Wikipedia, search for 'Python programming' 
        and on GitHub search for 'browser-use'. Then switch between tabs and tell me the titles 
        of both pages.""",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
