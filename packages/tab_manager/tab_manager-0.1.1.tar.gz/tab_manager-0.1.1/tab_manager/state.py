from dataclasses import dataclass
from fastapi import WebSocket
from .schema import SocketPayload


@dataclass
class Tab:
    """A Firefox tab."""

    title: str
    id: int


@dataclass
class Window:
    """A Firefox window with a list of tabs."""

    tabs: list[Tab]


@dataclass
class AppState:
    """Keep track of shared application state."""

    websocket: WebSocket = None
    window: Window = None
