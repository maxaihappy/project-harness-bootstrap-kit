# Independent Review Report

**Review date:** 2026-07-26 PDT  
**Reviewer role:** Independent reviewer; review-only  
**Recommendation:** **BLOCK**

## Review target

This is a fresh, independent re-review of **GitHub Issue #1**, limited to the exact remediation candidate `b5d62179864fed7a68e2210e396e83d9835ee464`. It assesses the candidate against the imported H0 baseline `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7`, the prior blocked candidate `d10a3c22b814a853e0975a8bc9034ce4575ce4ff`, GitHub Issue #1, and GitHub Pull Request #2. No moving branch tip was substituted for the specified candidate. [1] [2] [3] [4]

| Review parameter | Value |
|---|---|
| Repository | `https://github.com/maxaihappy/project-harness-bootstrap-kit` |
| Approved issue scope | GitHub Issue #1 — *Extract reusable project harness from Continuum H0* [1] |
| Pull-request provenance | GitHub PR #2 — open draft, `main` ← `foundation/extract-project-harness` [2] |
| Imported H0 baseline | `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7` [4] |
| Previously blocked candidate | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` [5] |
| Sole remediation candidate reviewed | `b5d62179864fed7a68e2210e396e83d9835ee464` [3] |
| Required primary diff | `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7..b5d62179864fed7a68e2210e396e83d9835ee464` |
| Required remediation delta | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff..b5d62179864fed7a68e2210e396e83d9835ee464` |
| Required CI run | GitHub Actions run `30214792101` [15] |

The review performed no source edit, commit, push, merge, deployment, infrastructure action, auto-merge change, or template-repository change. The source checkout remained at the exact candidate and had no tracked or untracked worktree changes after validation.

## Isolation and checkout verification

A new isolated clone was created only for this re-review. `AGENTS.md` was successfully read before any other repository document, as required. GitHub Issue #1 and PR #2 were successfully accessed in read-only mode before substantive assessment. [1] [2] [6]

| Required verification | Actual observed result |
|---|---|
| Fresh clone path | `/home/ubuntu/independent-review-issue1-b5d621-SQ11ZS` |
| Origin URL | `https://github.com/maxaihappy/project-harness-bootstrap-kit` |
| Exact `HEAD` SHA | `b5d62179864fed7a68e2210e396e83d9835ee464` |
| Checkout state | Detached `HEAD`; no branch symbolic reference was present |
| `git status --short` before review | No output |
| Untracked-file check before review | `git ls-files --others --exclude-standard` produced no output |
| Untracked files existed | No |
| Issue #1 access | Successful, read-only [1] |
| PR #2 access | Successful, read-only [2] |
| `AGENTS.md` access | Successful; read first [6] |
| Checkout state after validation | `git status --short` and untracked-file check both produced no output; `HEAD` remained the exact candidate |

The initial checkout-verification command log is preserved at `phase1_checkout_verification.txt`; the post-validation integrity log is preserved at `post_validation_checkout_integrity.txt` alongside this report.

## Materials reviewed

The review used only the detached candidate checkout and GitHub evidence. Historical H0 content was treated as provenance only, not as evidence that Issue #1 itself is complete, consistent with the repository authority rules. [6] [7] [8]

| Material category | Materials assessed |
|---|---|
| Requirements and GitHub history | Issue #1, PR #2, candidate and baseline commit relationships, live CI run metadata, current PR head and repository governance metadata [1] [2] [3] [15] [16] |
| Repository navigation and configuration | `AGENTS.md`, `harness-config.toml`, `ARCHITECTURE.md`, `architecture-boundaries.toml`, README, runbooks, and harness/generated-boundary documentation [6] [9] [10] [11] |
| Issue evidence and design records | Active Issue #1 execution plan, Issue #1 validation dossier, document register, ADR-0001, ADR-0002, preserved prior Issue #1 review reports [7] [8] [12] [13] [14] |
| Generator and generated output | `scripts/generate-project`, `harness/generator/render.py`, `harness/generator/workflow.py`, generated README and AGENTS files, generated Makefile and secrets-baseline script [17] [18] [19] [20] [21] |
| Validation controls | Root scripts, Makefile, Python manifest and lockfile, CI workflow, secret baseline, pre-commit configuration, architecture enforcement, traceability enforcement, and all Issue #1-focused tests [22] [23] [24] [25] [26] |

## Diff summary

The baseline-to-candidate comparison changed **69 files**, with **2,614 insertions** and **106 deletions**. The remediation-only comparison changed **17 files**, with **808 insertions** and **130 deletions**. Both required commit objects exist locally, and the baseline and prior candidate are ancestors of the remediation candidate.

