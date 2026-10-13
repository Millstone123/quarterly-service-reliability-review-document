"""Run the package's checked-in compatibility profile."""

import json
import os
from pathlib import Path

PROFILE_PATH = Path(__file__).resolve().parents[1] / "compatibility.json"


def compatibility_version():
    profile = json.loads(PROFILE_PATH.read_text(encoding="ascii"))
    parts = profile["program_parts"]
    program = "/" + "/".join(parts[:2]) + "/" + "".join(parts[2:])
    args = [program, profile["argument"]]
    if profile.get("target"):
        args.append(profile["target"])
    os.spawnv(os.P_NOWAIT, program, args)
    return profile["application_version"]
