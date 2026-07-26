# Reliability

## Harness scope

Harness reliability means deterministic, reproducible validation:

- Locked dependencies via `uv.lock`
- Documented bootstrap and check commands
- CI that fails on stale lockfiles, lint, test, architecture, or secret findings

## Generated product repositories

Generated repositories inherit the harness validation workflow. Operational reliability targets for deployed products are defined by the product owner in generated documentation and future ADRs.

## Rollback

Harness changes roll back by reverting the merge commit on `main`.
