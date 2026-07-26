---
title: ADR-0002 Project Harness Extraction
status: accepted
date: 2026-07-25
deciders: Product Owner
---

# ADR-0002: Project Harness Extraction from Continuum H0

## Status

Accepted

## Context

Issue #1 requires generalizing the validated Continuum H0 engineering harness into a reusable, product-neutral project harness and repository bootstrap kit. The harness must preserve validation, traceability, secret scanning, architecture enforcement, and independent-review workflows while removing unintended Continuum-specific coupling from operational artifacts.

## Decision

1. **Configuration separation:** Introduce `harness-config.toml` at the repository root for project-specific values, provenance metadata, package layout, and residual-reference policy. Generated repositories receive substituted values and exclude harness-only provenance artifacts.

2. **Generic package placeholders:** Replace Continuum-specific domain directory names with neutral placeholders (`domain_alpha` through `domain_delta`) while preserving the contracts-and-domains architecture model.

3. **Harness versus generated boundary:** The harness repository retains immutable H0 provenance under `docs/reference/`, `docs/validation/h0-*`, and `docs/exec-plans/completed/`. Generated repositories include only a minimal `docs/lineage.md` pointer and must not copy H0 validation evidence.

4. **Template generation:** Add `templates/product-repo/` and `scripts/generate-project` as the authoritative generation path. Generation uses deterministic placeholder substitution without new runtime dependencies.

5. **Residual-reference validation:** Add `harness/reference_policy.py` and pytest coverage to detect unintended Continuum references in operational files, with an allowlist for intentional provenance paths.

6. **Role-based governance:** Replace tool-specific role assignments with responsibility-based roles (product owner, planner, implementer, independent reviewer, repository authority) while documenting Cursor, Manus, and GitHub as example tooling only.

7. **CI branch coverage:** Extend push triggers to `foundation/**` so Issue #1 work receives the same validation workflow as H0 bootstrap branches.

## Consequences

- New repositories can be generated from the harness with documented initialization and checklist procedures.
- H0 provenance remains auditable without being mistaken for Issue #1 or generated-repository validation evidence.
- Traceability tests expand to cover Issue #1 artifacts without weakening immutable approved-input controls.
- Material future extraction decisions still require product-owner approval and additional ADRs.

## Alternatives considered

- **Keep Continuum package names as examples:** Rejected; names implied product-specific runtime semantics.
- **Jinja2 templating:** Rejected for H0 tooling scope; simple placeholder substitution is sufficient and avoids new dependencies.
- **Delete all Continuum provenance:** Rejected; rollback and audit requirements depend on preserved import evidence.
