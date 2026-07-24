---
title: Project Continuum H0 Repository Bootstrap Plan
document_id: continuum-h0-repository-bootstrap
version: 2.4
status: ready-for-execution
owner: Product Owner
last_updated: 2026-07-21
proposal: docs/strategy/project-continuum-proposal.md
proposal_version: 0.3
repository: https://github.com/maxaihappy/continuum
implementation_branch: bootstrap/h0
lineage: Manus v2.2; ChatGPT consolidation v2.3-v2.4
---

# Project Continuum - H0 Repository Bootstrap Plan

**Current baseline:** `main` contains one initial `README.md` commit.  
**Execution authority:** Implementation begins only after the product owner creates/approves the H0 GitHub issue and authorizes Cursor to execute this plan.  

---

## 1. Purpose

H0 establishes the repository and engineering-harness foundation required before substantive Project Continuum implementation begins. It creates a deterministic, auditable, agent-portable development environment and proves that work can move cleanly from planning to local implementation, independent review, GitHub evidence, and product-owner approval.

H0 delivers no user-facing Continuum behavior. It does not implement Telegram, model providers, a database, cloud infrastructure, deployment, memory, trust, proactivity, or relationship logic.

### H0 exit statement

H0 is complete when a qualified coding agent can clone the repository, follow `AGENTS.md`, run one documented bootstrap command and one documented test command, obtain green CI, and hand the pull request to an independent reviewer without relying on undocumented chat context or a required Manus, Cursor, ChatGPT, or Gemini runtime dependency.

---

## 2. Operating Roles and Handoff Model

| Role | Initial tool choice | Accountability |
|---|---|---|
| Product owner | Human | Defines intent, approves material decisions, approves plan and merge |
| Planner | ChatGPT or Gemini | Produces requirements, solution/design decisions, execution plan, risks, and evidence expectations |
| Editor / implementer | Cursor | Verifies repository state, edits files locally, runs checks, commits, pushes, and prepares the pull request |
| Independent reviewer | Manus | Reviews repository and PR evidence without planner-chat context; runs portability validation |
| Management and system of record | GitHub | Owns backlog issue, branch, commits, PR, CI evidence, review history, and merge record |

### Handoff rules

1. Chat output is advisory until converted into a versioned GitHub issue or repository artifact.
2. Cursor must validate the actual repository and local environment before implementing assumptions from this plan.
3. Manus receives only the repository, issue, PR, and documented commands for independent review; it should not rely on the planner conversation.
4. No named tool becomes a runtime dependency of Continuum or the harness.
5. Any tool may be replaced if the replacement can follow repository policy, execute the documented commands, produce required evidence, and respect approval gates.

---

## 3. Approved H0 Decisions

| Decision | Approved choice | Boundary |
|---|---|---|
| H0 tooling runtime | Python 3.12 | Applies only to repository tooling and tests; does not select the Continuum product runtime |
| Dependency manager | `uv` with committed `uv.lock` | CI and local checks fail if the lockfile is stale |
| Development dependencies | `ruff`, `pytest`, `detect-secrets`, `pre-commit` | No production dependencies in H0 |
| CI provider | GitHub Actions | No deployment jobs or secrets |
| Authoritative commands | Executable Bash scripts in `scripts/` | Makefile is convenience only |
| Architecture enforcement | Data-driven policy plus custom AST-based `pytest` checks | Specialized dependency tools deferred until a real H1 import graph exists |
| Secret detection | `detect-secrets` baseline plus pre-commit/CI gate | Baseline changes require explicit review; baselining a finding is not proof it is safe |
| Merge method for H0 | Merge commit | Preserves logical branch commits and PR history |
| Branch protection | Manual policy during H0 | Do not assume the current GitHub plan technically enforces it |

### Explicitly deferred

- Continuum application language and framework.
- Telegram adapter implementation and Bot API setup.
- Model-provider adapters and API keys.
- Database, event store, migrations, and ORM.
- Memory, trust, proactivity, learning, and action services.
- Cloud provider, containers, deployment, observability backend, and production secrets.
- Model evaluations and synthetic conversations beyond placeholder directories.
- Multi-agent automation beyond the documented planner/editor/reviewer handoff.

