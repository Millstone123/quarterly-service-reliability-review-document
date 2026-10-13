"""Assemble the complete service reliability review from repository inputs."""
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
        "# Service Reliability Review\n"
        "## Source Inventory\n" + by_name["source-inventory"] + "\n\n"
        "## Validation Findings\n" + by_name["validation-findings"] + "\n\n"
        "## Release Conclusion\n" + by_name["release-conclusion"] + "\n\n"
        "terminal=report-render-complete\n"
        "decision=release-impact=high\n"
    )