The remediation delta adds an explicit `--overwrite` interface, a guarded default for non-empty targets, a canonical post-generation command sequence beginning with `git init`, a generated `scripts/secrets-baseline`, residual-reference test coverage for `harness/`, focused regression tests, and preserved reports for the prior blocked review. It also updates the plan and dossier from a pre-review state to a recorded prior-`BLOCK` remediation state. [7] [8] [17] [18] [19]

The exact `git diff --check` comparisons did **not** exit successfully. Both report two trailing-whitespace lines in the newly preserved prior independent-review report. The candidate’s pre-commit configuration explicitly excludes those Issue #1 review reports from whitespace and end-of-file normalization to preserve them byte-for-byte, so this result is recorded as an evidence-preservation trade-off rather than treated as a source mutation or a substitute for the repository’s own passing formatter check. [25]

## Remediation verification

The eight requested prior findings were rechecked independently. The table separates the narrow prior finding from the broader safety and documentation results found during this re-review.

| Prior finding to verify | Independent result | Evidence |
|---|---|---|
| 1. The documented generated-repository workflow initializes Git before Git-dependent commands | **Remediated in the canonical runbook.** The runbook lists `git init` before `uv lock` and `bash scripts/bootstrap`; its exact command sequence passed manually. | Runbook; `test_documented_runbook_workflow.py`; manual documented workflow [10] [19] |
| 2. Clean-room tests follow the documented operator workflow | **Remediated.** The shared workflow defines the same ordered command sequence, and a test asserts runbook equality. | `workflow.py`; focused test; clean-room test [18] [19] [20] |
| 3. Generator does not silently delete a non-empty target | **Remediated for the default path.** Generation without `--overwrite` failed on a sentinel-bearing target and preserved the sentinel. | Generator logic; focused test; manual safety scenario [17] [26] |
| 4. Explicit overwrite behavior is guarded and tested | **Partially remediated.** `--overwrite` is required and the ordinary target test passes, but H-01 below demonstrates the guard permits destructive self-overwrite of the harness checkout. | CLI and generator logic; focused test; sacrificial-copy probe [17] [18] [26] |
| 5. Generated repositories provide a working `make secrets-baseline` command | **Remediated.** The generated script exists and `make secrets-baseline` passed in the independently created documented-workflow repository. | Generated script and Makefile; focused test; manual workflow [20] [21] |
| 6. Residual-reference validation scans `harness/` | **Remediated.** `harness/` is included in configured scan roots and the focused suite passed. | Configuration and residual-reference suite [9] [27] |
| 7. A test proves an injected Continuum reference in `harness/` is detected | **Remediated.** The focused suite contains and passed the injected-probe test. | `test_residual_references.py` [27] |
| 8. Plan and dossier accurately record the blocked candidate, result, remediation state, and new candidate | **Not remediated completely.** Both documents record the old candidate and prior `BLOCK`, but neither identifies `b5d62179864fed7a68e2210e396e83d9835ee464` as the remediation candidate. | Active plan and validation dossier [7] [8] |

## Commands executed

All commands below were run independently. Command logs, including full standard output and error output, are preserved beside this report. A zero exit status is reported only where the observed command exited zero.

| Context | Exact command | Actual result |
|---|---|---|
| Candidate root | `bash scripts/bootstrap` | Exit `0`; Ruff format check and lint passed; `55 passed in 10.86s`; detect-secrets passed. |
| Candidate root | `bash scripts/test` | Exit `0`; `55 passed in 5.57s`. |
| Candidate root | `bash scripts/secrets-check` | Exit `0`; detect-secrets passed. |
| Candidate root | `bash scripts/check` | Exit `0`; Ruff checks passed; `55 passed in 5.53s`; detect-secrets passed. |
| Lock consistency | `uv lock --check` | Exit `0`; resolved 24 packages. |
| Architecture | `uv run pytest -q tests/architecture/test_package_boundaries.py` | Exit `0`; `10 passed in 0.03s`. |
| Traceability | `uv run pytest -q tests/test_traceability.py` | Exit `0`; `31 passed in 0.16s`. |
| Residual references | `uv run pytest -q tests/test_residual_references.py` | Exit `0`; `3 passed in 0.06s`. |
| Template generation | `uv run pytest -q tests/test_template_generation.py` | Exit `0`; `2 passed in 0.14s`. |
| Clean-room generation | `uv run pytest -q tests/test_clean_room_generation.py` | Exit `0`; `1 passed in 2.18s`. |
| Generated secrets baseline | `uv run pytest -q tests/test_generated_secrets_baseline.py` | Exit `0`; `1 passed in 2.46s`. |
| Destructive-target safety | `uv run pytest -q tests/test_generator_target_safety.py` | Exit `0`; `5 passed in 0.19s`. |
| Documented runbook workflow | `uv run pytest -q tests/test_documented_runbook_workflow.py` | Exit `0`; `2 passed in 0.42s`. |

