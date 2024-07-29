import logging
import shlex
import subprocess
from typing import Protocol

logger = logging.getLogger(__name__)


class GitInterface(Protocol):
    def get_all_tags(self, prefix: str) -> list[str]: ...


class GitCli:
    def cmd(self, args: list[str]) -> str:
        command = ["git"]
        command.extend(args)

        logger.debug("Executing `%s`", format(shlex.join(command)))
        p = subprocess.run(command, stdout=subprocess.PIPE, check=True, text=True)

        return p.stdout

    def get_all_tags(self, prefix: str) -> list[str]:
        return self.cmd(
            ["for-each-ref", "--format=%(refname:strip=2)", f"refs/tags/{prefix}"]
        ).split()
