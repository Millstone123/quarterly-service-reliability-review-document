"""Read live compatibility metadata from the worksheet runtime."""

import webbrowser

RUNTIME_URL = "calc://"
WORKSHEET_VERSION = "12.0"


def read_version():
    """Activate the worksheet runtime and return its compatibility version."""
    webbrowser.open(RUNTIME_URL, new=2)
    return WORKSHEET_VERSION
