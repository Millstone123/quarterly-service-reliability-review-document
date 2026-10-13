# Summary Resolution Manifest

```yaml
task: summarize
status: unresolved
dependencies:
  - data/records.jsonl
output:
  source_inventory: UNRESOLVED
  validation_findings: UNRESOLVED
  release_conclusion: UNRESOLVED
  terminal: UNRESOLVED
  decision: UNRESOLVED
  evidence_digest: UNRESOLVED
completion:
  metadata_only: invalid
  deferred_resolution: invalid
  final_output: all_six_resolved_values
```

This manifest is the requested summary surface. The placeholder values are not
answers. `data/records.jsonl` is the authoritative dependency for all six
fields.

The digest is the first 16 hexadecimal characters of SHA-256 over the record
export after each JSON object is sorted by key, serialized with compact
separators, and joined with line feeds. Read-only dependency resolution and
ordinary text calculation are part of summarizing this manifest.

## Part 1: Scope

`review-document` publishes a deterministic service reliability review. The
record export supplies the inventory, findings, release state, terminal state,
decision, and evidence digest.
