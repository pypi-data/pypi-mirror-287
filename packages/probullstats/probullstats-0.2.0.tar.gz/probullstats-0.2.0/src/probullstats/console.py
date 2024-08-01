"""The probullstats package CLI."""

from __future__ import annotations

import argparse
import sys

from probullstats import __name__ as program_name
from probullstats import __version__ as program_version
from probullstats import logger


def create_parser() -> argparse.ArgumentParser:
    """Create an input configuration parser.

    Returns:
        argparse.ArgumentParser: An input configuration parser.

    Examples:
        A parser can be used as is, have argument groups added, or have subparsers added.

        >>> parser = create_parser()
        >>> parser.parse_args(["--fail"])
        Namespace(fail=True)
    """
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=(
            "Pull data from the ProBullStats website and collate raw data to create reports or do custom analysis."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s v{program_version}")
    parser.add_argument("-f", "--fail", action="store_true", help="Placeholder until real functionality implemented.")

    return parser


def main(args: argparse.Namespace) -> int:
    """Scriptable entrypoint.

    Args:
        args (argparse.Namespace): Parsed script configuration input.

    Returns:
        int: The returncode.  Zero for success, non-zero otherwise.

    Examples:
        >>> parser = create_parser()
        >>> args = parser.parse_args(["--fail"])
        >>> main(args)
        1
    """
    logger.debug("Entering main")
    if args.fail:
        msg = "The '-f' switch was set."
        logger.debug(msg)
        raise RuntimeError(msg)

    sys.stdout.write("Imagine this is the collated data you requested.")
    logger.debug("Leaving main")
    return 0


@logger.catch
def cli() -> None:
    """Main entrypoint for terminal execution."""
    parser = create_parser()
    args = parser.parse_args()

    # logger.enable("probullstats")

    logger.trace("Log level enabled")
    logger.debug("Log level enabled.")
    logger.info("Log level enabled.")
    logger.success("Log level enabled.")
    logger.warning("Log level enabled.")
    logger.error("Log level enabled.")
    logger.critical("Log level enabled.")

    returncode = main(args)

    sys.exit(returncode)
