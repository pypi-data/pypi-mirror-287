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


class Pep440State:
    NAMED_IDENTIFIER = 1
    PRERELEASE_NR = 2
    DEV_NR = 3


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
    dev_identifier: str = "dev",
    dev_nr: Optional[int] = None,
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
        identifiers = (source_version.prerelease or dev_identifier).split(".")

        prerelease_parts = []
        skip_next_nr = False
        dev_identifier_present = False
        for identifier in identifiers:
            if skip_next_nr:
                skip_next_nr = False
                if identifier.isnumeric():
                    continue

            prerelease_parts.append(identifier)

            if identifier.lower() == dev_identifier.lower():
                dev_identifier_present = True
                if dev_nr is not None:
                    prerelease_parts.append(str(dev_nr))
                    skip_next_nr = True

        if not dev_identifier_present:
            prerelease_parts.append(dev_identifier)
            if dev_nr is not None:
                prerelease_parts.append(str(dev_nr))

        version = source_version.replace(
            prerelease=".".join(prerelease_parts),
            build=None,
        )

    return version


def version_as_pep440(
    version: semver.Version,
    dev_identifier: str = "dev",
) -> str:
    if not version.prerelease:
        return str(version.finalize_version())
    else:
        identifiers = version.prerelease.split(".")
        state = Pep440State.NAMED_IDENTIFIER
        prerelease_segment_parts = []
        dev_release_segment_parts = []
        for identifier in identifiers:
            if state == Pep440State.PRERELEASE_NR:
                state = Pep440State.NAMED_IDENTIFIER
                if identifier.isnumeric():
                    prerelease_segment_parts.append(identifier)
                    continue
            elif state == Pep440State.DEV_NR:
                state = Pep440State.NAMED_IDENTIFIER
                if identifier.isnumeric():
                    dev_release_segment_parts.append(identifier)
                    continue

            if m := re.match(r"^(?P<name>alpha|beta|rc)$", identifier.lower()):
                if prerelease_segment_parts:
                    raise VersionConversionError(
                        "Multiple pre-release identifiers detected while "
                        f"converting {version} to PEP440"
                    )
                prerelease_segment_parts.append(
                    {"alpha": "a", "beta": "b", "rc": "rc"}[m["name"]]
                )
                state = Pep440State.PRERELEASE_NR
            elif identifier.lower() == dev_identifier.lower():
                if dev_release_segment_parts:
                    raise VersionConversionError(
                        "Multiple dev identifiers detected while "
                        f"converting {version} to PEP440"
                    )

                dev_release_segment_parts.append("dev")
                state = Pep440State.DEV_NR
            else:
                raise VersionConversionError(
                    f"Unrecognized identifier {identifier} found while "
                    f"converting {version} to PEP440"
                )

        version_parts = [str(version.finalize_version())]

        if len(prerelease_segment_parts) == 1:
            prerelease_segment_parts.append("0")

        if len(dev_release_segment_parts) == 1:
            dev_release_segment_parts.append("0")

        if prerelease_segment_parts:
            version_parts.append("".join(prerelease_segment_parts))

        if dev_release_segment_parts:
            dev_release_segment_parts.insert(0, ".")
            version_parts.append("".join(dev_release_segment_parts))

        return "".join(version_parts)


def make_env_variables(
    version: semver.Version,
    name_prefix: str,
    is_latest: bool,
    dev_identifier: str,
    extra_output_formats: Optional[set[ExtraOutputFormats]] = None,
) -> dict:
    variables = {
        f"{name_prefix}_SEMVER": str(version),
        f"{name_prefix}_SEMVER_MAJOR": str(version.major),
        f"{name_prefix}_SEMVER_MINOR": f"{version.major}.{version.minor}",
    }

    if version.prerelease:
        variables[f"{name_prefix}_IS_PRE_RELEASE"] = "1"
    else:
        variables[f"{name_prefix}_IS_RELEASE"] = "1"

    if is_latest and not version.prerelease:
        variables[f"{name_prefix}_IS_LATEST_RELEASE"] = "1"

    if extra_output_formats is not None:  # noqa: SIM102
        if ExtraOutputFormats.PEP440 in extra_output_formats:
            variables[f"{name_prefix}_PEP440"] = version_as_pep440(
                version, dev_identifier=dev_identifier
            )

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
    parser.add_argument("--dev-identifier", default="dev")
    parser.add_argument("--dev-nr", type=int)
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
                dev_identifier=args.dev_identifier,
                dev_nr=args.dev_nr,
            )

            all_released_versions = get_all_git_releases(args.git_version_tag_prefix)

            if all_released_versions:
                latest = version >= max(all_released_versions)
            else:
                latest = True

            variables = make_env_variables(
                version,
                name_prefix=args.output_var_prefix,
                is_latest=latest,
                dev_identifier=args.dev_identifier,
                extra_output_formats=extra_output_formats,
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
