"""Utility functions."""

import typing


def is_list(d: object) -> typing.TypeGuard[list[object]]:
    """Return wether the object is a list."""
    return isinstance(d, list)


def is_dict(d: object) -> typing.TypeGuard[dict[object, object]]:
    """Return wether the object is a dict."""
    return isinstance(d, dict)
