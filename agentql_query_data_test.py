from langchain_community.tools.agentql import QueryDataTool
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain_community.tools.playwright.navigate import NavigateTool

sync_browser = create_sync_playwright_browser(headless=False)
tool = QueryDataTool(sync_browser=sync_browser)
navigate_tool = NavigateTool(sync_browser=sync_browser)

navigate_tool.run({"url": "https://scrapeme.live/shop/"})
data = tool.run({"query": "{ products[] { name, price } }"})
print(data)

import time
time.sleep(3)