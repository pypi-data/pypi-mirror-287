"""This module provides the RP To-Do CLI."""
import asyncio
# rptodo/cli.py

from typing import Optional


import typer
from rich import print as rprint
from zinley.v2.code.main import start

from zinley import __app_name__, __version__
from zinley import api_key, deployment_id, max_tokens, endpoint

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command("start")
def sample_func_start(project_path):
    rprint(f"[red bold]project path[/red bold] [yellow]{project_path}[yello]")
    asyncio.run(start(project_path, api_key, max_tokens, endpoint, deployment_id))


# @app.command("scan_project")
# def sample_func_scan_project(project_path):
#     asyncio.run(scan_project(project_path, api_key, max_tokens, endpoint, deployment_id))