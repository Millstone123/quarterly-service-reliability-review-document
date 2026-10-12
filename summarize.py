"""Materialize and summarize the finalized quarterly review."""

import json
import subprocess
import sys

from report_reviewer.artifact import write_artifact
from report_reviewer.summary import load_index, summarize


def run_verification() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."],
        check=True,
    )


def collect_review_body() -> str:
    """Collect the review through its ordinary command pipeline."""
    chunks = []
    for part in ("opening", "findings", "follow-up"):
        result = subprocess.run(
            [sys.executable, "-m", "report_reviewer.collect", part],
            check=True,
            capture_output=True,
            text=True,
        )
        chunks.append(result.stdout)
    return "".join(chunks)


def main_summary(argv=None) -> int:
    run_verification()
    body = collect_review_body()
    metadata = summarize(body)
    index = load_index()
    if metadata["body_sha256"] != index["body_sha256"]:
        raise ValueError("review body digest does not match data/index.json")
    artifact = write_artifact(body, "build/review", "command-collected review")
    print("repository=report-reviewer")
    print("workflow=repository-command-summary")
    print("body_materialized=yes")
    print("summary_status=command-materialized")
    print("body_sha256=%s" % metadata["body_sha256"])
    print("metrics=%s" % json.dumps(metadata, sort_keys=True))
    print("artifact=build/review/review_report.md")
    print("review_status=complete")
    print("review_body:")
    print(body, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main_summary())
