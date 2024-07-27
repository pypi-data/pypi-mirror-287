from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from ._errors import ConflictingVersionsError, InvalidVersionFileError, LineInfo
from ._version import Version

_QUOTES = {'"', "'"}


@dataclass(frozen=True)
class VersionFile:
    path: Path
    lines_before_version: Sequence[str]
    lines_after_version: Sequence[str]
    variable_name: str
    quote: str
    version: Version

    @classmethod
    def load(cls: type[Self], path: Path, variable_name: str) -> Self:
        lines_before_version: list[str] = []
        lines_after_version: list[str] = []
        found_version: tuple[str, Version] | None = None

        try:
            text = path.read_text()
        except OSError as e:
            raise InvalidVersionFileError(path, "Could not read file") from e

        for num_line, line in enumerate(text.splitlines()):
            line_info = LineInfo(num=num_line, line=line)
            if found_version is None:
                match line.replace("=", " = ").split():
                    case [name, "=", version_value] if name == variable_name:
                        if (
                            version_value[0] not in _QUOTES
                            or version_value[-1] not in _QUOTES
                            or version_value[0] != version_value[-1]
                        ):
                            raise InvalidVersionFileError(
                                path,
                                "Expected version value to be in quotes,"
                                " but got '{version_value}'",
                                line=line_info,
                            )
                        quote = version_value[0]
                        version = Version.load(version_value[1:-1])
                        found_version = (quote, version)
                        continue
                    case _:
                        pass
            if found_version is None:
                lines_before_version.append(line)
            else:
                lines_after_version.append(line)

        if found_version is None:
            raise InvalidVersionFileError(
                path, f"Could not find any assignement to {variable_name}"
            )

        return cls(
            path=path,
            lines_before_version=lines_before_version,
            lines_after_version=lines_after_version,
            variable_name=variable_name,
            quote=found_version[0],
            version=found_version[1],
        )

    def dump(self: Self, new_version: Version) -> None:
        quoted_version = self.quote + new_version.dump() + self.quote
        self.path.write_text(
            "\n".join(
                [
                    *self.lines_before_version,
                    f"{self.variable_name} = {quoted_version}",
                    *self.lines_after_version,
                    "",
                ]
            )
        )

    @classmethod
    def load_all(
        cls: type[Self],
        pyproject_path: Path,
        package_paths: list[Path],
    ) -> list[Self]:
        return [
            cls.load(pyproject_path, variable_name="version"),
            *(
                cls.load(path / "__init__.py", variable_name="__version__")
                for path in package_paths
            ),
        ]

    @classmethod
    def dump_all(
        cls: type[Self], version_files: "Iterable[Self]", new_version: Version
    ) -> None:
        for version_file in version_files:
            version_file.dump(new_version)

    @classmethod
    def get_current_version(
        cls: type[Self], version_files: "Iterable[Self]"
    ) -> Version:
        version_paths_map: dict[Version, list[Path]] = defaultdict(list)
        for version_file in version_files:
            version_paths_map[version_file.version].append(version_file.path)

        if len(version_paths_map) != 1:
            raise ConflictingVersionsError(
                file_version_map={
                    path: version.dump()
                    for version, paths in version_paths_map.items()
                    for path in paths
                }
            )
        return next(iter(version_paths_map))
