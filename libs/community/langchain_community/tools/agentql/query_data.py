from pydantic import BaseModel, Field
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_community.tools.playwright.base import BaseBrowserTool
from langchain_community.tools.agentql.utils import get_current_page

class QueryDataToolInput(BaseModel):
    """Input for AgentQL's Query Data Tool"""

    query: Optional[str] = Field(default=None, description="The AgentQL query to acquire the data on the current page")
    # prompt: Optional[str] = Field(default=None, description="The natural language prompt to use to search for the target clickable element")

class QueryDataTool(BaseBrowserTool):
    """Tool for querying data given an AgentQL query or a natural language prompt."""

    name: str = "query_data"
    description: str = "Query data given an AgentQL query or a natural language prompt"
    args_schema: Type[BaseModel] = QueryDataToolInput

    def _run(
        self,
        query: Optional[str] = None,
        # prompt: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        if self.sync_browser is None:
            raise ValueError(f"Synchronous browser not provided to {self.name}")
        page = get_current_page(self.sync_browser)
        return page.query_data(query, mode="fast")
