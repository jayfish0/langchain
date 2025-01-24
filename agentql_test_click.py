from langchain_community.tools.agentql import ClickTool
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain_community.tools.playwright.navigate import NavigateTool

sync_browser = create_sync_playwright_browser(headless=False)
tool = ClickTool(sync_browser=sync_browser)
navigate_tool = NavigateTool(sync_browser=sync_browser)

navigate_tool.run({"url": "https://scrapeme.live/shop/"})
tool.run({"prompt": "next page button"})

import time
time.sleep(3)