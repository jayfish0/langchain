import agentql
from typing import TYPE_CHECKING, Optional, List

from playwright.sync_api import Browser as SyncBrowser
from playwright.sync_api import Page as SyncPage

if TYPE_CHECKING:
    from playwright.async_api import Browser as AsyncBrowser
    from playwright.async_api import Page as AsyncPage
    from playwright.sync_api import Browser as SyncBrowser
    from playwright.sync_api import Page as SyncPage

def get_current_page(browser: SyncBrowser) -> SyncPage:
    """
    Get the current page of the browser.
    Args:
        browser: The browser to get the current page from.
    Returns:
        SyncPage: The current page.
    """
    if not browser.contexts:
        context = browser.new_context()
        return agentql.wrap(context.new_page())
    context = browser.contexts[0]  # Assuming you're using the default browser context
    if not context.pages:
        return agentql.wrap(context.new_page())
    # Assuming the last page in the list is the active one
    return agentql.wrap(context.pages[-1])