from langchain_community.tools.agentql import QueryDataTool
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain_community.tools.playwright.navigate import NavigateTool

sync_browser = create_sync_playwright_browser(headless=False)
tool = QueryDataTool(sync_browser=sync_browser)
navigate_tool = NavigateTool(sync_browser=sync_browser)

navigate_tool.run({"url": "https://www.agentql.com/blog"})
data = tool.run({"query": "{ blogs[] { title, url, date, author}}"})
print(data)

# data = tool.run({"prompt": "Get the title, url, date and author of the blog posts on the current page"})
# print(data)
