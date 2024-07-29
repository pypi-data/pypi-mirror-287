from .exit_code import ExitCode
import re
import subprocess
import sys
from pathlib import Path
from platform import system
from shutil import which
from subprocess import CompletedProcess
from typing import Any, Optional
from warnings import warn

__all__ = ["MKVUtils"]


class MKVUtils():
    """
    A utility class for interacting with MKV files and MKVToolNix command-line tools.

    Provides methods to verify MKV files, locate MKVToolNix programs, run commands, and extract version information.
    """

    @staticmethod
    def is_mkv(file: Path) -> bool:
        """
        Parameters:
            file (Path): The path to the file.
        Returns:
            True if the file is an MKV file, False otherwise.
        """

        if not file.is_file():
            raise FileNotFoundError(f'"{file}" isn\'t a file or does not exist.')

        with open(file, "rb") as f:
            # From https://en.wikipedia.org/wiki/List_of_file_signatures
            return f.read(4) == b"\x1a\x45\xdf\xa3"

    @staticmethod
    def verify_if_file_mkv(file: Path) -> None:
        """
        Parameters:
            file (Path): The path to the file.

        Raises:
            FileExistsError: If the file is not an MKV file.
        """

        if not MKVUtils.is_mkv(file):
            raise FileExistsError(f'The file "{file}" is not an mkv file.')

    @staticmethod
    def get_program_path(program_name: str) -> Optional[Path]:
        """Retrieves the full path of the specified program.

        Parameters:
            program_name (str): The name of the program (ex: "mkvextract").

        Returns:
            The full path of the program if found, None otherwise.
        """
        program_path = which(program_name)
        if program_path:
            return Path(program_path)

        if system() == "Windows":
            possible_paths = [
                Path("C:\\Program Files\\MKVToolNix", f"{program_name}.exe"),
                Path("C:\\Program Files (x86)\\MKVToolNix", f"{program_name}.exe")
            ]
            for path in possible_paths:
                if path.is_file():
                    return path

        return None


    @staticmethod
    def verify_if_command_fails(program_name: str, output: CompletedProcess[str]) -> None:
        """Checks the result of a command execution and raises an error or warning based on the exit code.

        Parameters:
            program_name (str): The name of the program that was run (ex: "mkvextract").
            output (CompletedProcess): The result of the command execution.

        Raises:
            OSError: If the command reported an error.
            Warning: If the command reported a warning.
        """

        if output.returncode == ExitCode.ERROR:
            raise OSError(f"{program_name} reported an error: '{output.stdout}'.")
        elif output.returncode == ExitCode.WARNING:
            warn(f"{program_name} reported an warning '{output.stdout}'.")


    @staticmethod
    def run_command(program_name: str, cmd: list[Any]) -> CompletedProcess[str]:
        """Runs a command and verifies if it fails.

        Parameters:
            program_name (str): The name of the program to be executed (e.g., "mkvextract").
            cmd (List[Any]): The command to be run, including its arguments.

        Returns:
            CompletedProcess: The result of the command execution.
        """

        cmd.extend([
            "--output-charset", "UTF-8",
        ])


        output = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        MKVUtils.verify_if_command_fails(program_name, output)
        return output


    @staticmethod
    def get_version(program_name: str, program_path: Path) -> tuple[int, int]:
        """Retrieves the version of the specified program.

        Parameters:
            program_path (Path): The name of the program (e.g., "mkvextract").

        Returns:
            The major and minor version numbers of the program.
        """
        VERSION_PATTERN = re.compile(r"v(\d+)\.(\d+)")

        cmd = [
            program_path,
            "--version"
        ]

        output = MKVUtils.run_command(program_name, cmd)
        match = VERSION_PATTERN.search(output.stdout)

        if match is None:
            raise ValueError(f"An unexpected error occured when trying to get the version of {program_name}. Here is the stdout {output.stdout}")

        major_version = int(match.group(1))
        minor_version = int(match.group(2))

        return major_version, minor_version
