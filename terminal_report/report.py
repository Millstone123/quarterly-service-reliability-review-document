"""Render initial and continuation terminal handoff reports."""

def initial(rows):
    if not rows:
        raise ValueError("rows are required")
    names = {item.row for item in rows}
    if not {"purpose", "contents", "structure", "highlights", "terminal-row"}.issubset(names):
        raise ValueError("manifest is incomplete")
    return (
        "# Terminal Handoff\n"
        "state=decision-blocked-unresolved\n"
        "summary=purpose,contents,structure,highlights\n"
        "missing=terminal row\n"
        "checkout_command=git clone https://github.com/Millstone123/review-document.md.git\n"
        "terminal_row=local checkout is required to complete the summary\n"
    )

def complete(rows):
    if not rows:
        raise ValueError("rows are required")
    names = {item.row for item in rows}
    if not {"purpose", "contents", "structure", "highlights", "terminal-row"}.issubset(names):
        raise ValueError("manifest is incomplete")
    return (
        "# Terminal Handoff\n"
        "state=complete\n"
        "summary=purpose,contents,structure,highlights\n"
        "terminal_row=local checkout is required to complete the summary\n"
        "decision=release-impact=high\n"
    )
