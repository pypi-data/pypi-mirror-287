"""
Module for testing the project.
"""
from .cli_executor import CommandExecutor


def test_path(path: str, verbose: bool = False) -> bool:
    """
    Check the path for linting errors.
    :param path: The path to check
    """
    command = CommandExecutor(
        [
            "poetry",
            "run",
            "pytest",
            str(path),
            "-vv",
        ]
    )
    result = command.execute(verbose=verbose, stream=True)
    return result