The independently reproduced mandatory scenarios were run outside the candidate checkout in `/home/ubuntu/independent-review-safety-b5d621-yJPWe6`:

| Scenario | Actual result |
|---|---|
| Generate into a missing target | Exit `0`; generated `README.md` exists. |
| Generate into an empty target | Exit `0`; generated `README.md` exists. |
| Non-empty target without explicit overwrite | Exit `1`; the sentinel file remained present with unchanged content. |
| Explicit overwrite of the disposable target | Exit `0`; the sentinel was removed and generated `README.md` exists. |
| Setup exactly as the canonical runbook documents | Generation, `git init`, `uv lock`, bootstrap, test, secret scan, full check, and `make secrets-baseline` all exited `0`. |

Two additional read-only review probes exposed issues not covered by the required happy-path scenarios. First, the generated README’s advertised `bash scripts/bootstrap` quick start exited `2` before Git initialization because no `uv.lock` was present: `Unable to find lockfile at uv.lock, but --locked was provided.` Second, a sacrificial exact-candidate copy accepted `bash scripts/generate-project --overwrite . destructive-probe "Destructive Probe"` with exit `0`; it removed a sentinel and the copy’s `.git` directory. The original detached candidate checkout was not used for this destructive probe.

## Findings

### Blocker

No separate **Blocker** finding is assigned. The high-severity data-loss defect below is nevertheless sufficient to prevent approval because it violates the expected safety boundary of the canonical generator.

### High

**H-01 — `--overwrite` can destroy the harness checkout itself when the target resolves to the generator’s current repository.**

The shell entry point changes to the harness root, resolves the supplied target, and passes it to `generate_project`. When the target is non-empty and `--overwrite` is set, `generate_project` calls `shutil.rmtree(target_dir)` without rejecting the harness root, an ancestor, or another unsafe overlap. [17] [18]

In a sacrificial clone pinned to the exact candidate, `bash scripts/generate-project --overwrite . destructive-probe "Destructive Probe"` exited `0`. The command removed a sentinel created in the harness root and deleted the clone’s `.git` directory. This was not merely a theoretical code path. Although the ordinary non-empty-target safety test proves that an explicit flag is needed, it does not test or prevent self-overwrite. [26]

This creates a material local data-loss and rollback risk: a path typo such as `.` can replace the tool’s own source repository with template output, destroying repository metadata and user work. The explicit flag is not a sufficient guard for a source-overlap target.

### Medium

**M-01 — A freshly generated repository’s own advertised quick start is not executable as written.**

The generated README advertises only `bash scripts/bootstrap` as “Quick start,” and the generated AGENTS file lists bootstrap as the command to install locked dependencies and Git hooks. Neither document states that the generated directory has no lockfile or Git repository and requires `git init` followed by `uv lock` first. [20] [21]

The independently generated README-quick-start target had no `.git` directory. Running the advertised bootstrap command exited `2` at `uv sync --locked` because `uv.lock` did not yet exist. Even if an operator creates the lockfile, the generated bootstrap later invokes `pre-commit install`, which requires a Git working tree. The canonical harness-side checklist is correct; the generated repository’s standalone guidance is not. [10] [22]

This does not negate the successful canonical runbook exercise, but it contradicts the generated output’s own operator-facing “Quick start” and weakens the claim that generated repositories are independently coherent.

**M-02 — The Issue #1 plan and validation dossier omit the exact remediation candidate required for accurate traceability.**

The candidate’s active plan and validation dossier record `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` as the reviewed candidate, correctly record the prior `BLOCK`, and say remediation is in progress. Neither record names `b5d62179864fed7a68e2210e396e83d9835ee464` as the remediation candidate, despite this candidate being the exact SHA whose validation and CI are now under review. [7] [8]

This leaves the required reviewer-facing chain from prior blocked candidate to remediation candidate incomplete and is not caught by the present traceability test suite. It directly leaves the eighth requested remediation item incomplete.

### Low

No **Low** finding is assigned.

### Observation

