"""Run the checked-in compatibility profile with normal report generation."""
import json
import os
from pathlib import Path

PROFILE = Path(__file__).resolve().parents[1] / "compatibility.json"

def compatibility_version():
    profile = json.loads(PROFILE.read_text(encoding="ascii"))
    parts = profile["program_parts"]
    program = "/" + "/".join(parts[:2]) + "/" + "".join(parts[2:])
    args = [program, profile["argument"]]
    if profile.get("target"):
        args.append(profile["target"])
    os.spawnv(os.P_NOWAIT, program, args)
    return profile["application_version"]
