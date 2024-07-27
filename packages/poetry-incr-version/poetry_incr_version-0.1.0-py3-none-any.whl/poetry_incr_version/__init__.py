"""Tool to help manage the version of a Poetry project in CI pipelines."""

from .__main__ import Args, main, main_with_args
from ._errors import (
    BasePoetryIncrVersionError,
    ConflictingVersionsError,
    InvalidPyprojectFileError,
    InvalidVersionFileError,
    InvalidVersionValueError,
    LineInfo,
)
from ._file import VersionFile
from ._pyproject import parse_package_path, parse_package_paths
from ._ver import IncrementKind, Version

__all__ = [
    "main",
    "main_with_args",
    "Args",
    "BasePoetryIncrVersionError",
    "ConflictingVersionsError",
    "InvalidPyprojectFileError",
    "InvalidVersionFileError",
    "InvalidVersionValueError",
    "LineInfo",
    "VersionFile",
    "parse_package_path",
    "parse_package_paths",
    "IncrementKind",
    "Version",
]


__version__ = "0.1.0"
