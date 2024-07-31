"""Schema for communicating with the front end."""

from __future__ import annotations

from enum import StrEnum, auto

from pydantic import BaseModel, ConfigDict
from typing import Optional
import uuid


class SocketCommand(StrEnum):
    """Enumeration of all possible commands."""

    LIST_TABS = auto()
    NEXT_TAB = auto()
    PREV_TAB = auto()
    FOCUS_TAB = auto()
    MOVE_TAB = auto()
    CREATE_WINDOW = auto()
    LIST_HISTORY = auto()


class TabModel(BaseModel):
    """Pydantic model for capturing information about tabs."""

    id: int
    title: str
    windowId: int
    url: Optional[str] = None

    model_config = ConfigDict(extra="ignore")


class HistoryModel(BaseModel):
    """Pydantic model encapsulating a single history entry."""

    id: str
    visitCount: int
    title: Optional[str] = None
    url: str
    lastVisitTime: int


class TabsPayload(BaseModel):
    """Pydantic payload for receiving tabs."""

    tabs: list[TabModel]

    model_config = ConfigDict(extra="ignore")


class FocusTab(BaseModel):
    tab_id: int


class MoveTab(BaseModel):
    tab_id: int
    window_id: int


class SocketPayload(BaseModel):
    """Pydantic model of messages sent between extension and cli."""

    job_id: Optional[str] = None
    content: Optional[str] = None
    command: Optional[SocketCommand] = None
    payload: Optional[dict | FocusTab | MoveTab] = None

    def job_uuid(self) -> uuid.UUID:
        return uuid.UUID(self.job_id)

    @staticmethod
    def example() -> SocketPayload:
        """Retrieve an example payload."""
        return SocketPayload(content="Hello there")

    @staticmethod
    def list_tabs() -> SocketPayload:
        return SocketPayload(command=SocketCommand.LIST_TABS)

    @staticmethod
    def next_tab() -> SocketPayload:
        return SocketPayload(command=SocketCommand.NEXT_TAB)

    @staticmethod
    def prev_tab() -> SocketPayload:
        return SocketPayload(command=SocketCommand.PREV_TAB)

    @staticmethod
    def focus_tab(tab_id: int):
        return SocketPayload(
            command=SocketCommand.FOCUS_TAB,
            payload=FocusTab(tab_id=tab_id),
        )

    @staticmethod
    def move_tab(tab_id: int, window_id: int):
        return SocketPayload(
            command=SocketCommand.MOVE_TAB,
            payload=MoveTab(tab_id=tab_id, window_id=window_id),
        )

    @staticmethod
    def create_window():
        return SocketPayload(
            command=SocketCommand.CREATE_WINDOW,
        )

    @staticmethod
    def list_history():
        return SocketPayload(
            command=SocketCommand.LIST_HISTORY,
        )
