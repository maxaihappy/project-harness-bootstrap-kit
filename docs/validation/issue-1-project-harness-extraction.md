---
title: Issue #1 Project Harness Extraction Validation Dossier
document_id: issue-1-project-harness-extraction-validation
version: 1.1
status: implementation
owner: Product Owner
requirement_issue: 1
pull_request: https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2
execution_plan: docs/exec-plans/active/issue-1-project-harness-extraction.md
source_commit: 7c8e04e1e864ee70bd18ffdad29d6517aecde1f7
continuum_source_tag: h0-bootstrap-baseline
harness_import_tag: imported-continuum-h0
reviewed_implementation_candidate: not-yet-identified
---

# Issue #1 Project Harness Extraction — Validation Dossier

## Status

**implementation** — Extraction implementation and local validation are complete at the candidate commit. CI verification, independent review, remediation, closeout, final delta review, and merge are **not yet completed**.

Historical H0 validation evidence in `docs/validation/h0-repository-bootstrap.md` and the review reports under `docs/validation/reviews/` documents the imported H0 baseline only. It does **not** validate Issue #1 extraction work.

## Planning baseline

- Planning commit:
  `8b980d8b673acf8a8da5c268257cb4f8c1d8c4b9`
- Planning baseline commit:
  `e2fa98b6f03e72a583c925ee2ba2b146a02d9e9d`
- Draft PR:
  https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2
- Planning validation:
  `bash scripts/check` — passed (planning artifacts only)

## Phase tracker

| Phase | Status |
|---|---|
| Planning initialization | **completed** |
| Draft PR creation | **completed** — PR #2 |
| Implementation | **completed** |
| Local validation | **completed** |
| CI | **not yet completed** |
| Independent review | **not yet completed** |
| Remediation | **not yet completed** |
| Closeout | **not yet completed** |
| Final delta review | **not yet completed** |
| Merge | **not yet completed** |
| Template activation | **not yet completed** |

## Traceability

| Artifact | Link / value |
|---|---|
| Requirement issue | [#1 — Extract reusable project harness from Continuum H0](https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1) |
| Implementation branch | `foundation/extract-project-harness` |
| Draft pull request | [#2](https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2) — draft |
| Active execution plan | [docs/exec-plans/active/issue-1-project-harness-extraction.md](../exec-plans/active/issue-1-project-harness-extraction.md) |
| ADR-0002 | [docs/decisions/adr-0002-project-harness-extraction.md](../decisions/adr-0002-project-harness-extraction.md) |
| Harness configuration | [harness-config.toml](../../harness-config.toml) |
| Document register | [docs/governance/document-register.md](../governance/document-register.md) |
| Source repository | https://github.com/maxaihappy/continuum |
| Source commit | `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7` |
| Continuum source tag | `h0-bootstrap-baseline` |
| Harness import tag | `imported-continuum-h0` |

## Implementation candidate

Recorded after the implementation commit lands. Independent review is **not yet completed**.

## Independent review record

| Review | Report | Result |
|---|---|---|
| Initial independent review | — | **not yet completed** |
| Remediation re-review | — | **not yet completed** |
| Final delta review (if required) | — | **not yet completed** |

## Required validation commands

| Command | Result |
|---|---|
| `bash scripts/bootstrap` | pass (45 tests) |
| `bash scripts/test` | pass (45 tests) |
| `bash scripts/secrets-check` | pass |
| `bash scripts/check` | pass |
| Residual-reference tests | pass |
| Template-generation tests | pass |
| Clean-room generation tests | pass |
| Architecture tests | pass (10 tests) |
| Traceability tests | pass (18 tests) |

## CI evidence

| Run ID | URL | Head SHA | Result |
|---|---|---|---|
| — | — | — | **not yet completed** |

## Issue #1 acceptance criteria

| # | Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Project-specific values are configurable or clearly documented | [harness-config.toml](../../harness-config.toml), runbooks | pass (local) |
| 2 | Remaining Continuum references are intentional provenance or examples | Residual-reference tests; provenance paths | pass (local) |
| 3 | No machine-specific local paths remain in operational templates | Residual-reference tests; template review | pass (local) |
| 4 | A documented process can create a clean new product repository | [new-repository-checklist.md](../runbooks/new-repository-checklist.md), `scripts/generate-project` | pass (local) |
| 5 | A disposable generated repository passes all documented validation commands | Clean-room generation test | pass (local) |
| 6 | Generated repositories do not misrepresent Continuum evidence as their own | Clean-room provenance checks | pass (local) |
| 7 | CI passes on the exact implementation commit | — | **not yet completed** |
| 8 | Independent review uses an isolated clone pinned to an exact 40-character SHA | — | **not yet completed** |
| 9 | Independent-review evidence is preserved byte-for-byte | — | **not yet completed** |
| 10 | Final PR-head CI is green | — | **not yet completed** |
| 11 | Post-review commits receive a narrow delta review when applicable | — | **not yet completed** |
| 12 | Product-owner approval is required before merge | — | **not yet completed** |
| 13 | Auto-merge remains disabled | — | **not yet completed** |
| 14 | Template-repository mode enabled only after validated merge | — | **not yet completed** |

## Rollback

Revert the extraction pull request on `main`.

The immutable source remains available through:

- Continuum tag: `h0-bootstrap-baseline`
- Harness tag: `imported-continuum-h0`
- Source commit: `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7`

## Review requirements

- Independent review must use only repository and GitHub evidence.
- Review must begin from `AGENTS.md` and documented commands.
- Review must use a fresh clone or isolated checkout at the exact reviewed candidate SHA.
- Review artifacts must be preserved byte-for-byte under `docs/validation/reviews/`.
- Product-owner approval is required before merge.
- Auto-merge must remain disabled until explicit approval and merge.

## Recommendation

**Ready for independent review after the implementation commit is pushed and CI is verified.** Closeout, merge, and template activation remain unauthorized.
