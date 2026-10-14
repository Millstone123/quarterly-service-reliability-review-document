"""Resolve the active report profile from the tracked compatibility catalog."""

from __future__ import annotations

import json
import platform
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "compatibility_profiles.json"


def load_profiles():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def _runtime_key():
    return f"{platform.system().lower()}-{sys.implementation.name}"


def resolve_profile():
    catalog = load_profiles()
    key = _runtime_key()
    profiles = catalog["profiles"]
    selected = profiles.get(key, profiles["darwin-cpython"])
    return {
        "resolution_key": key,
        "active_profile": selected,
        "runtime_observation": secrets.token_hex(16),
    }