---

## 4. Repository Structure

Directories with no executable H0 behavior contain only a `README.md` placeholder. H0 does not create importable product packages.

```text
continuum/
├── AGENTS.md
├── ARCHITECTURE.md
├── SECURITY.md
├── PRIVACY.md
├── RELIABILITY.md
├── COST.md
├── README.md
├── .editorconfig
├── .gitignore
├── .python-version
├── .pre-commit-config.yaml
├── .secrets.baseline
├── architecture-boundaries.toml
├── pyproject.toml
├── uv.lock
├── Makefile
├── scripts/
│   ├── bootstrap
│   ├── check
│   ├── test
│   ├── secrets-check
│   └── secrets-baseline
├── packages/
│   ├── contracts/README.md
│   ├── channel_gateway/README.md
│   ├── relationship_core/README.md
│   ├── intelligence/README.md
│   └── memory_governance/README.md
├── harness/README.md
├── tests/
│   ├── architecture/test_package_boundaries.py
│   └── fixtures/README.md
├── evals/README.md
├── docs/
│   ├── strategy/
│   │   ├── project-continuum-proposal.md
│   │   └── assets/README.md
│   ├── reference/
│   │   └── exports/
│   │       └── project-continuum-proposal-v0.3.docx
│   ├── governance/
│   │   └── document-register.md
│   ├── product-specs/README.md
│   ├── design-docs/README.md
│   ├── decisions/
│   │   ├── README.md
│   │   └── adr-0001-h0-repository-bootstrap.md
│   ├── exec-plans/
│   │   ├── active/h0-bootstrap.md
│   │   └── completed/.gitkeep
│   ├── validation/h0-repository-bootstrap.md
│   ├── quality/README.md
│   ├── runbooks/README.md
│   └── generated/README.md
└── .github/
    ├── workflows/ci.yml
    ├── ISSUE_TEMPLATE/
    │   ├── requirement.md
    │   └── bug_report.md
    └── pull_request_template.md
```

### Artifact ownership

| Artifact | Owns |
|---|---|
| Canonical proposal (`docs/strategy/project-continuum-proposal.md`) | Product strategy, operating model, governance, stage definitions, and major constraints |
| Document register (`docs/governance/document-register.md`) | Current authoritative paths, document status, version, owner, and export relationships |
| GitHub requirement issue | Problem, desired outcome, scope, non-goals, acceptance criteria, risk, approval authority |
| ADR | Technical decision, alternatives, consequences, and rationale |
| Active execution plan | Ordered work, status, dependencies, deviations, and evidence links |
| Validation dossier | Test results, command outputs, reviewed commit, CI link, limitations, portability report, and release recommendation |
| Pull request | Concise summary and links to the issue, ADR, plan, validation dossier, and CI |
| GitHub merge record | Final authorization, merge commit, and completion timestamp |

Avoid copying the same detailed content into every artifact. Link instead.

### Document authority rule

- `docs/strategy/project-continuum-proposal.md` is the canonical strategic proposal.
- `docs/reference/exports/project-continuum-proposal-v0.3.docx` is a presentation export and must not be independently edited.
- The stable Markdown path remains unchanged across proposal versions; version metadata and Git history preserve change history.
- `docs/governance/document-register.md` identifies the current authoritative document and any superseded export.

---

## 5. Architecture Policy

`architecture-boundaries.toml` is the machine-readable policy. `ARCHITECTURE.md` explains the intent. `tests/architecture/test_package_boundaries.py` enforces the policy without importing product packages.

### H0 dependency intent

```text
product boundary placeholders  ──future──> contracts
harness tooling                ──────────> contracts and standard library only
tests                          ──────────> test utilities and documented public boundaries
```

### Rules

1. Product-domain directories may eventually depend on contracts, but not directly on another product-domain implementation.
2. Harness tooling must not depend on product-domain implementations.
3. Telegram, model-provider, database, and cloud SDK imports are location-restricted, not permanently banned.
4. In H0, no adapter or infrastructure source directory is approved, so such imports are prohibited in executable H0 files.
5. In H1+, an adapter directory is approved by updating the architecture policy and an ADR—not by weakening or bypassing the test.
6. Placeholder product directories must contain no executable source files during H0.

