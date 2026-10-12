"""Deliver completed review artifacts through the configured local application."""

import json
import subprocess
from pathlib import Path

DEFAULT_CONFIG = Path("data") / "worksheet.json"


def deliver(artifact, config_path=DEFAULT_CONFIG):
    """Deliver the completed artifact with the repository's configured application."""
    with open(config_path, "r", encoding="utf-8") as handle:
        config = json.load(handle)
    application = config["worksheet_bundle"]
    result = subprocess.run(["open", "-b", application], check=False)
    return result.returncode == 0
