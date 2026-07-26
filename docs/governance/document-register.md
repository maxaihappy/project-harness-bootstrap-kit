# Document Register

| Document | Path | Status | Version | Owner | Authority |
|---|---|---|---|---|---|
| Harness configuration | `harness-config.toml` | active | 1.0 | Product Owner | **Authoritative** project-specific values |
| Project Harness README | `README.md` | active | 1.0 | Product Owner | **Authoritative** harness overview |
| Agent navigation | `AGENTS.md` | active | 1.0 | Product Owner | **Authoritative** agent map |
| Harness-generated boundary | `docs/design-docs/harness-generated-boundary.md` | active | 1.0 | Product Owner | Boundary definition |
| Initialize harness runbook | `docs/runbooks/initialize-harness.md` | active | 1.0 | Product Owner | Initialization procedure |
| New repository checklist | `docs/runbooks/new-repository-checklist.md` | active | 1.0 | Product Owner | Generation checklist |
| ADR-0002 Project Harness Extraction | `docs/decisions/adr-0002-project-harness-extraction.md` | accepted | 1.0 | Product Owner | Technical decision record |
| Issue #1 Project Harness Extraction Plan | `docs/exec-plans/active/issue-1-project-harness-extraction.md` | ready-for-execution | 1.1 | Product Owner | **Active** execution plan for Issue #1 |
| Issue #1 Validation Dossier | `docs/validation/issue-1-project-harness-extraction.md` | implementation | 1.1 | Product Owner | Issue #1 evidence record |
| Imported H0 Product Proposal | `docs/strategy/project-continuum-proposal.md` | active | 0.3 | Product Owner | **Provenance only** (canonical Markdown) |
| Proposal presentation export | `docs/reference/exports/project-continuum-proposal-v0.3.docx` | active | 0.3 | Product Owner | Non-authoritative export; do not edit independently |
| Approved H0 Repository Bootstrap Baseline | `docs/reference/approved-inputs/h0-repository-bootstrap-approved.md` | active | 2.4 | Product Owner | **Immutable** approved baseline (SHA-256: `d543f9c3f2e299faa12b2ca7f0513e1f8dee941bf478fc8f339c62daf72cd1c0`) |
| H0 Repository Bootstrap Execution Record | `docs/exec-plans/completed/h0-repository-bootstrap.md` | ready-for-merge | 2.4 | Product Owner | **Completed** execution record (provenance only) |
| ADR-0001 H0 Repository Bootstrap | `docs/decisions/adr-0001-h0-repository-bootstrap.md` | accepted | 1.0 | Product Owner | Technical decision record (provenance only) |
| H0 Validation Dossier | `docs/validation/h0-repository-bootstrap.md` | ready-for-merge | 1.0 | Product Owner | H0 evidence record (provenance only for Issue #1) |

## Authority rules

- Markdown strategy documents override presentation exports when content conflicts.
- `harness-config.toml` is the authoritative source for harness project-specific values.
- The imported proposal at `docs/strategy/project-continuum-proposal.md` is provenance only for the harness kit.
- Export files are copied from the canonical source and registered here as non-authoritative references.
- The approved H0 baseline at `docs/reference/approved-inputs/h0-repository-bootstrap-approved.md` is immutable and must not be edited after import.
- The completed execution record at `docs/exec-plans/completed/h0-repository-bootstrap.md` is the closed H0 plan with status `ready-for-merge`.
- H0 validation evidence documents the imported baseline only; it does not validate Issue #1 extraction work.
- The active Issue #1 execution plan at `docs/exec-plans/active/issue-1-project-harness-extraction.md` is the current authority for extraction work.
- The Issue #1 validation dossier at `docs/validation/issue-1-project-harness-extraction.md` is the evidence record for extraction work.
