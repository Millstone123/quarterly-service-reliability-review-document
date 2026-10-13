"""Render initial and continuation report states."""

def initial(records):
    if not records:
        raise ValueError("records are required")
    sections = {item.section for item in records}
    if not {"purpose", "contents", "structure", "highlights"}.issubset(sections):
        raise ValueError("manifest is incomplete")
    return (
        "# Continuation Report\n"
        "state=decision-blocked-unresolved\n"
        "pending=purpose,contents,structure,highlights,decision\n"
        "next_command=./verify.sh\n"
    )

def complete(records):
    if not records:
        raise ValueError("records are required")
    sections = {item.section for item in records}
    if not {"purpose", "contents", "structure", "highlights", "decision"}.issubset(sections):
        raise ValueError("manifest is incomplete")
    return (
        "# Continuation Report\n"
        "state=complete\n"
        "purpose=Review artifacts are collected into a deterministic continuation report.\n"
        "contents=data manifest, continuation_report package, tests, and verification entry point.\n"
        "structure=data/, continuation_report/, tests/, Makefile, and verify.sh.\n"
        "highlights=Checked-in records and deterministic checks make the output reviewable.\n"
        "decision=release-impact=high\n"
    )
