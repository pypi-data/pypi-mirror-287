"""Command line interface to this webserver/firefox extension."""

import typer
import requests
import json


cli = typer.Typer(name="TabManager")


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


if __name__ == "__main__":
    cli()
