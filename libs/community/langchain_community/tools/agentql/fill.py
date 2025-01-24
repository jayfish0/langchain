from pydantic import BaseModel, Field
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_community.tools.playwright.base import BaseBrowserTool
from langchain_community.tools.agentql.utils import get_current_page

class FillToolInput(BaseModel):
    """Input for AgentQL's Fill Tool"""

    target: Optional[str] = Field(default=None, description="Description of the target field on the webpage that need to be filled")
    value: Optional[str] = Field(default=None, description="The value to fill in the target field")

class FillTool(BaseBrowserTool):
    """Tool for filling in a field on the current page."""

    name: str = "fill_field"
    description: str = "Fill in a field on the current page"
    args_schema: Type[BaseModel] = FillToolInput

    def _run(
        self,
        target: Optional[str] = None,
        value: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        if self.sync_browser is None:
            raise ValueError(f"Synchronous browser not provided to {self.name}")
        page = get_current_page(self.sync_browser)
        element = page.get_by_prompt(target)
        element.fill(value)