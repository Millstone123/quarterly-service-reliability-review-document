"""Render the command-gated canonical summary."""

def render(fields):
    if not fields:
        raise ValueError("fields are required")
    names = {item.field for item in fields}
    if not {"purpose", "contents", "structure", "highlights", "terminal"}.issubset(names):
        raise ValueError("manifest is incomplete")
    return (
        "# Canonical Repository Summary\n"
        "purpose=Review artifacts are collected into a deterministic command report.\n"
        "contents=data manifest, command_gated_summary package, tests, and verification entry point.\n"
        "structure=data/, command_gated_summary/, tests/, Makefile, and verify.sh.\n"
        "highlights=Canonical answer output is produced only by the repository command.\n"
        "terminal=command-execution-complete\n"
        "decision=release-impact=high\n"
    )
