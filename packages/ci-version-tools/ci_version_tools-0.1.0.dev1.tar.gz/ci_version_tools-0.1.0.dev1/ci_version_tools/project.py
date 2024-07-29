import argparse
import contextlib
import importlib.metadata
import logging
import pathlib
import re
import sys
from enum import Enum
from typing import Optional

import semver

from . import git
from .exceptions import (
    CliError,
    TargetAlreadyReleasedError,
    VersionConversionError,
    VersionError,
    VersionMismatchError,
)
from .util import print_env

logger = logging.getLogger(__name__)

DEFAULT_GIT_INTERFACE = git.GitCli()


class ExtraOutputFormats(Enum):
    PEP440 = 1


def get_all_git_releases(
    version_tag_prefix: str, git_interface: git.GitInterface = DEFAULT_GIT_INTERFACE
) -> set:
    versions = set()
    for tag in git_interface.get_all_tags(version_tag_prefix):
        try:
            version = semver.Version.parse(tag.removeprefix(version_tag_prefix))
        except ValueError:
            logger.debug(
                "Git tag %s had the correct prefix %s"
                "but didn't parse as a valid semver",
                tag,
                version_tag_prefix,
            )
            continue

        logger.debug("Found tagged release %s", version)
        versions.add(version)

    return versions


def derive_version(
    source_version: semver.Version,
    git_version_tag_prefix: str = "v",
    git_tag: Optional[str] = None,
    prerelease_nr: Optional[int] = None,
) -> semver.Version:
    tag_version = None

    if git_tag is not None and git_tag.startswith(git_version_tag_prefix):
        with contextlib.suppress(ValueError):
            tag_version = semver.Version.parse(
                git_tag.removeprefix(git_version_tag_prefix)
            )

    # Release build.
    if tag_version is not None:
        version = source_version.finalize_version()

        if tag_version != version:
            raise VersionMismatchError(
                f"Version {source_version} in the version source does not match the "
                "version {tag_version} in the Git tag"
            )
    else:
        prerelease_parts = [source_version.prerelease or "dev"]

        if prerelease_nr is not None:
            prerelease_parts.append(str(prerelease_nr))

        version = source_version.replace(
            prerelease=".".join(prerelease_parts),
            build=None,
        )

    return version


# TODO: Fix missing nr -> default to 0.
def version_as_pep440(version: semver.Version) -> str:
    if not version.prerelease:
        return str(version.finalize_version())
    else:
        pre_release_segment = None
        dev_release_segment = None
        identifiers = version.prerelease.split("-")
        for identifier in identifiers:
            if m := re.match(
                r"^(?P<name>a|alpha|b|beta|rc)(\.(?P<nr>\d+))?$", identifier.lower()
            ):
                if pre_release_segment is not None:
                    raise VersionConversionError(
                        "Multiple pre-release identifiers detected while "
                        f"converting {version} to PEP440"
                    )
                segment_parts = [
                    {"a": "a", "alpha": "a", "b": "b", "beta": "b", "rc": "rc"}[
                        m["name"]
                    ]
                ]

                segment_parts.append(m["nr"] or "0")

                pre_release_segment = "".join(segment_parts)
            elif m := re.match(
                r"^(?P<name>(dev|snapshot))(\.(?P<nr>\d+))?$", identifier.lower()
            ):
                if dev_release_segment is not None:
                    raise VersionConversionError(
                        "Multiple dev identifiers detected while "
                        f"converting {version} to PEP440"
                    )

                dev_release_segment = "dev{}".format(m["nr"] or "0")
            else:
                raise VersionConversionError(
                    f"Unrecognized identifier {identifier} found while "
                    f"converting {version} to PEP440"
                )

        version_parts = [str(version.finalize_version())]
        if pre_release_segment is not None:
            version_parts.append(pre_release_segment)

        if dev_release_segment is not None:
            version_parts.append(f".{dev_release_segment}")

        return "".join(version_parts)


def make_env_variables(
    version: semver.Version,
    name_prefix: str,
    is_latest: bool,
    extra_output_formats: Optional[set[ExtraOutputFormats]] = None,
) -> dict:
    variables = {
        f"{name_prefix}_SEMVER": str(version),
        f"{name_prefix}_SEMVER_MAJOR": str(version.major),
        f"{name_prefix}_SEMVER_MINOR": f"{version.major}.{version.minor}",
        f"{name_prefix}_IS_PRE_RELEASE": "1" if version.prerelease else "0",
        f"{name_prefix}_IS_LATEST_RELEASE": "1" if is_latest else "0",
    }

    if extra_output_formats is not None:  # noqa: SIM102
        if ExtraOutputFormats.PEP440 in extra_output_formats:
            variables[f"{name_prefix}_PEP440"] = version_as_pep440(version)

    return variables


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        default="INFO",
    )
    parser.add_argument("--version-source-file", type=pathlib.Path)
    parser.add_argument("--git-version-tag-prefix", default="v")
    parser.add_argument("--output-var-prefix", default="VERSION")
    # CI_COMMIT_TAG
    parser.add_argument("--git-tag")
    # CI_PIPELINE_IID
    parser.add_argument("--prerelease-nr")
    parser.add_argument(
        "--no-fail-if-target-release-exists", action="store_true", default=False
    )

    subcommand = parser.add_subparsers(dest="command", required=True)

    subcommand.add_parser("version")

    env_vars_cmd = subcommand.add_parser("env-vars")
    env_vars_cmd.add_argument("--with-pep440", action="store_true", default=False)

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    logging.basicConfig(level=args.log_level)

    try:
        if args.command == "version":
            distribution = importlib.metadata.distribution(__package__)
            print(importlib.metadata.version(distribution.metadata["Name"]))

            sys.exit(0)

        if args.version_source_file is not None:
            with open(args.version_source_file) as f:
                version = semver.Version.parse(f.read().rstrip())
        # elif:
        else:
            raise CliError("No version source provided")

        if args.command == "env-vars":
            extra_output_formats = set()
            if args.with_pep440:
                extra_output_formats.add(ExtraOutputFormats.PEP440)

            version = derive_version(
                version,
                args.git_version_tag_prefix,
                git_tag=args.git_tag,
                prerelease_nr=args.prerelease_nr,
            )

            all_released_versions = get_all_git_releases(args.git_version_tag_prefix)

            if all_released_versions:
                latest = version >= max(all_released_versions)
            else:
                latest = True

            variables = make_env_variables(
                version, args.output_var_prefix, latest, extra_output_formats
            )
            print_env(variables)

            target_release_version = version.finalize_version()
            if version.prerelease and target_release_version in all_released_versions:
                raise TargetAlreadyReleasedError(
                    f"Version {version} targets {target_release_version} which "
                    "is already released"
                )

    except (CliError, VersionError) as e:
        logger.error(e)
        sys.exit(1)

    except TargetAlreadyReleasedError as e:
        if not args.no_fail_if_target_release_exists:
            logger.error(e)
            sys.exit(2)
