from importlib.metadata import version

from cozy_kit import Details, __version__
from rich.console import Console
from rich.table import Table
from urllib import request

import argparse
import webbrowser
import pathlib
import platform
import sys
import json

console = Console()
details = Details()


def doctor():
    table = Table(title="cozy-kit Doctor Report")
    table.add_column("Check", style="cyan", justify="left")
    table.add_column("Status", style="magenta", justify="center")

    # Python version
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
    # Version check (using __version__ and __latest_version__)
    with console.status("[bold cyan]Checking cozy-kit version...[/bold cyan]"):
        local_version = __version__
        try:
            with request.urlopen(
                "https://pypi.org/pypi/cozy-kit/json", timeout=5
            ) as response:
                data = json.load(response)

            latest_version = data["info"]["version"]

        except Exception:
            table.add_row("cozy-kit latest", "[yellow]![/yellow] Unable to reach PyPI")
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
    console.print("[green]✓[/green] Finished!")
    console.print(table)


def main():
    parser = argparse.ArgumentParser(prog="cozy-kit")

    parser.add_argument(
        "--version", "-V", action="store_true", help="Show cozy-kit version"
    )
    parser.add_argument("--info", "-I", action="store_true", help="Show cozy-kit info")
    parser.add_argument(
        "--license", action="store_true", help="Show cozy-kit's license"
    )
    parser.add_argument(
        "--pypi",
        action="store_true",
        help="Open cozy-kit's PyPI page in the browser",
    )
    parser.add_argument(
        "--github",
        action="store_true",
        help="Open cozy-kit's GitHub repo in the browser",
    )
    parser.add_argument(
        "--homepage",
        action="store_true",
        help="Open cozy-kit's Homepage in the browser",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Open cozy-kit's Documentation website in the browser",
    )

    parser.add_argument(
        "--doctor", action="store_true", help="Run tests to check if everything is okay"
    )

    args = parser.parse_args()

    if args.version:
        console.print(
            f'[magenta italic]cozy-kit[/magenta italic] [cyan bold]v{version("cozy-kit")}[/cyan bold]'
        )

    elif args.info:
        console.print(details.about())
        console.print(
            f"[bright_cyan italic]This package[/bright_cyan italic] is a package made by [magenta bold]Youssef Ahmed[/magenta bold]. "
            f"\n[bright_cyan italic]The package's[/bright_cyan italic] latest version is "
            f"[magenta bold]v{version('cozy-kit')}[/magenta bold]."
        )

    elif args.license:
        console.print("[red bold]MIT[/red bold] License")

    elif args.pypi:
        webbrowser.open_new_tab("https://pypi.org/project/cozy-kit/")
        console.print(
            "[green]✓[/green] [cyan bold]Successfully opened cozy-kit's PyPI page[/cyan bold]"
        )

    elif args.github:
        webbrowser.open_new_tab("https://github.com/youssefahmed2017/cozy-kit/")
        console.print(
            "[green]✓[/green] [cyan bold]Successfully opened cozy-kit's GitHub repository[/cyan bold]"
        )

    elif args.homepage:
        webbrowser.open_new_tab("https://cozykit-home.vercel.app/")
        console.print(
            "[green]✓[/green] [cyan bold]Successfully opened cozy-kit's Homepage[/cyan bold]"
        )

    elif args.docs:
        webbrowser.open_new_tab("https://cozy-docs.vercel.app/")
        console.print(
            "[green]✓[/green] [cyan bold]Successfully opened cozy-kit's Documentation[/cyan bold]"
        )

    elif args.doctor:
        doctor()


if __name__ == "__main__":
    main()
