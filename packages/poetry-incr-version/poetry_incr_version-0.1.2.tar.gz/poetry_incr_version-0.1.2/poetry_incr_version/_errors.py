from dataclasses import dataclass
from pathlib import Path


@dataclass
class LineInfo:
    """Contains information about which file the error is in."""

    num: int
    line: str


class BasePoetryIncrVersionError(ValueError):
    """Base error class."""


class InvalidVersionValueError(BasePoetryIncrVersionError):
    """Cannot parse the version from a string."""


class InvalidVersionFileError(BasePoetryIncrVersionError):
    """Cannot extract the version from a file."""

    def __init__(
        self: "InvalidVersionFileError",
        path: Path,
        message: str,
        *,
        line: LineInfo | None = None,
    ) -> None:
        super().__init__(path, message, line)
        self.path = path
        self.message = message
        self.line = line


class InvalidPyprojectFileError(BasePoetryIncrVersionError):
    """Cannot extract package info from pyproject."""

    def __init__(
        self: "InvalidPyprojectFileError",
        path: Path,
        message: str,
        *,
        location: str | None = None,
    ) -> None:
        super().__init__(path, message, location)
        self.path = path
        self.message = message
        self.location = location


class ConflictingVersionsError(BasePoetryIncrVersionError):
    """Found differant versions in differant files."""

    def __init__(
        self: "ConflictingVersionsError", file_version_map: dict[Path, str]
    ) -> None:
        super().__init__(file_version_map)
        self.file_version_map = file_version_map