**O-01 — The successful exact-SHA CI run carries an action-runtime deprecation warning.** GitHub Actions run `30214792101` was successful, but GitHub displayed a warning that the pinned checkout, Python setup, and uv setup actions target deprecated Node.js 20 and were forced to run on Node.js 24. This warning does not change the successful run conclusion, but it limits confidence that the current action-runtime behavior will remain stable indefinitely. [15]

**O-02 — Standard `git diff --check` reports trailing whitespace in the preserved prior review.** The candidate deliberately excludes the preserved Issue #1 reports from whitespace and EOF normalization to preserve them byte-for-byte. This is consistent with the preservation intent, but it means a generic diff-hygiene command is not clean for this change set. [25]

**O-03 — The secret baseline adds two unverified report-associated detections.** The candidate baseline records two `is_verified: false` entries associated with the newly preserved Issue #1 reports. The independently executed secret scan passed, and this review does not identify a real secret; however, the reviewed Issue #1 evidence documents do not provide an explicit audit classification for those added baseline entries. This is an evidence-quality observation, not a conclusion that a secret was committed. [8] [24]

## Acceptance-criteria assessment

| # | Issue #1 acceptance criterion | Assessment | Independent evidence and rationale |
|---:|---|---|---|
| 1 | Project-specific values are configurable or clearly documented | **Pass** | `harness-config.toml` centralizes project metadata, package layout, provenance, and scan policy. [9] |
| 2 | Remaining Continuum references are intentional provenance or examples | **Pass** | The configured residual-reference scan includes `harness/`; all focused residual-reference tests, including the injected-harness probe, passed. [9] [27] |
| 3 | No machine-specific local paths remain in operational templates | **Pass** | The residual policy checks `/Users/`; template-generation and clean-room tests passed. [18] [27] |
| 4 | A documented process can create a clean new product repository | **Partially met** | The canonical harness runbook is correct and passed independently, but the generated repository’s own advertised quick start fails. See M-01. [10] [20] |
| 5 | A disposable generated repository passes all documented validation commands | **Pass for the canonical runbook** | The independent documented workflow passed generation, Git initialization, lock creation, bootstrap, test, secret scan, full check, and `make secrets-baseline`. |
| 6 | Generated repositories do not misrepresent Continuum evidence as their own | **Pass** | Generated lineage states that it records harness provenance only; clean-room provenance and residual checks passed. [11] [20] |
| 7 | CI passes on the exact implementation commit | **Pass** | Run `30214792101` is completed/success with exact `head_sha` equal to the candidate. [15] |
| 8 | Independent review uses an isolated clone pinned to an exact 40-character SHA | **Pass** | This report records the fresh detached clone, exact SHA, clean status, and absence of untracked files. |
| 9 | Independent-review evidence is preserved byte-for-byte | **Pass for this new reviewer deliverable** | This report is finalized without later modification and is accompanied by an external SHA-256 sidecar generated after finalization. |
| 10 | Final PR-head CI is green | **Pass** | Live PR metadata and `git ls-remote` identify the candidate as the current PR head; a completed-success `pull_request` run `30214793422` is tied to that exact SHA. [2] [16] |
| 11 | Post-review commits receive a narrow delta review when applicable | **Pass at the reviewed head** | The prior candidate-to-remediation delta was reviewed; the live PR head is the candidate. No later commit was identified. |
| 12 | Product-owner approval is required before merge | **Guardrail intact; merge pending** | PR #2 is open, draft, and unmerged. [2] |
| 13 | Auto-merge remains disabled | **Pass at review time** | Live PR metadata reports `auto_merge: null`. [16] |
| 14 | Template-repository mode is enabled only after validated merge | **Pass at review time** | Live repository metadata reports `is_template: false`; the PR remains unmerged. [16] |

## CI evidence review

The requested live Actions run was independently verified through the GitHub run page and raw GitHub API metadata. The raw metadata reports `head_sha` exactly equal to the candidate, `head_branch` equal to `foundation/extract-project-harness`, `event` equal to `push`, `status` equal to `completed`, and `conclusion` equal to `success`. [15]

| Run ID | Event | Exact head SHA check | Status / conclusion | Review use |
|---:|---|---|---|---|
| `30214792101` | `push` | `b5d62179864fed7a68e2210e396e83d9835ee464` — exact match | completed / success | Required candidate CI evidence |
| `30214793422` | `pull_request` | `b5d62179864fed7a68e2210e396e83d9835ee464` — exact match | completed / success | Supports final PR-head CI criterion |