The test must fail with a clear message naming the violating file, import, applicable policy rule, and remediation path.

---

## 6. Command Contract

All scripts use:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

All tool invocations run through `uv run` after synchronization so the locked environment, not an agent's global PATH, determines tool versions.

### `scripts/bootstrap`

Purpose: establish a clean local environment, install the Git hook, and run all checks.

```bash
#!/usr/bin/env bash
set -euo pipefail

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install it using the documented prerequisite in README.md." >&2
  exit 1
fi

uv sync --locked
uv run pre-commit install
bash scripts/check
```

### `scripts/check`

Purpose: non-mutating full validation suitable for local use and CI.

```bash
#!/usr/bin/env bash
set -euo pipefail

uv run ruff format --check .
uv run ruff check .
bash scripts/test
bash scripts/secrets-check
```

### `scripts/test`

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run pytest -q tests/
```

### `scripts/secrets-check`

Purpose: run the configured detect-secrets hook against all files selected by pre-commit. It must not update the baseline.

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run pre-commit run detect-secrets --all-files
```

### `scripts/secrets-baseline`

Purpose: explicitly maintain the baseline. This is never run automatically by `scripts/check` or CI.

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run detect-secrets scan --baseline .secrets.baseline
printf '%s\n' \
  "Baseline updated." \
  "Review the diff and run: uv run detect-secrets audit .secrets.baseline" \
  "Do not commit a baseline change until every finding is classified."
