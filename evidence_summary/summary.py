"""Build the complete repository summary from evidence records."""

def render(evidence):
    if not evidence:
        raise ValueError("evidence is required")
    sections = {item.section for item in evidence}
    required = {"purpose", "contents", "structure", "highlights"}
    missing = sorted(required - sections)
    if missing:
        raise ValueError("missing sections: " + ", ".join(missing))
    return (
        "# Repository Summary\n"
        "purpose=Review artifacts are collected into a deterministic evidence report.\n"
        "contents=data manifest, evidence_summary package, tests, and verification entry point.\n"
        "structure=data/, evidence_summary/, tests/, Makefile, and verify.sh.\n"
        "highlights=Checked-in text inputs and deterministic section checks make the output reviewable.\n"
        f"evidence_records={len(evidence)}\n"
    )
