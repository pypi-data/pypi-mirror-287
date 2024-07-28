from slidge.util.util import get_version  # noqa: F401

# import everything for automatic subclasses discovery by slidge core
from . import command, contact, gateway, group, session

__all__ = "session", "gateway", "contact", "group", "command"

__version__ = "0.2.0alpha1"
