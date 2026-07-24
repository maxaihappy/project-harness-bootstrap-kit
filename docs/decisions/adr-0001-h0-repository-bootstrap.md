---
title: ADR-0001 H0 Repository Bootstrap
status: accepted
date: 2026-07-22
deciders: Product Owner
---

# ADR-0001: H0 Repository Bootstrap

## Status

Accepted

## Context

Project Continuum requires a deterministic, auditable, and agent-portable engineering harness before substantive product implementation begins. H0 establishes repository structure, governance, validation commands, and CI without selecting the Continuum product runtime or implementing product behavior.

## Decision

1. **H0 tooling runtime:** Python 3.12 for repository tooling and tests only.
2. **Dependency manager:** `uv` with committed `uv.lock`; CI and local checks fail on stale lockfiles.
3. **Development dependencies:** `ruff`, `pytest`, `detect-secrets`, and `pre-commit` only.
4. **Command contract:** Authoritative Bash scripts in `scripts/`; Makefile delegates to scripts.
5. **Repository structure:** Monorepo with README-only product placeholders and harness tooling under `tests/` and `scripts/`.
6. **Architecture enforcement:** Data-driven `architecture-boundaries.toml` plus AST-based pytest checks with positive and negative fixtures.
7. **Secret detection:** `detect-secrets` baseline with pre-commit and CI gate; baseline changes require explicit review.
8. **CI:** GitHub Actions with least privilege, pinned action SHAs, and `scripts/check`.
9. **Merge method:** Merge commit for H0 to preserve logical branch history.

## Consequences

- Agents can bootstrap with `scripts/bootstrap` and validate with `scripts/check` without undocumented context.
- Product runtime, Telegram, providers, database, and cloud infrastructure remain explicitly deferred.
- Architecture policy changes require ADR updates before new adapter paths are approved.

## Alternatives considered

- **Makefile-only commands:** Rejected; scripts are authoritative for portability.
- **Specialized dependency-graph tools:** Deferred until H1 has a real import graph.
- **Selecting a product language in H0:** Rejected; would prematurely constrain Continuum implementation.
