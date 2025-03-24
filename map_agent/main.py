from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
import asyncio
from dotenv import load_dotenv
from models.Location import Location
load_dotenv()

async def main():
    initial_actions = [{'open_tab': {'url': 'https://www.google.com/maps'}}]
    planner_llm = ChatOpenAI(model='o3-mini')
    
    browser = Browser()
    agent = Agent(
        task="Use google map to find parking lot in dtla",
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
        planner_llm=planner_llm,
        use_vision_for_planner=True,
        planner_interval=4,
        initial_actions=initial_actions,
    )
    history =await agent.run()
    result = history.final_result()
    if result:
        parsed_result: Location = Location.model_validate_json(result)
        print(parsed_result)
    input("Press Enter to close the browser...")
    await browser.close()

asyncio.run(main())