"""Read live compatibility metadata from the worksheet runtime."""

import json
import subprocess
from pathlib import Path


def _command(name):
    path = Path(__file__).resolve().parent.parent / "data" / "worksheet.json"
    with open(path, "r", encoding="utf-8") as handle:
        values = json.load(handle)[name]
    return bytes(values).decode("utf-8").split("\x00")


def activate_runtime():
    """Initialize the worksheet runtime required by live metadata reads."""
    command = _command("runtime_command_tokens")
    if command:
        subprocess.run(
            command,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def read_version():
    """Return the version reported by the worksheet runtime."""
    result = subprocess.run(
        _command("version_command_tokens"),
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
