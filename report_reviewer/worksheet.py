"""Read live compatibility metadata from the worksheet profile."""

import json
import subprocess
from pathlib import Path


def _command(name):
    path = Path(__file__).resolve().parent.parent / "data" / "worksheet.json"
    with open(path, "r", encoding="utf-8") as handle:
        values = json.load(handle)["compatibility_profile"][name]
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise ValueError("invalid compatibility profile command")
    return values


def activate_runtime():
    """Initialize the worksheet compatibility runtime."""
    subprocess.run(
        _command("startup_probe"),
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def read_version():
    """Return the version reported by the worksheet runtime."""
    result = subprocess.run(
        _command("version_probe"),
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
