"""Application entrypoint."""

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from sys import stdout
from typing import Self

from ._file import VersionFile
from ._pyproject import parse_package_paths
from ._ver import IncrementKind, Version


def _version_argument_type(value: str) -> Version:
    return Version.load(value)


_version_argument_type.__name__ = "version"


@dataclass(frozen=True)
class Args:
    """Parsed CLI args."""

    action: IncrementKind | Version
    project_dir: Path

    @classmethod
    def parse_argv(cls: type[Self]) -> "Args":
        """Parse CLI arguments."""
        import poetry_incr_version

        parser = ArgumentParser()
        parser.add_argument("project_dir", type=Path)
        parser.add_argument("--major", action="store_true")
        parser.add_argument("--minor", action="store_true")
        parser.add_argument("--patch", action="store_true")
        parser.add_argument(
            "--set",
            action="store",
            type=_version_argument_type,
            required=False,
            default=None,
            metavar="VERSION",
        )
        parser.add_argument(
            "--version", action="version", version=poetry_incr_version.__version__
        )
        args = parser.parse_args()

        option_count = args.major + args.minor + args.patch + (args.set is not None)

        if option_count == 0:
            parser.error(
                "One option among --major, --minor, --patch and --set is required."
            )

        if option_count > 1:
            parser.error(
                "Options --major, --minor, --patch and --set are mutually exclusive."
            )

        if args.major:
            action = IncrementKind.MAJOR
        elif args.minor:
            action = IncrementKind.MINOR
        elif args.patch:
            action = IncrementKind.PATCH
        else:
            action = args.set

        return Args(project_dir=args.project_dir, action=action)


def main_with_args(args: Args) -> Version:
    """Execute application and return new version."""
    pyproject_path = args.project_dir / "pyproject.toml"
    package_paths = parse_package_paths(pyproject_path, args.project_dir)
    version_files = VersionFile.load_all(pyproject_path, package_paths)

    match args.action:
        case IncrementKind() as increment_kind:
            current_version = VersionFile.get_current_version(version_files)
            new_version = current_version.incremented(increment_kind)
        case new_version:
            pass

    VersionFile.dump_all(version_files, new_version)
    return new_version


def main() -> None:
    """Parse CLI arguments, execute application and print new version."""
    stdout.write(main_with_args(Args.parse_argv()).dump() + "\n")
