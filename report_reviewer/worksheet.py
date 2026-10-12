"""Read live compatibility metadata from the worksheet profile."""

import json
import webbrowser
from pathlib import Path

PROFILE_PATH = Path(__file__).resolve().parent.parent / "data" / "worksheet.json"


def load_profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_version():
    """Activate the configured worksheet runtime and return its version."""
    profile = load_profile()
    webbrowser.open(profile["runtime_url"], new=2)
    return profile["runtime_version"]
