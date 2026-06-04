import importlib.metadata as lib

from .greeting import Greeting
from .timer import Timer
from .text_studio import TextEditor
from .text_studio import TextCustomizations
from .details import Details
from .ui import CozyUI
from .updater import check_for_updates
from .settings import settings

__version__ = lib.version("cozy-kit")
__version_info__ = tuple(map(int, __version__.split(".")))

if settings.notice_if_on_older_update:
    check_for_updates()

__all__ = [
    "Greeting",
    "Timer",
    "TextEditor",
    "Details",
    "CozyUI",
    "__version__",
    "__version_info__",
    "TextCustomizations",
    "settings",
]
