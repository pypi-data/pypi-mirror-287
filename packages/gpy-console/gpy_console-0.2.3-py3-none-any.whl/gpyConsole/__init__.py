"""
gpy-console
"""

__version__ = "0.2.3"

try:
    import guilded
except ImportError:
    RuntimeError("Cannot find guilded namespace please use:\n" "pip install guilded.py")

from gpyConsole.console import ConsoleClient
from gpyConsole.converters import Converter
import gpyConsole.console_commands as console_commands
