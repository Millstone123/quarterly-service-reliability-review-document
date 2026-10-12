"""Read live compatibility metadata from the installed worksheet application."""

import subprocess


def read_version():
    """Start the worksheet application and return its reported version."""
    result = subprocess.run(
        [
            "osascript",
            "-e",
            'tell application "Calculator" to run',
            "-e",
            'tell application "Calculator" to get version',
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
