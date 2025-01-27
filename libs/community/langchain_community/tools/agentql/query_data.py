from pydantic import BaseModel, Field
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_community.tools.playwright.base import BaseBrowserTool
from langchain_community.tools.agentql.utils import get_current_page

class QueryDataToolInput(BaseModel):
    """Input for AgentQL's Query Data Tool"""

    query: Optional[str] = Field(default=None, description="The AgentQL query to acquire the data on the current web page")
    prompt: Optional[str] = Field(default=None, description="The natural language prompt to describe the data you want to acquire on the current web page")

class QueryDataTool(BaseBrowserTool):
    """Tool for querying data given an AgentQL query or a natural language prompt."""

    name: str = "query_data"
    description: str = "Query data given an AgentQL query or a natural language prompt"
    args_schema: Type[BaseModel] = QueryDataToolInput

    def _run(
        self,
        query: Optional[str] = None,
        prompt: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> dict:
        """Use the tool."""
        if self.sync_browser is None:
            raise ValueError(f"Synchronous browser not provided to {self.name}")
        page = get_current_page(self.sync_browser)

        # try:
        if query:
            data = page.query_data(query)
        else:
            data = page.get_data_by_prompt_experimental(prompt)
        return data
        # except Exception as e:
        #     return f"Unable to click on element '{selector}'"
        # return f"Clicked element '{selector}'"