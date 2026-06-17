# ============= cozy_kit/_internal/cli_doctor.py =============

# ============= IMPORTS =============
from cozy_kit import Details
from cozy_kit import __version__
from rich.console import Console
from rich.table import Table
from urllib import request

import platform
import sys
import json
import pathlib

# ============= OBJECTS =============

console = Console()
details = Details()

# ============= doctor FUNCTION =============


def doctor():
    # Create table
    table = Table(title="cozy-kit Doctor Report")
    table.add_column("Check", style="cyan", justify="left")
    table.add_column("Status", style="magenta", justify="center")

    # Check Python version
    with console.status("[cyan]Checking Python version...[/cyan]"):
        py_ver = platform.python_version()
        if sys.version_info >= (3, 8):
            table.add_row("Python >= 3.8", f"[green]✓[/green] {py_ver}")
        else:
            table.add_row("Python >= 3.8", f"[red]✗[/red] {py_ver}")

        console.print("[green]✓[/green] Checked Python version")

    # Import test
    with console.status("[cyan]Testing imports...[/cyan]"):
        try:
            import cozy_kit

            table.add_row("Import cozy-kit", "[green]✓[/green]")
        except Exception as e:
            table.add_row("Import cozy-kit", f"[red]✗[/red] {e}")

        console.print("[green]✓[/green] Tested imports")
    # Version check (using __version__ and urllib request)
    with console.status("[bold cyan]Checking cozy-kit version...[/bold cyan]"):
        local_version = __version__
        latest_version = None

        try:
            with request.urlopen(
                "https://pypi.org/pypi/cozy-kit/json", timeout=5
            ) as response:
                data = json.load(response)

            latest_version = data["info"]["version"]

        except Exception:
            table.add_row("cozy-kit latest", "[yellow]![/yellow] Unable to reach PyPI")

        if latest_version is not None:
            if local_version == latest_version:
                table.add_row("cozy-kit latest", f"[green]✓[/green] {local_version}")
            else:
                table.add_row(
                    "cozy-kit latest",
                    f"[yellow]![/yellow] Installed: {local_version}, Latest: {latest_version}",
                )

        console.print("[green]✓[/green] Checked cozy-kit version")

    # main.py check
    with console.status("[cyan]Checking main.py...[/cyan]"):
        if pathlib.Path("main.py").exists():
            table.add_row("main.py exists", "[green]✓[/green]")
        else:
            table.add_row("main.py exists", "[yellow]![/yellow] Not found")

        console.print("[green]✓[/green] Checked main.py")

    # Show result

    console.print("[green]✓[/green] Finished!")
    console.print(table)
