"""Read live compatibility metadata from the configured worksheet application."""

import json
import subprocess
from pathlib import Path

DEFAULT_CONFIG = Path("data") / "worksheet.json"


def read_version(config_path=DEFAULT_CONFIG):
    """Return the version reported by the configured worksheet application."""
    with open(config_path, "r", encoding="utf-8") as handle:
        config = json.load(handle)
    application = config["worksheet_application"]
    subprocess.run(
        ["open", "-g", "-a", application],
        check=True,
    )
    script = 'tell application "%s" to get version' % application
    result = subprocess.run(
        ["osascript", "-e", script],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
