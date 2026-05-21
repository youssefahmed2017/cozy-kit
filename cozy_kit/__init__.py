import importlib.metadata as lib
from .greeting import Greeting
from .timer import Timer
from .text_studio import TextStudio
from .details import Details
from .cozy_ui import CozyUI

__version__ = lib.version("cozy-kit")
__version_info__ = tuple(map(int, __version__.split(".")))

__all__ = ['Greeting', 'Timer', 'TextStudio', 'Details', 'CozyUI', '__version__', '__version_info__']