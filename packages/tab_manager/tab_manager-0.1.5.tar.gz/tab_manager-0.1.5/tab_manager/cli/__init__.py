"""Command line interface to this webserver/firefox extension."""

import typer
import requests
import json
from ..schema import TabModel


cli = typer.Typer(name="TabManager")


def get_tabs(host: str = "localhost", port: int = 8001) -> list[TabModel]:
    """Return a list of tabs."""
    response = requests.get(f"http://{host}:{port}/tabs")
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    tabs = json_dict["tabs"]
    return [TabModel(**t) for t in tabs]


@cli.command(name="list")
def list_tabs(host: str = "localhost", port: int = 8001):
    """Request that the server lists all tabs."""
    response = requests.get(f"http://{host}:{port}/tabs")
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    tabs = json_dict["tabs"]
    for t in tabs:
        print(json.dumps(t))


@cli.command(name="next")
def next_tab(host: str = "localhost", port: int = 8001):
    """Focus on the next tab."""
    response = requests.get(f"http://{host}:{port}/tabs/next")
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    print(json_dict)


@cli.command(name="prev")
def prev_tab(host: str = "localhost", port: int = 8001):
    """Focus on the previous tab."""
    response = requests.get(f"http://{host}:{port}/tabs/prev")
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    print(json_dict)


@cli.command(name="focus")
def focus_tab(tab_id: int, host: str = "localhost", port: int = 8001):
    """Focus on the tab with the given id."""
    response = requests.get(
        f"http://{host}:{port}/tabs/focus",
        params=dict(tab_id=tab_id),
    )
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    print(json_dict)


# @cli.command(name="windows")
# def list_window_ids(host: str = "localhost", port: int = 8001):
#     """List all the window ids that are active."""
#     tabs = get_tabs(host, port)
#     window_ids = set()
#     for t in tabs:
#         window_ids.add(t.windowId)
#     print(window_ids)
#
#


@cli.command(name="windows")
def list_window_ids(host: str = "localhost", port: int = 8001):
    """List all the window ids that are active."""
    response = requests.get(
        f"http://{host}:{port}/windows",
    )
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    for window in json_dict:
        print(json.dumps(window))
    # window_ids = set()
    # for t in tabs:
    #     window_ids.add(t.windowId)
    # print(window_ids)


@cli.command(name="move")
def move_tab(tab_id: int, window_id: int, host: str = "localhost", port: int = 8001):
    """Move a tab to a different window."""
    response = requests.get(
        f"http://{host}:{port}/tabs/move",
        params=dict(window_id=window_id, tab_id=tab_id),
    )
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    print(json_dict)


@cli.command(name="window")
def create_window(host: str = "localhost", port: int = 8001):
    """Move a tab to a different window."""
    response = requests.get(
        f"http://{host}:{port}/windows/create",
    )
    json_dict = response.json()
    assert response.status_code == 200, str(json_dict)
    print(json_dict)


@cli.command(name="history")
def list_history(host: str = "localhost", port: int = 8001):
    """Move a tab to a different window."""
    response = requests.get(
        f"http://{host}:{port}/history",
    )
    json_dict: list[dict] = response.json()
    assert response.status_code == 200, str(json_dict)
    for history in json_dict:
        print(json.dumps(history))


@cli.command(name="split")
def split_tabs(host: str = "localhost", port: int = 8001):
    """Split all tabs into their own window."""
    window_ids = set()
    tabs = get_tabs(host, port)
    for t in tabs:
        window_ids.add(t.windowId)

    n_windows = len(window_ids)
    for tab, window in zip(tabs[:n_windows], window_ids):
        move_tab(tab.id, window, host, port)

    for tab in tabs[n_windows:]:
        create_window(host, port)


@cli.command(name="congregate")
def congregate(window_id: int, host: str = "localhost", port: int = 8001):
    """Congregate all tabs to a single window."""
    tabs = get_tabs(host, port)
    tabs_not_in_window = [t for t in tabs if t.windowId != window_id]
    print(tabs_not_in_window)

    for tab in tabs_not_in_window:
        move_tab(tab.id, window_id)


if __name__ == "__main__":
    cli()
