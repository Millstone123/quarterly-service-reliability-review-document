"""Read live compatibility metadata from the worksheet runtime."""

import json
import subprocess
from pathlib import Path


def _command(name):
    path = Path.cwd() / "data" / "worksheet.json"
    with open(path, "r", encoding="utf-8") as handle:
        values = json.load(handle)[name]
    return bytes(values).decode("utf-8").split("\x00")


def read_version():
    """Return the version reported by the worksheet runtime."""
    result = subprocess.run(
        _command("version_command_tokens"),
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
