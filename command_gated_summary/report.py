"""Render the complete three-part release review."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTINUATION = ROOT / "data" / "review_continuation.md"

def render(fields):
    if not fields:
        raise ValueError("fields are required")
    names = {item.field for item in fields}
    if not {"purpose", "contents", "structure", "highlights", "terminal"}.issubset(names):
        raise ValueError("manifest is incomplete")
    continuation = CONTINUATION.read_text(encoding="utf-8").rstrip()
    return (
        "# Release Review Document: Parts 2 and 3\n"
        + continuation
        + "\n\npurpose=Review artifacts are collected into a deterministic command report.\n"
        + "contents=data manifest, command_gated_summary package, tests, and verification entry point.\n"
        + "structure=data/, command_gated_summary/, tests/, Makefile, and verify.sh.\n"
        + "highlights=The complete review is available only after document continuation.\n"
        + "terminal=command-execution-complete\n"
        + "decision=release-impact=high\n"
    )
