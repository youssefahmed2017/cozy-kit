# ============= cozy_kit/details.py =============

# ============= IMPORTS =============

from rich.table import Table
from rich.console import Console

# ============= Details CLASS =============


class Details:
    """
    Package metadata.
    Metadata:
        Author: Youssef Ahmed
        Author email: Youssef Ahmed
        Description: A cozy Python package with greetings, timers, and more.
        GitHub: https://github.com/youssefahmed2017/cozy-kit
        PyPI: https://pypi.org/project/cozy-kit/
        Homepage: https://github.com/youssefahmed2017/cozy-kit
        Our Docs: https://cozy-docs.verceel.app/
        License: MIT
    """

    def __init__(self):
        self.console = Console()

        # ============= DETAILS =============

        self.author = "Youssef Ahmed"
        self.author_email = "youssef.ahmed.29062017@gmail.com"
        self.description = "A cozy Python package with greetings, timers, and more."
        self.github = "https://github.com/youssefahmed2017/cozy-kit/"
        self.pypi = "https://pypi.org/project/cozy-kit/"
        self.homepage = "https://cozykit-home.vercel.app/"
        self.docs = "https://cozy-docs.vercel.app/"

        self.license = "MIT"

        self.details = {
            "Author": self.author,
            "Author email": self.author_email,
            "Description": self.description,
            "GitHub": self.github,
            "PyPI": self.pypi,
            "Homepage": self.homepage,
            "Our Docs": self.docs,
            "license": self.license,
        }

    def about(self) -> None:
        """
        Displays package details in a formatted table.

        Returns:
            Formatted details table with all the metadata.
        """
        # Create table
        about_table = Table(title="About this package")
        about_table.add_column("Detail", style="bold cyan")
        about_table.add_column("Value", style="bold magenta")

        for detail, value in self.details.items():
            about_table.add_row(detail, value)

        # Show table

        self.console.print(about_table)
