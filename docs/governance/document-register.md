# Document Register

| Document | Path | Status | Version | Owner | Authority |
|---|---|---|---|---|---|
| Project Continuum Product Proposal | `docs/strategy/project-continuum-proposal.md` | active | 0.3 | Product Owner | **Authoritative** (canonical Markdown) |
| Proposal presentation export | `docs/reference/exports/project-continuum-proposal-v0.3.docx` | active | 0.3 | Product Owner | Non-authoritative export; do not edit independently |
| Approved H0 Repository Bootstrap Baseline | `docs/reference/approved-inputs/h0-repository-bootstrap-approved.md` | active | 2.4 | Product Owner | **Immutable** approved baseline (SHA-256: `d543f9c3f2e299faa12b2ca7f0513e1f8dee941bf478fc8f339c62daf72cd1c0`) |
| H0 Repository Bootstrap Execution Record | `docs/exec-plans/active/h0-repository-bootstrap.md` | active | 2.4 | Product Owner | **Mutable** active execution record |
| ADR-0001 H0 Repository Bootstrap | `docs/decisions/adr-0001-h0-repository-bootstrap.md` | accepted | 1.0 | Product Owner | Technical decision record |
| H0 Validation Dossier | `docs/validation/h0-repository-bootstrap.md` | draft | 0.1 | Product Owner | Evidence record (in progress) |

## Authority rules

- Markdown strategy documents override presentation exports when content conflicts.
- The stable Markdown path for the proposal remains `docs/strategy/project-continuum-proposal.md`; version metadata and Git history preserve change history.
- Export files are copied from the canonical source and registered here as non-authoritative references.
- The approved H0 baseline at `docs/reference/approved-inputs/h0-repository-bootstrap-approved.md` is immutable and must not be edited after import.
- The active execution record at `docs/exec-plans/active/h0-repository-bootstrap.md` is mutable and tracks remediation, evidence, and status.
