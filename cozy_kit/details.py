from cozy_kit import text_studio
from cozy_kit import cozy_ui

class Details:
    def __init__(self):
        # FIX 5: studio was a module-level global instance — moved inside __init__
        # so each Details instance owns its own TextStudio, avoiding shared global state
        self.studio = text_studio.TextStudio()
        self.ui = cozy_ui.CozyUI()

        self.author = "Youssef Ahmed"

        self.author_email = (
            "youssef.ahmed.29062017@gmail.com"
        )

        self.description = (
            "A cozy Python package with greetings, timers, and text utilities."
        )

        self.github = (
            "github.com/youssefahmed2017/cozy-kit"
        )

        self.pypi = (
            "pypi.org/project/cozy-kit/"
        )

        self.license = "MIT"

        self.details = {
            "author": self.author,
            "author_email": self.author_email,
            "description": self.description,
            "github": self.github,
            "pypi": self.pypi,
            "license": self.license,
        }

    def about(self):
        rows = []

        for detail, value in self.details.items():
            rows.append([detail, value])

        return self.ui.cozy_table(
            headers=["Detail", "Value"],
            rows=rows,
        )