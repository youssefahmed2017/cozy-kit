# ============= cozy_kit/cli.py =============

# ============= IMPORTS =============
from importlib.metadata import version
from rich.console import Console
from cozy_kit import Details
from cozy_kit._internal.cli_doctor import doctor

import argparse
import webbrowser

# ============= OBJECTS =============

console = Console()
details = Details()

# ============= MAIN FUNCTION =============


def main():
    parser = argparse.ArgumentParser(prog="cozy-kit")

    # ============= ARGUMENTS =============

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
        "--doctor",
        action="store_true",
        help="Run tests to check if everything is okay",
    )

    args = parser.parse_args()

    # ============= CASES =============

    if args.version:
        console.print(
            f'[magenta italic]cozy-kit[/magenta italic] [cyan bold]v{version("cozy-kit")}[/cyan bold]'
        )

    elif args.info:
        details.about()
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
