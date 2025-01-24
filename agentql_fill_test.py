from langchain_community.tools.agentql import FillTool
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain_community.tools.playwright.navigate import NavigateTool

sync_browser = create_sync_playwright_browser(headless=False)
tool = FillTool(sync_browser=sync_browser)
navigate_tool = NavigateTool(sync_browser=sync_browser)

navigate_tool.run({"url": "https://account.ycombinator.com/?continue=https%3A%2F%2Fapply.ycombinator.com%2F"})
tool.run({"target": "email", "value": "test@test.com"})
tool.run({"target": "password", "value": "test"})

import time
time.sleep(3)