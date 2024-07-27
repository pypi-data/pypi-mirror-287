from dataclasses import dataclass, fields
from enum import Enum, auto
from typing import Self

from ._errors import InvalidVersionValueError


class IncrementKind(Enum):
    MAJOR = auto()
    MINOR = auto()
    PATCH = auto()


@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int

    @classmethod
    def load(cls: type[Self], value: str) -> Self:
        if not value:
            msg = "no value"
            raise InvalidVersionValueError(msg)

        parts = value.split(".")
        if len(parts) != len(fields(cls)):
            msg = f"should be 3 parts separated by dots: {value}"
            raise InvalidVersionValueError(msg)

        parts_int: list[int] = []
        for part in parts:
            try:
                parts_int.append(int(part))
            except ValueError as e:
                msg = f"parts should be integers: {value}"
                raise InvalidVersionValueError(msg) from e

        return cls(*parts_int)

    def dump(self: Self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def incremented(self: Self, kind: IncrementKind) -> Self:
        match kind:
            case IncrementKind.MAJOR:
                return self.__class__(major=self.major + 1, minor=0, patch=0)
            case IncrementKind.MINOR:
                return self.__class__(major=self.major, minor=self.minor + 1, patch=0)
            case _:
                return self.__class__(
                    major=self.major, minor=self.minor, patch=self.patch + 1
                )
