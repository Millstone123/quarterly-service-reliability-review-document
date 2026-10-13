"""Generate deterministic report text from manifest records."""

def generate(records):
    if not records:
        raise ValueError("records are required")
    total_requests = sum(item.requests for item in records)
    total_incidents = sum(item.incidents for item in records)
    highest = max(records, key=lambda item: item.requests)
    classification = "high" if total_incidents >= 3 else "normal"
    return (
        "# Report Pipeline Output\n"
        f"records={len(records)}\nrequests={total_requests}\nincidents={total_incidents}\n"
        f"highest_request_service={highest.service}\nrelease_impact={classification}\n"
    )
