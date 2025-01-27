from __future__ import annotations

from typing import Optional, Type

from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_community.tools.agentql.utils import get_current_page

from pydantic import BaseModel, Field

from langchain_community.tools.playwright.base import BaseBrowserTool

class QueryElementToolInput(BaseModel):
    """Input for AgentQL's Query Data Tool"""

    query: Optional[str] = Field(default=None, description="The AgentQL query to query the target element")
    prompt: Optional[str] = Field(default=None, description="The natural language prompt to use to search for the target element")
    
    # timeout: Optional[int] = Field(..., description="Timeout value in seconds for the connection with backend API service")
    # wait_for_network_idle: Optional[bool] = Field(..., description="Whether to wait for network idle state")
    # include_hidden: Optional[bool] = Field(..., description="Whether to include hidden elements")
    # mode: Optional[str] = Field(..., description="Mode of the query ('standard' or 'fast')")
    # force_click: Optional[bool] = Field(..., description="Whether to force click on the target element")


class QueryElementTool(BaseBrowserTool): # type: ignore[override, override, override]
    """Tool for clicking on an element given an AgentQL query or a natural language prompt."""

    name: str = "click_element"
    description: str = "Click on an element given an AgentQL query or a natural language prompt"
    args_schema: Type[BaseModel] = QueryElementToolInput

    playwright_timeout: float = 5_000
    """Timeout (in ms) for Playwright to wait for element to be ready."""
    playwright_force_click: bool = False
    """Whether to force click on the target element."""

    def _run(
        self,
        query: Optional[str] = None,
        prompt: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ):
        """Use the tool."""
        if self.sync_browser is None:
            raise ValueError(f"Synchronous browser not provided to {self.name}")
        page = get_current_page(self.sync_browser)

        # try:
        if query:
            element = page.query_elements(query)
            # TODO: identify the only element here
            # return element
        else:
            element = page.get_by_prompt(prompt)
            tf_id = element.get_attribute("tf623_id")
            return f"[tf623_id='{tf_id}']"
        # except Exception as e:
        #     return f"Unable to click on element '{selector}'"
        # return f"Clicked element '{selector}'"