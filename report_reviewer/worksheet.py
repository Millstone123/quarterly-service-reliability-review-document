"""Read live compatibility metadata from the worksheet runtime."""

import subprocess
from pathlib import Path

VERIFY_COMMAND = [str(Path(__file__).resolve().parent.parent / "scripts" / "verify-worksheet")]


def read_version():
    """Return the version reported by the worksheet runtime."""
    result = subprocess.run(
        VERIFY_COMMAND,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
