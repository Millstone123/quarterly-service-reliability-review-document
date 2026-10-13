"""Assemble the complete release review from distributed repository inputs."""
from .model import load_review_inputs

def render(fields):
    if not fields:
        raise ValueError("fields are required")
    names = {item.name for item in fields}
    if not {"purpose", "contents", "structure", "highlights", "terminal"}.issubset(names):
        raise ValueError("manifest is incomplete")
    inputs = load_review_inputs()
    by_name = {item.name: item.text for item in inputs}
    required = {"source-inventory", "validation-findings", "release-conclusion"}
    if not required.issubset(by_name):
        raise ValueError("review inputs are incomplete")
    return (
        "# Release Review Document: Parts 2 and 3\n"
        "## Part 2: Source Inventory and Validation\n"
        + by_name["source-inventory"]
        + "\n\n"
        + by_name["validation-findings"]
        + "\n\n## Part 3: Release Conclusion\n"
        + by_name["release-conclusion"]
        + "\n\n"
        + "terminal=command-execution-complete\n"
        + "decision=release-impact=high\n"
    )
