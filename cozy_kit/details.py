from cozy_kit.text_studio import TextEditor
from cozy_kit.ui import CozyUI


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
        self.github = "github.com/youssefahmed2017/cozy-kit"
        self.pypi = "pypi.org/project/cozy-kit/"
        self.license = "MIT"

        self.details = {
            "author": self.author,
            "author_email": self.author_email,
            "description": self.description,
            "github": self.github,
            "pypi": self.pypi,
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
