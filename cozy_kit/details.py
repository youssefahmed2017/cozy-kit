from .text_studio import TextEditor
from .ui import CozyUI


class Details:
    """
    Package detail and metadata utilities.
    """

    def __init__(self):
        self.studio = TextEditor()
        self.ui = CozyUI()

        self.author = "Youssef Ahmed"
        self.author_email = "youssef.ahmed.29062017@gmail.com"
        self.description = "A cozy Python package with greetings, timers, and more."
        self.github = "https://github.com/youssefahmed2017/cozy-kit"
        self.pypi = "https://pypi.org/project/cozy-kit/"
        self.docs = "https://cozy-docs.vercel.app/"

        self.license = "MIT"

        self.details = {
            "Author": self.author,
            "Author email": self.author_email,
            "Description": self.description,
            "GitHub": self.github,
            "PyPI": self.pypi,
            "Our Docs": self.docs,
            "license": self.license,
        }

    def about(self) -> str:
        """
        Displays package details in a formatted table.

        Returns:
            Formatted details table.
        """

        rows = []

        for detail, value in self.details.items():
            rows.append([detail, value])

        return self.ui.cozy_table(
            headers=["Detail", "Value"],
            rows=rows,
        )
