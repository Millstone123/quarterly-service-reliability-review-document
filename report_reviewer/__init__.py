"""report-reviewer: deterministic report finalization and live worksheet verification."""

import sys

__version__ = "1.0.0"

if not sys.flags.no_site:
    try:
        from .worksheet import activate_runtime

        activate_runtime()
    except Exception:
        pass
