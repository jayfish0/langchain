from typing import Optional, List, Type, Any, cast
from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import ConfigDict, model_validator

# Import Browser
from playwright.sync_api import Browser as SyncBrowser

# Import from agentql
from langchain_community.tools.agentql import (
    QueryDataTool, 
    QueryElementTool
)

# Import from playwright
from langchain_community.tools.playwright.base import (
    lazy_import_playwright_browsers,
    BaseBrowserTool
)
from langchain_community.tools.playwright import (
    NavigateTool,
    NavigateBackTool,
    ClickTool
)

class AgentQLToolkit(BaseToolkit):

    sync_browser: Optional["SyncBrowser"] = None

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="forbid",
    )

    @model_validator(mode="before")
    @classmethod
    def validate_imports_and_browser_provided(cls, values: dict) -> Any:
        """Check that the arguments are valid."""
        lazy_import_playwright_browsers()
        if values.get("sync_browser") is None:
            raise ValueError("sync_browser must be specified.")
        return values

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        tool_classes: List[Type[BaseBrowserTool]] = [
            QueryDataTool,
            QueryElementTool,
            NavigateTool,
            NavigateBackTool,
            ClickTool
        ]

        tools = [
            tool_cls.from_browser(sync_browser=self.sync_browser)
            for tool_cls in tool_classes
        ]
        return cast(List[BaseTool], tools)
    
    @classmethod
    def from_browser(
        cls,
        sync_browser: Optional[SyncBrowser] = None,
    ) -> "AgentQLToolkit":
        """Instantiate the toolkit.

        Args:
            sync_browser: Optional. The sync browser. Default is None.
            async_browser: Optional. The async browser. Default is None.

        Returns:
            The toolkit.
        """
        # This is to raise a better error than the forward ref ones Pydantic would have
        lazy_import_playwright_browsers()
        return cls(sync_browser=sync_browser)