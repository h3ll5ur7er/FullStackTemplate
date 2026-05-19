from my_fullstack_template.di.container import AppContainer
from typer import Typer
from rich.console import Console
from ..helpers import coro
from ..di.container import get_container
from ..api_client import Client
from ..api_client.api.status import get_status as get_status_api

cli = Typer(name="status", no_args_is_help=True, help="Check the status of the API server")
console = Console()

@cli.command()
@coro
async def get_status():
    with get_container().api_client() as client:
        response = await get_status_api.asyncio(client=client)
        print(response)
        console.print(f"My Fullstack Template API status: [green]{response.status}[/green]")

