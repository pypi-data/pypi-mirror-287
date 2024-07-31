from .ws import app
import uvicorn

import typer


fast_api = typer.Typer(name="TabManagerWebServer")


@fast_api.command()
def run(
    port: int = 8001,
    host: str = "0.0.0.0",
):
    uvicorn.run(app, port=port, host=host)
