from langchain_community.agent_toolkits import AgentQLToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, create_react_agent
from langchain_openai import ChatOpenAI

import os
os.environ["OPENAI_API_KEY"] = "sk-"
os.environ["LANGCHAIN_API_KEY"] = ""

sync_browser = create_sync_playwright_browser(headless=False)
toolkit = AgentQLToolkit.from_browser(sync_browser=sync_browser)
tools = toolkit.get_tools()

prompt = hub.pull("hwchase17/openai-tools-agent")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) 

agent = create_openai_tools_agent(llm, tools, prompt)
# agent = create_react_agent(llm, tools, prompt) #Use this if using hwchase17/react prompt
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# command = {
#     "input": """
# Go to https://news.ycombinator.com/ and give me the title of the posts from the first three pages using the following agentql query for each page:
# { posts[] { title}}
# """
# }

command = {
    "input": """
Go to https://news.ycombinator.com/ and give me the title of the posts from the first three pages using the following agentql query for each page:
{ posts[] { title}}
"""
}
agent_executor.invoke(command)