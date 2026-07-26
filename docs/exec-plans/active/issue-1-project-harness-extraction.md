---
title: Issue #1 Project Harness Extraction Plan
document_id: issue-1-project-harness-extraction
version: 1.1
status: ready-for-execution
owner: Product Owner
last_updated: 2026-07-25
requirement_issue: https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1
implementation_branch: foundation/extract-project-harness
source_repository: https://github.com/maxaihappy/continuum
source_commit: 7c8e04e1e864ee70bd18ffdad29d6517aecde1f7
continuum_source_tag: h0-bootstrap-baseline
harness_import_tag: imported-continuum-h0
lineage: Continuum H0 import; Issue #1 planning initialization
---

## Execution record (planning initialized)

This file is the **active execution plan** for Issue #1. Historical H0 evidence in this repository validates the imported Continuum H0 baseline only; it does **not** validate Issue #1 extraction work.

| Artifact | Status |
|---|---|
| Requirement issue | [#1](https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1) — open |
| Implementation branch | `foundation/extract-project-harness` — created |
| Draft pull request | [#2 — draft](https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2) |
| Reviewed implementation candidate | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` |
| Independent review report | [issue-1-manus-independent-review-d10a3c22.md](../../validation/reviews/issue-1-manus-independent-review-d10a3c22.md) |
| Access-block review report | [issue-1-manus-access-block-d10a3c22.md](../../validation/reviews/issue-1-manus-access-block-d10a3c22.md) — preserved |
| Manus recommendation | **BLOCK** |
| Remediation | **in progress** |
| ADR for extraction decisions | [ADR-0002](../../decisions/adr-0002-project-harness-extraction.md) — accepted |
| Validation dossier | [docs/validation/issue-1-project-harness-extraction.md](../../validation/issue-1-project-harness-extraction.md) — remediation evidence |
| Independent re-review | **not yet completed** |
| Closeout | **not yet completed** |
| Final delta review | **not yet required** |
| Product-owner merge approval | **not yet requested** |
| Merge | **not yet completed** |

### Source baseline (immutable reference)

| Reference | Value |
|---|---|
| Source repository | https://github.com/maxaihappy/continuum |
| Source commit | `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7` |
| Continuum source tag | `h0-bootstrap-baseline` |
| Harness import tag | `imported-continuum-h0` |
| Import state | Unmodified Continuum H0 tree at source commit |

Do not modify the original Continuum repository. Rollback and provenance rely on the references above.

---

# Issue #1 — Extract Reusable Project Harness from Continuum H0

**Current baseline:** `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7` (tagged `imported-continuum-h0`).
**Execution authority:** Implementation begins only after this plan is committed and the product owner authorizes extraction work on Issue #1.

---

## 1. Purpose

Issue #1 generalizes the validated Continuum H0 engineering harness into a reusable, product-neutral project harness and repository bootstrap kit. The outcome must preserve the validated engineering workflow while removing unintended Continuum-specific assumptions, paths, names, and evidence coupling.

This work delivers no Continuum product behavior, no deployment, no infrastructure, and no template-repository mode until the generalized harness is validated, reviewed, approved, and merged.

### Issue #1 exit statement

Issue #1 is complete when a documented process can create a clean new product repository from the harness, a disposable generated repository passes all documented validation commands, remaining Continuum references are intentional provenance or examples, CI is green on the exact implementation commit, independent review is preserved byte-for-byte at an exact 40-character SHA, any post-review commits receive a narrow delta review, and merge occurs only after explicit product-owner approval with auto-merge disabled and template mode enabled only after merge.

---

## 2. Operating Roles and Handoff Model

| Role | Example tool choice | Accountability |
|---|---|---|
| Product owner | Human | Defines intent, approves material decisions, approves plan and merge |
| Planner | ChatGPT, Gemini, or equivalent | Produces requirements, design decisions, execution plan, risks, and evidence expectations |
| Editor / implementer | Cursor or equivalent | Verifies repository state, edits files locally, runs checks, commits, pushes, and prepares the pull request |
| Independent reviewer | Manus or equivalent | Reviews repository and PR evidence without planner-chat context; runs portability validation |
| Repository authority | GitHub | Owns backlog issue, branch, commits, PR, CI evidence, review history, and merge record |

### Handoff rules

1. Chat output is advisory until converted into a versioned GitHub issue or repository artifact.
2. The implementer must validate the actual repository and local environment before implementing assumptions from this plan.
3. The independent reviewer receives only the repository, issue, PR, and documented commands; it should not rely on the planner conversation.
4. No named tool becomes a runtime dependency of the harness or generated product repositories.
5. Cursor, Manus, and GitHub are example operating configuration, not universal requirements.

---

## 3. Scope and Non-Goals

### In scope

- Replace unintended Continuum-specific names, paths, assumptions, and operational wording.
- Separate reusable governance rules from project-specific configuration.
- Define responsibility-based roles (product owner, implementation agent, independent reviewer, repository authority).
- Preserve Cursor, Manus, and GitHub as an example operating configuration.
- Add initialization and usage documentation for new projects.
- Add a checklist for creating a new repository from the harness.
- Add validation that detects unintended residual Continuum references.
- Remove machine-specific operational paths from reusable templates.
- Preserve CI, validation, secret scanning, architecture, traceability, evidence, approval, rollback, and independent-review capabilities.
- Define the boundary between the reusable harness repository and generated product repositories.
- Validate the harness using a disposable generated repository.

### Non-goals

- No Continuum business behavior.
- No new application functionality.
- No deployment or infrastructure creation.
- No programming-language or application-framework selection for generated products.
- No automatic GitHub administration.
- No rewriting of Continuum history.
- No modification of the original Continuum repository.
- No automatic upgrade mechanism between the harness and generated projects.
- No enabling of template-repository mode before validation and merge.

---

## 4. Repository Artifacts for Issue #1

| Artifact | Path | Role |
|---|---|---|
| Requirement issue | GitHub Issue #1 | Problem, scope, acceptance criteria, rollback, safety constraints |
| Active execution plan | `docs/exec-plans/active/issue-1-project-harness-extraction.md` | Ordered work, status, dependencies, deviations, evidence links |
| Validation dossier | `docs/validation/issue-1-project-harness-extraction.md` | Test results, reviewed commit, CI link, limitations, review record |
| ADR(s) | `docs/decisions/` | Material extraction decisions (to be created during implementation) |
| Document register | `docs/governance/document-register.md` | Authoritative paths, status, version, owner |
| Pull request | GitHub PR (draft, then ready) | Summary and links to issue, ADR, plan, validation dossier, CI |

### Historical H0 artifacts (provenance only)

The following artifacts document the imported Continuum H0 baseline. They are **not** Issue #1 validation evidence:

- `docs/exec-plans/completed/h0-repository-bootstrap.md`
- `docs/validation/h0-repository-bootstrap.md`
- `docs/validation/reviews/h0-manus-*.md`
- `docs/reference/approved-inputs/h0-repository-bootstrap-approved.md`

---

## 5. Command Contract (unchanged for Issue #1 planning)

Authoritative validation commands remain:

| Command | Purpose |
|---|---|
| `bash scripts/bootstrap` | Install locked deps, Git hooks, and run full checks |
| `bash scripts/check` | Non-mutating full validation (format, lint, test, secrets) |
| `bash scripts/test` | Run pytest suite |
| `bash scripts/secrets-check` | Run detect-secrets without modifying baseline |

Issue #1 implementation will add harness-specific tests (residual-reference detection, template generation, clean-room generation) as defined in later implementation steps. Those tests do not exist yet.

---

## 6. Implementation Sequence

### Phase status summary

| Phase | Status |
|---|---|
| Planning initialization | **completed** at `8b980d8b673acf8a8da5c268257cb4f8c1d8c4b9` |
| Draft pull request | **completed** — PR #2 |
| Implementation | **completed** (Steps 3–7) at `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` |
| Local validation | **completed** at reviewed candidate |
| Independent review | **completed** — BLOCK at `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` |
| Remediation | **in progress** |
| CI | **not yet completed** for remediation commit |
| Closeout | **not yet completed** |
| Final delta review | **not yet completed** |
| Merge | **not yet completed** |
| Template activation | **not yet completed** |

### Precondition

- GitHub Issue #1 exists and is open.
- Branch `foundation/extract-project-harness` exists at source commit `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7`.
- Tag `imported-continuum-h0` marks the unmodified import.
- Product owner approves this plan before substantive extraction edits begin.

### Step 1 — Planning initialization (this step)

Commit:

- This active execution plan.
- The Issue #1 validation dossier stub.
- Document-register entries for both artifacts.

Record issue #1, branch, source commit, source tags, and future PR placeholder in both artifacts.

**Gate:** No extraction implementation begins until this planning commit lands and the product owner authorizes implementation.

### Step 2 — Create draft pull request — completed

- PR: #2
- URL: https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2
- Base: `main`
- Head: `foundation/extract-project-harness`
- State: draft
- Planning commit: `8b980d8b673acf8a8da5c268257cb4f8c1d8c4b9`

### Step 3 — Generalize governance and navigation — completed

- Updated `AGENTS.md`, `README.md`, policy documents, and `harness-config.toml`.
- Added harness-versus-generated boundary documentation.
- Added initialization and new-repository checklist runbooks.

### Step 4 — Remove unintended Continuum coupling — completed

- Renamed Continuum-specific package directories to neutral placeholders.
- Generalized operational documentation and tooling package name.
- Preserved intentional provenance under `docs/reference/`, `docs/validation/h0-*`, and `docs/exec-plans/completed/`.

### Step 5 — Add harness-specific validation — completed

- Added `tests/test_residual_references.py`, `tests/test_template_generation.py`, and `tests/test_clean_room_generation.py`.
- Extended `tests/test_traceability.py` for Issue #1 artifacts.

### Step 6 — Validate with disposable generated repository — completed

- Clean-room test generates a disposable repository, runs `uv lock`, and passes `scripts/bootstrap`, `scripts/test`, `scripts/secrets-check`, and `scripts/check`.

### Step 7 — ADR and architecture updates — completed

- Accepted [ADR-0002](../../decisions/adr-0002-project-harness-extraction.md).
- Updated `architecture-boundaries.toml` for neutral domain placeholders and harness tooling paths.
- Extended CI push triggers to `foundation/**`.

### Step 8 — Candidate validation commit — completed locally

Run and record:

```bash
bash scripts/bootstrap
bash scripts/test
bash scripts/secrets-check
bash scripts/check
```

Local results: all commands passed; 45 tests including architecture, traceability, residual-reference, template-generation, and clean-room suites.

`VALIDATED_SOURCE_COMMIT` will be recorded after the implementation commit lands. Independent review, closeout, and merge remain pending.

### Step 9 — Independent review

The independent reviewer receives only:

- Repository URL and branch.
- GitHub Issue #1.
- Draft or ready pull request.
- Instruction to begin with `AGENTS.md`.
- Exact candidate commit SHA.

The reviewer must use a fresh clone or clean isolated checkout pinned to the exact 40-character SHA, run documented commands, and preserve review evidence byte-for-byte.

### Step 10 — Remediation (in progress)

Independent review at `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` returned **BLOCK**. Findings B-01, H-01, M-01, M-02, and L-01 are being remediated. Review reports:

- [issue-1-manus-independent-review-d10a3c22.md](../../validation/reviews/issue-1-manus-independent-review-d10a3c22.md)
- [issue-1-manus-access-block-d10a3c22.md](../../validation/reviews/issue-1-manus-access-block-d10a3c22.md) (preserved)

### Step 11 — Independent re-review

**Not yet completed.** Repeat independent review at the remediation candidate SHA after local validation and CI pass.

### Step 12 — Closeout

- Finalize the validation dossier with requirement coverage, command outputs, CI links, review record, limitations, and rollback.
- Move this plan to `docs/exec-plans/completed/issue-1-project-harness-extraction.md`.
- Set plan status to `ready-for-merge`.
- Confirm CI is green on the PR head.

### Step 13 — Final delta review (if needed)

If any commits land after the independently reviewed implementation commit, obtain a narrow delta review before merge.

### Step 14 — Product-owner approval and merge

- Product owner reviews scope, validation dossier, independent review, CI, and rollback.
- Merge using a merge commit after explicit approval.
- Enable template-repository mode only after merge.
- Do not enable auto-merge.

---

## 7. Acceptance Criteria and Evidence

| Acceptance criterion | Required evidence | Status |
|---|---|---|
| Project-specific values are configurable or clearly documented | Documentation and configuration review | **not yet completed** |
| Remaining Continuum references are intentional provenance or examples | Residual-reference validation and changed-file review | **not yet completed** |
| No machine-specific local paths remain in operational templates | Template and documentation review | **not yet completed** |
| A documented process can create a clean new product repository | New-repository checklist and generation procedure | **not yet completed** |
| A disposable generated repository passes all documented validation commands | Generated-repository validation record | **not yet completed** |
| Generated repositories do not misrepresent Continuum evidence as their own | Generated-repository evidence boundary review | **not yet completed** |
| CI passes on the exact implementation commit | GitHub Actions run link and head SHA | **not yet completed** |
| Independent review uses an isolated clone pinned to an exact 40-character SHA | Review report with candidate SHA | **not yet completed** |
| Independent-review evidence is preserved byte-for-byte | Committed review artifacts under `docs/validation/reviews/` | **not yet completed** |
| Final PR-head CI is green | GitHub Actions run link on PR head | **not yet completed** |
| Post-review commits receive a narrow delta review when applicable | Delta review record | **not yet completed** |
| Product-owner approval is required before merge | GitHub approval record | **not yet completed** |
| Auto-merge remains disabled | GitHub PR settings evidence | **not yet completed** |
| Template-repository mode enabled only after validated merge | GitHub repository settings evidence | **not yet completed** |

---

## 8. Rollback

Revert the extraction pull request on `main`.

The immutable source remains available through:

- Continuum tag: `h0-bootstrap-baseline`
- Harness tag: `imported-continuum-h0`
- Source commit: `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7`

---

## 9. Review Requirements

- Independent review must not rely on planner or implementer chat context.
- Review begins from `AGENTS.md` and documented commands only.
- Review uses a fresh clone or isolated checkout at the exact reviewed candidate SHA.
- Review evidence is committed under `docs/validation/reviews/` without modification.
- Any remediation must produce a new candidate commit and a repeated or delta review as appropriate.
- Product-owner approval is mandatory before merge.

---

## 10. Safety Constraints

- Do not push directly to `main`.
- Do not merge without explicit product-owner approval.
- Do not deploy or create infrastructure.
- Do not enable auto-merge.
- Do not modify the original Continuum repository.
- Do not enable template-repository mode before validation and merge.
- Do not claim tests, CI, review, push, save, or merge succeeded without evidence.

---

*Plan v1.1 records completion of planning initialization and draft PR creation. Extraction implementation begins only after explicit product-owner authorization.*
