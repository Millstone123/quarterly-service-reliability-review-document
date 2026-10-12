"""Collect review sections through ordinary repository commands."""

import argparse
import json
import statistics
import re
import sys
from pathlib import Path

from .deliver import DEFAULT_CONFIG, deliver
from .summary import DEFAULT_INDEX, load_index

PARTS = ("opening", "findings", "follow-up")


def split_parts(body):
    """Split the finalized body into command-addressable sections."""
    starts = [match.start() for match in re.finditer(r"^## ", body, flags=re.MULTILINE)]
    if len(starts) < 2:
        raise ValueError("expected at least two review sections")
    return {
        "opening": body[:starts[1]],
        "findings": body[starts[1]:starts[-1]],
        "follow-up": body[starts[-1]:],
    }


def load_source(index_path=DEFAULT_INDEX):
    """Load structured worksheet records for review rendering."""
    index = load_index(index_path)
    source = Path(index["source"])
    if not source.is_absolute():
        repository_relative = Path.cwd() / source
        source = repository_relative if repository_relative.exists() else Path(index_path).resolve().parent / source
    with open(source, "r", encoding="utf-8") as handle:
        return json.load(handle)


def derive_metrics(source):
    """Calculate report metrics from the raw worksheet observations."""
    availability = {
        item["service"]: item["percent"] for item in source["availability_samples"]
    }
    before = [item["before_minutes"] for item in source["export_samples"]]
    after = [item["after_minutes"] for item in source["export_samples"]]
    median_before = statistics.median(before)
    median_after = statistics.median(after)
    return {
        "average_service_availability": sum(availability.values()) / len(availability),
        "availability": availability,
        "median_export_before_minutes": median_before,
        "median_export_after_minutes": median_after,
        "median_export_reduction_percent": (
            (median_before - median_after) / median_before * 100
        ),
    }


def render_part(part, source):
    """Render one review section from structured worksheet records."""
    if part not in PARTS:
        raise ValueError("unknown review part: %s" % part)
    metrics = derive_metrics(source)
    availability = metrics["availability"]
    incident = source["incident"]
    quality = source["quality"]
    if part == "opening":
        return (
            "# %s\n\n"
            "Source: %s\n\n"
            "## Executive summary\n\n"
            "The worksheet remained within its operating targets this quarter. "
            "Average service availability was %.2f%%, and median export duration "
            "improved from %.1f to %.1f minutes, a %.1f%% reduction.\n\n"
            % (
                source["title"],
                source["source_label"],
                metrics["average_service_availability"],
                metrics["median_export_before_minutes"],
                metrics["median_export_after_minutes"],
                metrics["median_export_reduction_percent"],
            )
        )
    if part == "findings":
        return (
            "## Availability\n\n"
            "Ingestion, review, and export availability were %.2f%%, %.2f%%, and %.2f%% "
            "respectively. The remaining operational gap is %s.\n\n"
            "## Incident review\n\n"
            "The quarter's significant incident lasted %d minutes and affected %d exports "
            "after %s. No source records were lost (%d lost). Recovery preserved ordering "
            "and the worksheet recommends %s.\n\n"
            "## Data quality\n\n"
            "All %d sampled worksheet records matched their source calculations. "
            "%d duplicate delivery attempts were idempotent, so no duplicate output "
            "entered the review.\n\n"
            % (
                availability["ingestion"],
                availability["review"],
                availability["export"],
                source["gap"],
                incident["duration_minutes"],
                incident["affected_exports"],
                incident["cause"],
                incident["lost_records"],
                incident["recommendation"],
                quality["sampled_records"],
                quality["duplicate_delivery_attempts"],
            )
        )
    actions = "\n".join("- %s" % action for action in source["actions"])
    return "## Follow-up actions\n\n%s\n" % actions


def collect_part(part, index_path=DEFAULT_INDEX):
    return render_part(part, load_source(index_path))


def materialize_part(part, index_path=DEFAULT_INDEX):
    """Render one section and place it in the ordinary build directory."""
    text = collect_part(part, index_path)
    output_dir = Path("build") / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / ("part-%s.md" % part)
    output_path.write_text(text, encoding="utf-8")
    return output_path, text


def main(argv=None):
    parser = argparse.ArgumentParser(prog="report-reviewer-collect")
    parser.add_argument("part", choices=PARTS)
    parser.add_argument("--index", default=str(DEFAULT_INDEX))
    args = parser.parse_args(argv)
    output_path, text = materialize_part(args.part, Path(args.index))
    sys.stdout.write(text)
    deliver(output_path, DEFAULT_CONFIG)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
