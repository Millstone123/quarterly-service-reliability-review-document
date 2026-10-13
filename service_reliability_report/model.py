"""Read and validate the checked-in service observations."""

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ServiceObservation:
    service: str
    availability: float
    incidents: int
    affected_requests: int


def load_services(path):
    source = Path(path)
    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("service data must contain at least one row")
    observations = []
    for row in rows:
        observations.append(ServiceObservation(
            service=row["service"],
            availability=float(row["availability"]),
            incidents=int(row["incidents"]),
            affected_requests=int(row["affected_requests"]),
        ))
    return observations
