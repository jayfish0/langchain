from langchain_community.tools.agentql import QueryElementTool
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain_community.tools.playwright import NavigateTool, ClickTool

sync_browser = create_sync_playwright_browser(headless=False)
queryElement_tool = QueryElementTool(sync_browser=sync_browser)
navigate_tool = NavigateTool(sync_browser=sync_browser)
click_tool = ClickTool(sync_browser=sync_browser, visible_only=False)

navigate_tool.run({"url": "https://scrapeme.live/shop/"})
selector = queryElement_tool.run({"prompt": "next page element"})
click_tool.run({"selector": selector})

import time
time.sleep(3)