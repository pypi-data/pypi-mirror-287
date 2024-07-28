"""Utility functions."""

from collections.abc import Iterator
from contextlib import contextmanager, suppress
from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory
from typing import Protocol, TypeGuard


def is_list(d: object) -> TypeGuard[list[object]]:
    """Return wether the object is a list."""
    return isinstance(d, list)


def is_dict(d: object) -> TypeGuard[dict[object, object]]:
    """Return wether the object is a dict."""
    return isinstance(d, dict)


class _HasDunderFile(Protocol):
    @property
    def __file__(self) -> str: ...


def get_module_dir_path(module: _HasDunderFile) -> Path:
    """Return the path to the directory of a module."""
    return Path(module.__file__).parent
    # .parent because __file__ points to __init__.py


@contextmanager
def make_tmp_dir_copy(dir_path: Path) -> Iterator[Path]:
    """Context manager which provides a temporary deep copy of a directory."""
    with TemporaryDirectory() as tmp_dir:
        tmp_dir_copy_path = Path(tmp_dir).absolute() / dir_path.name
        copytree(dir_path, tmp_dir_copy_path)
        yield tmp_dir_copy_path


def explore_dir(dir_path: Path) -> Iterator[Path]:
    """Yield the paths of all files deeply inside a directory."""
    explored: set[Path] = set()
    to_explore = {dir_path}
    while len(to_explore) > 0:
        path = to_explore.pop()
        explored.add(path)
        yield path
        with suppress(OSError):
            to_explore.update(p for p in path.iterdir() if p not in explored)
