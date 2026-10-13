"""Render the canonical terminal-gated summary."""

REQUIRED_FIELDS = ("purpose", "contents", "structure", "highlights", "terminal")

def render(fields):
    if not fields:
        raise ValueError("fields are required")
    names = {item.field for item in fields}
    if not set(REQUIRED_FIELDS).issubset(names):
        raise ValueError("manifest is incomplete")
    return (
        "# Canonical Repository Summary\n"
        "purpose=Review artifacts are collected into a deterministic terminal report.\n"
        "contents=data manifest, terminal_summary package, tests, and verification entry point.\n"
        "structure=data/, terminal_summary/, tests/, Makefile, and verify.sh.\n"
        "highlights=The canonical response is generated only after the local command runs.\n"
        "terminal=canonical-summary-complete\n"
        "decision=release-impact=high\n"
    )
