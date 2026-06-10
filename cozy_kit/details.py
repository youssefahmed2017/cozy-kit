from rich.table import Table
from rich.console import Console


class Details:
    """
    Package detail and metadata utilities.
    """

    def __init__(self):
        self.console = Console()
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

    def about(self) -> Table:
        """
        Displays package details in a formatted table.

        Returns:
            Formatted details table.
        """
        about_table = Table(title="About this package")
        about_table.add_column("Detail", style="bold cyan")
        about_table.add_column("Value", style="bold magenta")

        for detail, value in self.details.items():
            about_table.add_row(detail, value)

        return about_table
