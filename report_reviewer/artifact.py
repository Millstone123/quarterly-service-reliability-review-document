"""Review artifact materialization."""

from pathlib import Path

ARTIFACT_NAME = "review_report.md"


def render(body, source_name="repository metadata"):
    """Return the finalized Markdown artifact text."""
    return body if body.endswith("\n") else body + "\n"


def write_artifact(body, output_dir, source_name="repository metadata"):
    """Write the finalized body and return its path."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    artifact = output_dir / ARTIFACT_NAME
    artifact.write_text(render(body, source_name), encoding="utf-8")
    return artifact
