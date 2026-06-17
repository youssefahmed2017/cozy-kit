# ============= cozy_kit/__init__.py =============

# ============= IMPORTS =============
import importlib.metadata as lib

from cozy_kit.greeting import Greeting
from cozy_kit.timer import Timer
from cozy_kit.text_studio import TextEditor
from cozy_kit.text_studio import TextCustomizations
from cozy_kit.details import Details
from cozy_kit.ui import CozyUI
from cozy_kit.mailer import SMTPMailer

# ============= VARIABLES =============

__version__ = lib.version("cozy-kit")
__version_info__ = tuple(map(int, __version__.split(".")))

__all__ = [
    "Greeting",
    "Timer",
    "TextEditor",
    "Details",
    "CozyUI",
    "__version__",
    "__version_info__",
    "TextCustomizations",
    "SMTPMailer",
]
