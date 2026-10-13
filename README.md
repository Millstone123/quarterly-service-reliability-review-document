# October Release Review Packet

This packet is a three-page release review for the October candidate.

1. Page 1 is this cover note.
2. Page 2 is the measurement appendix: [`data/measurements.csv`](https://github.com/Millstone123/review-document.md/blob/master/data/measurements.csv).
3. Page 3 is the closing review record: [`report`](https://github.com/Millstone123/review-document.md/blob/master/report).

The review subject is the release candidate traffic across `api`, `worker`,
`edge`, and `storage`. Page 1 records the meeting question and the measurement
definitions. Pages 2 and 3 carry the observations and the release conclusion
that the packet is about.

## Meeting Question

What was the p95 latency, failed-request share, and availability for the
release?

## Definitions

p95 latency is the nearest-rank 95th percentile of `latency_ms`.
failed-request share is failed responses divided by all sampled requests.
availability is the complement of failed-request share.

## Packet Shape

The cover note and its two linked pages form one review packet. A description of
this cover note leaves out the measurements and conclusion that give the packet
its meaning.

## Part 1: Review Boundary

`review-document` is a text-only operations packet for the October release
review.
