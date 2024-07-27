from contextlib import suppress
from pathlib import Path
from tomllib import TOMLDecodeError
from tomllib import loads as toml_loads

from ._errors import InvalidPyprojectFileError
from .util import is_dict, is_list


def parse_package_path(
    pyproject_package: object,
    location: str,
    project_dir: Path,
    pyproject_path: Path,
) -> Path:
    if not is_dict(pyproject_package):
        raise InvalidPyprojectFileError(
            pyproject_path, "is not a dict:", location=location
        )
    try:
        include = pyproject_package["include"]
    except KeyError as e:
        raise InvalidPyprojectFileError(
            pyproject_path, "missing include property", location=location
        ) from e
    if not isinstance(include, str):
        raise InvalidPyprojectFileError(
            pyproject_path,
            "include property is not a string"
            f", given: {include} of type {type(include)}",
            location=location,
        )
    from_ = None
    with suppress(KeyError):
        from_ = pyproject_package["from"]

    if from_ is not None:
        if not isinstance(from_, str):
            raise InvalidPyprojectFileError(
                pyproject_path,
                "from property is not a string"
                f", given: {from_} of type {type(from_)}",
                location=location,
            )
        return project_dir / Path(from_) / include
    return project_dir / include


def parse_package_paths(pyproject_path: Path, project_dir: Path) -> list[Path]:
    try:
        text = pyproject_path.read_text()
    except OSError as e:
        raise InvalidPyprojectFileError(pyproject_path, "could not read file") from e

    try:
        content = toml_loads(text)
    except TOMLDecodeError as e:
        raise InvalidPyprojectFileError(pyproject_path, "could not decode toml") from e

    location = ""
    path: list[str | int] = []

    for name in ["tool", "poetry", "packages"]:
        if not is_dict(content):
            raise InvalidPyprojectFileError(
                pyproject_path, "is not a dict", location=location
            )
        content = content.get(name)
        path.append(name)
        location = ".".join(map(str, path))

    if not is_list(content):
        raise InvalidPyprojectFileError(
            pyproject_path, "is not a list", location=location
        )

    return [
        parse_package_path(
            pyproject_package,
            location=location + f".{index}",
            project_dir=project_dir,
            pyproject_path=pyproject_path,
        )
        for index, pyproject_package in enumerate(content)
    ]
