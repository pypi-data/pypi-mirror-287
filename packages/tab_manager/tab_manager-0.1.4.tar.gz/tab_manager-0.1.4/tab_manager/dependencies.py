"""FastAPI dependencies."""

from .state import AppState
from starlette.requests import Request
from fastapi import WebSocket


async def get_app_state() -> AppState:
    """Retrieve the application state object from within a websocket connection."""
    from tab_manager.ws import app

    # Set during lifespan function
    return app.state.app_state


async def get_app_state_request(request: Request) -> AppState:
    """Retrieve the application state object from within an http request."""
    # Set during lifespan function
    return request.app.state.app_state


async def get_websocket_request(request: Request) -> WebSocket:
    app_state = await get_app_state_request(request)
    return app_state.websocket
