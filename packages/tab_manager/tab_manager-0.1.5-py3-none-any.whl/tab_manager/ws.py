"""Application that opens websocket server."""

from enum import StrEnum, auto
import uuid
import asyncio
from .schema import SocketPayload, TabsPayload, SocketCommand, HistoryModel, Window
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from typing import Any
from .logger import logger

from .state import AppState
from .dependencies import get_app_state, get_app_state_request
from .exc import BrowserNotConnected


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Setup application state."""
    app.state.app_state = AppState()
    yield


app = FastAPI(title="New WS server", lifespan=lifespan)


example_json = SocketPayload.example().model_dump_json()


class JobStatus(StrEnum):
    """Enumeration of Job statuses."""

    INITIALIZED = auto()
    FINISHED = auto()


print(example_json)


g_SEND_JOBS: dict[uuid, JobStatus] = {}
g_JOB_RESPONSES: dict[uuid, Any] = {}


async def send_command_ws(app_state: AppState, payload: SocketPayload) -> uuid.UUID:
    """Send a command to the websocket."""
    try:
        job_uuid = await send_payload(
            app_state.websocket,
            payload=payload,
        )

        # Wait until our tabs have been received..
        logger.info(f"Send message with uuid: {job_uuid}")

        count = 0
        while count < 100:
            if not is_job_finished(job_uuid):
                await asyncio.sleep(0.03)
                logger.info(f"Waiting for job: {job_uuid}")
                count += 1
            else:
                break

        return job_uuid
    except BrowserNotConnected:
        raise HTTPException(
            400,
            detail="Browser extension not connected via websocket.",
        )


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    app_state: AppState = Depends(get_app_state),
):
    await websocket.accept()
    app_state.websocket = websocket
    try:
        while True:
            data = await websocket.receive_text()
            socket_payload = SocketPayload.model_validate_json(data)

            if socket_payload.command:
                match socket_payload.command:
                    case SocketCommand.LIST_TABS:
                        # logger.critical(socket_payload.payload)
                        tabs_payload = TabsPayload(**socket_payload.payload)
                        logger.info("Received [list-tabs]")

                        if socket_payload.job_id is not None:
                            global g_JOB_RESPONSES
                            job_uuid = socket_payload.job_uuid()
                            g_JOB_RESPONSES[job_uuid] = tabs_payload

                        for t in tabs_payload.tabs:
                            logger.info(str(t))

                    case SocketCommand.LIST_HISTORY:
                        logger.info("Received [list-history]")

                        if socket_payload.job_id is not None:
                            job_uuid = socket_payload.job_uuid()
                            g_JOB_RESPONSES[job_uuid] = socket_payload.payload

                    case SocketCommand.LIST_WINDOWS:
                        if socket_payload.job_id is not None:
                            job_uuid = socket_payload.job_uuid()
                            g_JOB_RESPONSES[job_uuid] = socket_payload.payload

            if socket_payload.job_id is not None:
                global g_SEND_JOBS
                job_uuid = socket_payload.job_uuid()
                g_SEND_JOBS[job_uuid] = JobStatus.FINISHED
                logger.info(f"Finished job with uuid: {job_uuid}")

    except WebSocketDisconnect:
        print("Websocket disconnected!")


async def send_payload(websocket: WebSocket, payload: SocketPayload) -> uuid.UUID:
    """Send a payload through our websocket."""
    if websocket is None:
        logger.critical("No websocket connected!")
        raise BrowserNotConnected()

    global g_SEND_JOBS
    job_id = uuid.uuid4()
    g_SEND_JOBS[job_id] = JobStatus.INITIALIZED
    payload.job_id = str(job_id)

    await websocket.send_json(payload.model_dump())
    return job_id


def is_job_finished(job_id: uuid.UUID) -> bool:
    """Check if a job has completed."""
    if job_id not in g_SEND_JOBS:
        return False
    return g_SEND_JOBS[job_id] == JobStatus.FINISHED


@app.get("/tabs")
async def get_tabs(app_state: AppState = Depends(get_app_state_request)) -> TabsPayload:
    """Retrieve a list of tabs from the active window."""
    job_uuid = await send_command_ws(app_state, SocketPayload.list_tabs())
    return g_JOB_RESPONSES[job_uuid]


@app.get("/tabs/prev")
async def prev_tab(app_state: AppState = Depends(get_app_state_request)) -> uuid.UUID:
    """Retrieve a list of tabs from the active window."""
    return await send_command_ws(app_state, SocketPayload.prev_tab())


@app.get("/tabs/next")
async def next_tab(app_state: AppState = Depends(get_app_state_request)) -> uuid.UUID:
    """Retrieve a list of tabs from the active window."""
    return await send_command_ws(app_state, SocketPayload.next_tab())


@app.get("/tabs/focus")
async def focus_tab(
    tab_id: int,
    app_state: AppState = Depends(get_app_state_request),
) -> uuid.UUID:
    """Retrieve a list of tabs from the active window."""
    return await send_command_ws(app_state, SocketPayload.focus_tab(tab_id))


@app.get("/tabs/move")
async def move_tab(
    tab_id: int,
    window_id: int,
    app_state: AppState = Depends(get_app_state_request),
) -> uuid.UUID:
    """Retrieve a list of tabs from the active window."""
    return await send_command_ws(app_state, SocketPayload.move_tab(tab_id, window_id))


@app.get("/windows")
async def list_windows(
    app_state: AppState = Depends(get_app_state_request),
) -> list[Window]:
    """List windows."""
    job_uuid = await send_command_ws(app_state, SocketPayload.list_windows())
    windows = g_JOB_RESPONSES[job_uuid]["windows"]
    return [Window(**window) for window in windows]


@app.get("/windows/create")
async def create_window(
    app_state: AppState = Depends(get_app_state_request),
) -> uuid.UUID:
    """Retrieve a list of tabs from the active window."""
    return await send_command_ws(app_state, SocketPayload.create_window())


@app.get("/history")
async def list_history(
    app_state: AppState = Depends(get_app_state_request),
) -> list[HistoryModel]:
    """Retrieve a list of History objects."""
    job_uuid = await send_command_ws(app_state, SocketPayload.list_history())
    history_dicts: list[dict] = g_JOB_RESPONSES[job_uuid]["history"]
    return [HistoryModel(**hm) for hm in history_dicts]


@app.get("/")
def hello_app() -> dict:
    return dict(detail="Hello app!")
