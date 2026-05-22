import importlib.metadata as lib
from .greeting import Greeting
from .timer import Timer
from .text_studio import TextEditor, TextCustomizations
from .details import Details
from .cozy_ui import CozyUI
from .updater import check_for_updates

check_for_updates()

__version__ = lib.version("cozy-kit")
__version_info__ = tuple(map(int, __version__.split(".")))

__all__ = ['Greeting', 'Timer', 'TextEditor', 'Details', 'CozyUI', '__version__', '__version_info__', 'TextCustomizations']