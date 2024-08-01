"""An interface to the ProBullStats website."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from loguru import logger

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"


logger.disable("probullstats")
logger.info("This message should never be displayed.")

__all__ = [
    "__version__",
    "logger",
]
