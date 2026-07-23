# Reliability

## H0 scope

H0 reliability means deterministic, reproducible validation:

- Locked dependencies via `uv.lock`
- Documented bootstrap and check commands
- CI that fails on stale lockfiles, lint, test, architecture, or secret findings

## Future product

Operational reliability targets for the Continuum product are defined in the canonical proposal and future ADRs. H0 does not deploy services.

## Rollback

H0 changes roll back by reverting the merge commit on `main`.
