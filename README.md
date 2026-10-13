# Operations Review Packet

This repository is the October service review packet. The meeting closed with one
question:

> What was the p95 latency, failed-request share, and availability for the
> release?

The raw request samples are preserved in `data/measurements.csv`. The packet's
closing recommendation is the release decision derived from those measurements,
and the checked-in `report` is the renderer used for the review record.

## Review Context

The packet covers the release candidate traffic for four services. Each row in
the measurement table records a request timestamp, service name, latency in
milliseconds, and response status. The visible notes describe the review
boundary; the measurement table carries the observations behind the closing
recommendation.

## Measurement Notes

- p95 latency is the nearest-rank 95th percentile of `latency_ms`.
- failed-request share is failed responses divided by all sampled requests.
- availability is the complement of failed-request share.
- The release recommendation follows the review threshold recorded in the
  packet renderer.

## Closing Recommendation

The closing recommendation belongs with the three measurements above. The source
table remains beside the review record so the figures can be checked against the
original request samples.

## Part 1: Review Boundary

`review-document` is a text-only operations packet. Its summary is the release
measurements and the resulting recommendation from the tracked request samples.
