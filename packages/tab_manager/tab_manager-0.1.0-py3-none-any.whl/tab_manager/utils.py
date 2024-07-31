"""Utility functions."""

from .state import AppState, Window, Tab


async def get_tabs(app_state: AppState) -> list[Tab]:
    """Retrieve the tabs that are currently open."""