```

### Secret-baseline policy

- H0 should finish with no unexplained baseline findings.
- Any `.secrets.baseline` change must be called out in the PR and manually reviewed.
- A real secret must be removed and rotated; it must not be accepted merely by adding it to the baseline.
- The validation dossier records whether the baseline changed and who reviewed it.

### Makefile

The Makefile may expose `bootstrap`, `check`, `test`, `secrets-check`, and `secrets-baseline`, but each target delegates directly to the corresponding script.

---

## 7. CI Requirements

`.github/workflows/ci.yml` must:

1. Trigger on pull requests targeting `main` and pushes to `main` or `bootstrap/**`.
2. Declare minimal permissions: `contents: read`.
3. Use concurrency to cancel superseded runs for the same branch or PR.
4. Install Python 3.12 and `uv` without using repository secrets.
5. Run `uv sync --locked` followed by `scripts/check`.
6. Avoid deployment, cloud credentials, external service calls, and generated commits.
7. Pin every GitHub Action to a full-length commit SHA, with a comment noting the corresponding release tag.
8. Fail on stale `uv.lock`, formatting, lint, tests, architecture violations, or unbaselined secret findings.

CI is evidence, not authority to merge. H0 merge still requires explicit product-owner approval.

---

## 8. Implementation Sequence

### Precondition

- The product owner explicitly approves this plan.
- The H0 GitHub requirement issue is created and its number is known.
- Cursor can read these three approved source files before editing the repository:
  - `project-continuum-proposal.md`
  - `Project_Continuum_Proposal_Harness_Engineering_v0.3.docx`
  - `h0-repository-bootstrap.md`
- Cursor verifies the local clone has the expected remote, clean `main`, and no uncommitted work.
- Cursor records any mismatch between the source files, the issue, and the repository instead of silently choosing one.

### Step 1 — Create the GitHub requirement issue

Create the issue using Appendix A. Record issue number `#N`.

**Gate:** No branch work begins until the issue exists.

### Step 2 — Cursor validates current state

Run and record:

```bash
git remote -v
git branch --show-current
git status --short
git log --oneline --decorate -5
python3 --version || true
uv --version || true
gh --version || true
```

Cursor reports discrepancies before changing files. It must not silently change the remote, install global software, or choose a different runtime.

### Step 3 — Create branch

```bash
git switch -c bootstrap/h0
```

### Step 4 — First commit and draft PR

The first commit contains:

- This approved plan at `docs/exec-plans/active/h0-bootstrap.md`.
- The canonical proposal at `docs/strategy/project-continuum-proposal.md`.
- The unmodified Word export at `docs/reference/exports/project-continuum-proposal-v0.3.docx`.
- The initial document register at `docs/governance/document-register.md`.
- ADR-0001 stub with status `proposed`.
- Validation dossier stub.
- The directory tree and placeholder README files.
- A minimal root README update.

The first commit must record SHA-256 hashes of the three approved input files in the active execution plan so later review can prove which inputs Cursor used.

Commit:

```text
chore(scaffold): establish H0 plan, ADR, validation stub, and repository tree
```

Push and open a draft PR linked to issue `#N`:

```bash
git push -u origin bootstrap/h0
gh pr create \
  --title "H0: Repository bootstrap" \
  --body "Draft implementation for issue #N. See docs/exec-plans/active/h0-bootstrap.md." \
  --base main \
  --head bootstrap/h0 \
  --draft
```

Record PR number `#M` in the active plan.

### Step 5 — Governance and navigation

Complete:

- `AGENTS.md`
- `ARCHITECTURE.md`
- `SECURITY.md`
- `PRIVACY.md`
- `RELIABILITY.md`
- `COST.md`
- Root `README.md`

`AGENTS.md` must be short and navigational. It must name the authoritative commands, source-of-truth artifacts, branch policy, approval gates, escalation conditions, and links to deeper documents. It must direct every agent to read the canonical proposal, architecture rules, current execution plan, ADRs, and validation evidence in that order. It must state that Markdown sources override presentation exports.

`docs/governance/document-register.md` must list the proposal Markdown file as active and authoritative, the v0.3 DOCX as a non-authoritative export, and the H0 plan as the active execution plan.

Commit:

```text
docs(governance): add agent map and engineering policy documents
```

### Step 6 — Locked H0 tooling environment

Create:

- `pyproject.toml` configured as a non-package tooling project.
- `[dependency-groups].dev` entries for `ruff`, `pytest`, `detect-secrets`, and `pre-commit`.
- `.python-version` specifying Python 3.12.
- `uv.lock` generated by `uv lock`.

No production dependency and no importable Continuum package is permitted.

Commit:

```text
chore(deps): add locked H0 tooling environment
```

### Step 7 — Command scripts and editor hygiene

Create the authoritative scripts, thin Makefile wrappers, `.editorconfig`, and `.gitignore`. Mark scripts executable and verify executable bits are tracked by Git.

Commit:

```text
chore(scripts): add authoritative bootstrap and validation commands
```

### Step 8 — Pre-commit and secret baseline

Configure pinned pre-commit hooks for:

- Ruff formatting.
- Ruff linting.
- Detect-secrets using `.secrets.baseline`.
- Trailing whitespace.
- End-of-file fixes.
- YAML and TOML checks.

Generate the initial baseline, audit every finding, and document the result. Pre-commit dependencies and GitHub Actions must use immutable revisions where supported.

Commit:

```text
chore(tooling): add pre-commit policy and reviewed secrets baseline
```

### Step 9 — Architecture policy and test

Create `architecture-boundaries.toml` and the AST-based architecture test. Tests must cover both compliant and violating fixture cases so the suite proves it can fail, not merely pass against an empty tree.

Minimum fixtures:

- Allowed standard-library import in harness tooling.
- Disallowed product-to-product import.
- Disallowed provider SDK import outside an approved adapter path.
- Approved adapter-path behavior represented by an isolated fixture policy, without creating real adapter code.

Commit:

```text
test(architecture): add policy-driven boundary checks and failure fixtures
```

### Step 10 — GitHub templates and CI

Create the requirement issue template, bug template, PR template, and secure CI workflow. Run the workflow on the branch and resolve failures without weakening checks.

Commit:

```text
ci: add GitHub templates and secure H0 validation workflow
```

### Step 11 — Complete ADR-0001

Change ADR status from `proposed` to `accepted`. Record:

- H0-only Python decision.
- `uv` and lockfile choice.
- Command contract.
- Monorepo/bootstrap structure.
- Location-aware architecture policy.
- Secret-baseline policy.
- Deferred product runtime and infrastructure choices.

Commit:

```text
docs(decisions): accept ADR-0001 for H0 repository bootstrap
```

### Step 12 — Candidate validation commit

Run:

```bash
bash scripts/bootstrap
bash scripts/test
bash scripts/secrets-check
git status --short
```

Fix all failures. Commit any fixes. Record the candidate implementation commit:

```bash
git rev-parse HEAD
```

Call this `VALIDATED_SOURCE_COMMIT`. This value may be recorded in the validation dossier because it refers to the completed implementation before evidence-closeout documents are committed.

### Step 13 — Independent Manus portability and review pass

Manus receives only:

- Repository URL and branch.
- GitHub issue.
- Draft PR.
- Instruction to begin with `AGENTS.md`.

Manus must:

1. Use a fresh clone or clean isolated checkout of `VALIDATED_SOURCE_COMMIT`.
2. Run `scripts/bootstrap`, `scripts/test`, and `scripts/secrets-check`.
3. Confirm no planner-chat context was required.
4. Review architecture policy, CI security, secret-baseline changes, and artifact links.
5. Report blockers, non-blocking findings, and exact evidence.

Any blocker returns the work to Cursor. Cursor fixes it, creates a new candidate commit, and Manus repeats the affected validation.

### Step 14 — Final validation dossier and plan closure

Complete `docs/validation/h0-repository-bootstrap.md` with:

- Requirement coverage.
- The approved-input SHA-256 hashes and confirmation that the committed proposal, DOCX export, and H0 plan match those inputs.
- Document-register review confirming that authoritative and export formats are unambiguous.
- `VALIDATED_SOURCE_COMMIT`.
- Local command outputs or concise machine-readable summaries.
- CI run link and result.
- Secret-baseline review result.
- Architecture-test positive and negative fixture results.
- Manus portability-review result and any resolved findings.
- Known limitations.
- Rollout statement: none.
- Rollback: revert the H0 merge commit.
- Recommendation: approve or reject merge.

Move the active plan to:

```text
docs/exec-plans/completed/h0-bootstrap.md
```

Set status to `ready-for-merge`. Do **not** claim the closing commit or merge commit SHA inside the same commit that creates it. The PR and GitHub merge record remain authoritative for those SHAs.

Commit:

```text
docs(validation): finalize H0 evidence and mark plan ready for merge
```

### Step 15 — Final CI and ready-for-review

- Push the evidence-closeout commit.
- Confirm CI is green on the actual PR head.
- Update the PR body with links to issue, accepted ADR, completed plan, validation dossier, and CI.
- Convert the draft PR to ready for review.
- Stop. Do not merge.

### Step 16 — Product-owner approval and merge

The product owner reviews:

- Scope and changed files.
- Validation dossier.
- Manus findings.
- CI result.
- Secret-baseline diff.
- Known limitations and rollback.

On explicit approval, merge using a merge commit. Close issue `#N` through the PR relationship or manually after verifying the merge. No post-merge direct edit to `main` is required for H0 closeout.

---

## 9. Acceptance Criteria and Evidence

| Acceptance criterion | Required evidence |
|---|---|
| `scripts/bootstrap` succeeds from a fresh clone with documented prerequisites | Manus fresh-clone output and validation-dossier summary |
| `scripts/test` passes | Pytest output, including tests that prove architecture violations are detected |
| `scripts/secrets-check` passes without modifying the baseline | Command output and clean Git status |
| `uv.lock` matches `pyproject.toml` | `uv sync --locked` succeeds locally and in CI |
| CI is green on the final PR head | GitHub Actions run link |
| CI uses least privilege and immutable action references | Workflow review recorded in validation dossier |
| Repository contains all required H0 artifacts | Requirement-coverage table |
| Canonical proposal, Word export, and H0 plan are committed at their approved paths and match the approved input hashes | Git history, input-hash record, and validation dossier |
| Document register clearly identifies authoritative Markdown and non-authoritative exports | Document-register review in validation dossier |
| `AGENTS.md` links agents to the canonical proposal and current plan | Manus portability review |
| Product placeholders contain no implementation code | Tree inspection and architecture test |
| No Telegram, provider, database, cloud, deployment, or product behavior is introduced | Changed-file review and dependency inventory |
| `AGENTS.md` is sufficient for an independent reviewer | Manus reports no undocumented-context dependency |
| Secret baseline contains no unexplained finding | Human audit record and baseline diff review |
| Issue → ADR → plan → branch → PR → CI → validation links are complete | Link audit in dossier |
| No direct push to `main` and no auto-merge occurred | GitHub branch and PR history |
| Product owner explicitly approved merge | GitHub PR approval/comment and merge record |

---

## 10. Definition of Done

H0 is done only when all of the following are true:

- The PR contains no substantive Continuum product behavior.
- The canonical proposal, its Word export, the document register, and the approved H0 plan are committed and linked from `AGENTS.md`.
- The final PR head passes CI.
- The locked bootstrap and test commands pass in a fresh independent checkout.
- Architecture tests include negative fixtures and demonstrably fail on prohibited imports.
- The secrets baseline is reviewed and contains no unexplained secret.
- Manus completes an independent portability and review pass without planner-chat context.
- The validation dossier recommends merge and links all evidence.
- The execution plan is committed under `completed/` with status `ready-for-merge`.
- The product owner explicitly approves and performs or authorizes the merge.
- GitHub records the final merge and issue closeout.

---

## 11. Risks and Controls

| Risk | Control |
|---|---|
| H0 accidentally selects the product language | Python is explicitly limited to H0 tooling; product directories remain README-only |
| Empty tests create false confidence | Architecture suite includes violating fixtures that must be rejected |
| A secret is hidden in the baseline | Baseline changes require manual audit and PR callout; real secrets must be removed and rotated |
| CI action supply-chain compromise | Actions are pinned to full-length commit SHAs and workflow permissions are read-only |
| Planner assumptions differ from local reality | Cursor performs current-state validation before editing |
| Reviewer repeats planner assumptions | Manus receives only repository and GitHub evidence |
| Evidence document refers to its own nonexistent final SHA | Dossier records the prior candidate implementation SHA; GitHub records final and merge SHAs |
| Manual branch policy is bypassed | Product owner checks PR and GitHub history before merge |
| H0 grows into product development | Explicit non-goals and changed-file review gate |
| Tool lock-in | Standard files, Git, Bash, Python tooling, and GitHub artifacts; no required planner/editor/reviewer runtime dependency |
| Proposal Markdown and Word export drift apart | Markdown is explicitly authoritative; export is copied unchanged and registered as non-authoritative; future exports are generated from the canonical source |

---

## Appendix A — GitHub Requirement Issue

**Title**

```text
H0: Repository bootstrap — establish the engineering-harness foundation
```

**Body**

```markdown
## Problem and desired outcome

The repository currently contains only an initial README. Before substantive
Continuum development begins, the project needs a deterministic, auditable,
and agent-portable repository foundation.

Desired outcome: a qualified coding agent can clone the repository, follow
AGENTS.md, run scripts/bootstrap and scripts/test, obtain green CI, and hand
the change to an independent reviewer without undocumented chat context.

## Acceptance criteria

- [ ] scripts/bootstrap succeeds from a fresh clone with documented prerequisites.
- [ ] scripts/test passes, including negative architecture-policy fixtures.
- [ ] scripts/secrets-check passes without modifying .secrets.baseline.
- [ ] uv sync --locked succeeds locally and in CI.
- [ ] GitHub Actions is green on the final PR head.
- [ ] Required H0 governance, architecture, plan, validation, template, and
      command artifacts exist and are linked.
- [ ] The canonical proposal is committed at
      docs/strategy/project-continuum-proposal.md.
- [ ] The v0.3 DOCX is committed as a non-authoritative export at
      docs/reference/exports/project-continuum-proposal-v0.3.docx.
- [ ] docs/governance/document-register.md clearly identifies document
      authority, status, version, and owner.
- [ ] Manus completes independent portability validation using only repository
      and GitHub evidence.
- [ ] No Telegram, provider, database, cloud, deployment, or substantive
      product behavior is introduced.
- [ ] Merge requires explicit product-owner approval.

## Constraints and non-goals

No product implementation, Telegram bot, model-provider integration, database,
cloud infrastructure, deployment environment, credentials, or autonomous merge.
Python 3.12 is approved for H0 tooling only; the product runtime is deferred.

## Risk and data classification

Risk: low. Data sensitivity: none. No user data or external service access.

## Deployment authority

No deployment. Work occurs on bootstrap/h0. Merge to main requires explicit
product-owner approval.

## Evidence

Authoritative product context:
docs/strategy/project-continuum-proposal.md

Authoritative execution plan:
docs/exec-plans/active/h0-bootstrap.md

Authoritative validation dossier:
docs/validation/h0-repository-bootstrap.md

## Proposal reference

Project Continuum Proposal, Harness Engineering v0.3 — H0 repository bootstrap,
repository-as-system-of-record, cross-tool handoff, and audit model.
```

---

## Appendix B — Cursor Execution Prompt

Use this after the GitHub issue is created and replace `#N` with its number.

```text
Implement GitHub issue #N using the approved H0 execution plan attached to this
request. The target repository is https://github.com/maxaihappy/continuum.

Approved local inputs supplied with this request:
- project-continuum-proposal.md
- Project_Continuum_Proposal_Harness_Engineering_v0.3.docx
- h0-repository-bootstrap.md

You are the editor and implementation agent. GitHub and the repository are the
source of truth. Do not rely on undocumented assumptions from this chat. Copy
the approved Markdown files without changing their product intent. Copy the
DOCX export byte-for-byte; do not edit it.

Before editing:
1. Verify remote, branch, clean status, recent commits, Python, uv, and gh.
2. Report any discrepancy from the plan.
3. Do not install global software or change the remote without approval.

Then execute the plan exactly:
- Create branch bootstrap/h0.
- Calculate and record SHA-256 hashes for the three approved inputs.
- Make the canonical proposal, unmodified DOCX export, document register,
  approved execution plan, ADR stub, validation stub, and repository tree the
  first commit.
- Push and open a draft PR immediately after the first commit.
- Continue through implementation, local checks, CI remediation, and candidate
  validation.
- Do not implement Continuum product behavior.
- Do not add secrets, cloud resources, deployment, Telegram, providers, or a
  database.
- Do not push to main, merge, or enable auto-merge.
- Preserve small logical commits and keep the active execution plan updated.
- Stop when the PR is ready for independent Manus review, and provide the PR
  link, candidate commit SHA, commands run, and current evidence status.
```

---

## Appendix C — Manus Independent Review Prompt

Use after Cursor identifies `VALIDATED_SOURCE_COMMIT` and a draft PR.

```text
Independently review Project Continuum H0 using only the repository and GitHub
artifacts. Do not use prior planner or implementation chat context.

Repository: https://github.com/maxaihappy/continuum
Branch: bootstrap/h0
Issue: #N
Pull request: #M
Candidate commit: VALIDATED_SOURCE_COMMIT

Begin with AGENTS.md. Use a fresh clone or isolated clean checkout at the
candidate commit. Run scripts/bootstrap, scripts/test, and scripts/secrets-check.

Review:
- Whether AGENTS.md is sufficient without undocumented context
- Architecture policy and both positive/negative test fixtures
- CI permissions and immutable action references
- uv lock consistency
- Secret-baseline changes and audit evidence
- Traceability among proposal, document register, issue, ADR, plan, branch, PR,
  CI, and validation dossier
- Whether the committed Markdown proposal and DOCX export match the approved
  input hashes and document authority is unambiguous
- Compliance with H0 non-goals

Return blockers, non-blocking findings, evidence, and a clear approve/reject
recommendation. Do not modify or merge the repository unless explicitly asked.
```

---

*Plan v2.4 is execution-ready. Implementation begins only after explicit product-owner approval and creation of the H0 GitHub issue.*
