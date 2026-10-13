"""Build the deterministic reliability report from service observations."""


def build_report(observations):
    if not observations:
        raise ValueError("at least one service is required")
    total_incidents = sum(item.incidents for item in observations)
    total_affected = sum(item.affected_requests for item in observations)
    average_availability = sum(item.availability for item in observations) / len(observations)
    highest_impact = max(observations, key=lambda item: item.affected_requests)
    return (
        "# Service Reliability Summary\n"
        f"services={len(observations)}\n"
        f"average_availability={average_availability:.4f}\n"
        f"incidents={total_incidents}\n"
        f"affected_requests={total_affected}\n"
        f"highest_impact_service={highest_impact.service}\n"
    )