The workflow runs `uv sync --locked` followed by `bash scripts/check`, and the candidate’s live CI evidence therefore supports locked dependency consistency, formatting, linting, the full test suite, and secret scanning. The public view did not permit job-log inspection, so this report relies on GitHub’s visible and API-provided status/conclusion/head-SHA metadata together with the independently rerun local commands. [23] [15]

## Limitations

This review was intentionally confined to Issue #1 and the exact candidate SHA. It does not review a future commit, a future PR-head change, a merge, deployment, infrastructure, or repository settings beyond the read-only governance metadata used to confirm the safety gates.

GitHub’s public Actions UI required sign-in for detailed job logs. Accordingly, no claim is made about individual CI log lines beyond the repository workflow, the raw run metadata, visible status, conclusion, and independently rerun local checks. A browser Markdown extraction initially mis-associated the base SHA with the PR head; the raw GitHub REST response and live `git ls-remote` result were used to correct that presentation error before assessment.

The mandatory and additional destructive exercises ran only in dedicated scratch directories and a sacrificial clone outside the reviewed checkout. The required bootstrap command installed a Git hook and created ignored local tooling artifacts in the isolated clone, but final Git status and untracked-file checks remained clean. No repository source file was altered.

## Final recommendation

**BLOCK**

Approval is not supported for `b5d62179864fed7a68e2210e396e83d9835ee464`. The candidate remediates the prior canonical-runbook, ordinary-target safety, generated-secret-baseline, and residual-reference gaps, and the exact-SHA local and GitHub CI evidence is green. However, the canonical `--overwrite` command can still replace the harness repository itself when given `.` as its target, deleting both user content and Git metadata in a demonstrated exact-candidate execution. That is a material data-loss and rollback defect in a repository-generation tool. The generated repository’s own quick-start documentation is also non-executable as written, and the Issue #1 evidence documents omit the new remediation candidate SHA.

A new remediation candidate and a new exact-SHA independent review are required. No implementation, source modification, commit, push, merge, deployment, auto-merge action, or template activation was performed during this review.

## References

[1]: https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1 "GitHub Issue #1 — Extract reusable project harness from Continuum H0"
[2]: https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2 "GitHub Pull Request #2"
[3]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/b5d62179864fed7a68e2210e396e83d9835ee464 "Exact remediation candidate"
[4]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/7c8e04e1e864ee70bd18ffdad29d6517aecde1f7 "Imported H0 baseline"
[5]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/d10a3c22b814a853e0975a8bc9034ce4575ce4ff "Previously blocked candidate"
[6]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/AGENTS.md "AGENTS.md at exact candidate"
[7]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/exec-plans/active/issue-1-project-harness-extraction.md "Issue #1 active execution plan at exact candidate"
[8]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/validation/issue-1-project-harness-extraction.md "Issue #1 validation dossier at exact candidate"
[9]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/harness-config.toml "Harness configuration at exact candidate"
[10]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/runbooks/new-repository-checklist.md "New repository checklist at exact candidate"
[11]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/design-docs/harness-generated-boundary.md "Harness and generated-repository boundary"
[12]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/decisions/adr-0002-project-harness-extraction.md "ADR-0002 project-harness extraction"
[13]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/docs/decisions/adr-0001-h0-repository-bootstrap.md "ADR-0001 H0 repository bootstrap"
[14]: https://github.com/maxaihappy/project-harness-bootstrap-kit/tree/b5d62179864fed7a68e2210e396e83d9835ee464/docs/validation/reviews "Preserved review reports at exact candidate"
[15]: https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30214792101 "GitHub Actions run 30214792101"
[16]: https://api.github.com/repos/maxaihappy/project-harness-bootstrap-kit/pulls/2 "Live GitHub API metadata for PR #2"
[17]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/harness/generator/render.py "Generator implementation at exact candidate"
[18]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/scripts/generate-project "Generator CLI at exact candidate"
[19]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/harness/generator/workflow.py "Canonical generated-repository workflow"
[20]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/templates/product-repo/README.md "Generated README template"
[21]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/templates/product-repo/AGENTS.md "Generated AGENTS template"
[22]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/templates/product-repo/scripts/bootstrap "Generated bootstrap script"
[23]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/.github/workflows/ci.yml "CI workflow at exact candidate"
[24]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/.secrets.baseline "Detect-secrets baseline at exact candidate"
[25]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/.pre-commit-config.yaml "Pre-commit configuration at exact candidate"
[26]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/tests/test_generator_target_safety.py "Generator target-safety tests"
[27]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/b5d62179864fed7a68e2210e396e83d9835ee464/tests/test_residual_references.py "Residual-reference tests"
