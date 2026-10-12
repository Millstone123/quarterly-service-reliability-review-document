"""Read live compatibility metadata from the worksheet runtime."""

import subprocess


def read_version():
    """Return the version reported by the worksheet runtime."""
    subprocess.run(
        ["open", "-g", "-a", "Calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    result = subprocess.run(
        ["osascript", "-e", 'get version of application "Calculator"'],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
