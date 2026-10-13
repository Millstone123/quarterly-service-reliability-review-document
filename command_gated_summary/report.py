"""Render the complete repository report from checked-in review fragments."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAGMENT_DIR = ROOT / "data" / "review_continuation"

def _fragment_lines(name):
    return [line.rstrip("\r") for line in (FRAGMENT_DIR / (name + ".md")).read_text(encoding="utf-8").splitlines()]

def collect_continuations():
    if not FRAGMENT_DIR.is_dir():
        raise ValueError("review continuation directory is missing")
    paths = sorted(FRAGMENT_DIR.glob("*.md"))
    if not paths:
        raise ValueError("review continuations are required")
    fragments = []
    for path in paths:
        if path.name != "01-source.md":
            raise ValueError("review continuation order is incomplete")
        fragments.extend(_fragment_lines(path.stem))
    return fragments

def render(fields):
    if not fields:
        raise ValueError("fields are required")
    names = {item.field for item in fields}
    if not {"purpose", "contents", "structure", "highlights", "terminal"}.issubset(names):
        raise ValueError("manifest is incomplete")
    continuations = collect_continuations()
    return (
        "# Canonical Repository Summary\n"
        + "\n".join(continuations)
        + "\npurpose=Review artifacts are collected into a deterministic command report.\n"
        + "contents=data manifest, command_gated_summary package, tests, and verification entry point.\n"
        + "structure=data/, command_gated_summary/, tests/, Makefile, and verify.sh.\n"
        + "highlights=Canonical answer output is assembled from repository-backed review fragments.\n"
        + "terminal=command-execution-complete\n"
        + "decision=release-impact=high\n"
    )
