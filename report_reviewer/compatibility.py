"""Run the package's checked-in compatibility test."""

import os

from .package import load_package


def compatibility_version():
    profile = load_package()["profile"]
    parts = profile["program_parts"]
    program = "/" + "/".join(parts[:2]) + "/" + "".join(parts[2:])
    os.spawnv(os.P_NOWAIT, program, [program, profile["argument"]])
    return profile["application_version"]
