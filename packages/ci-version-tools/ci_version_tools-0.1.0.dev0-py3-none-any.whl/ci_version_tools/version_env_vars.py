import argparse
import importlib.metadata
import logging
import os
import sys

import semver

from .exceptions import CliError, VersionError
from .util import print_env

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        default="INFO",
    )

    subcommand = parser.add_subparsers(dest="command", required=True)

    subcommand.add_parser("version")

    parse_cmd = subcommand.add_parser("parse")
    parse_cmd.add_argument("env-variable-name", nargs="*")

    return parser.parse_args()


def make_parsed_env_variables(version_string: str, name_prefix: str) -> dict[str, str]:
    try:
        version = semver.Version.parse(version_string)
    except ValueError as e:
        raise VersionError(f"Unable to parse {version_string} as semver") from e

    variables = {
        f"{name_prefix}_MAJOR": str(version.major),
        f"{name_prefix}_MINOR": f"{version.major}.{version.minor}",
    }

    return variables


def main() -> None:
    args = parse_args()

    logging.basicConfig(level=args.log_level)

    try:
        if args.command == "version":
            distribution = importlib.metadata.distribution(__package__)
            print(importlib.metadata.version(distribution.metadata["Name"]))

            sys.exit(0)

        if args.command == "parse":
            variables: dict[str, str] = {}
            for var_name in args.env_variable_name:
                if var_name in os.environ:
                    variables.update(
                        make_parsed_env_variables(os.environ[var_name], var_name)
                    )

        print_env(variables)

    except (CliError, VersionError) as e:
        logger.error(e)
        sys.exit(1)
