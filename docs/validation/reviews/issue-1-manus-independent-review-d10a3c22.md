# Independent Review Report

**Review date:** 2026-07-26 PDT  
**Reviewer role:** Independent reviewer; review-only  
**Recommendation:** **BLOCK**

## Review target

This review evaluates only the exact implementation candidate `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` in `maxaihappy/project-harness-bootstrap-kit`, measured against GitHub Issue #1 and the imported H0 baseline `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7`. The reviewed diff boundary is exactly `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7..d10a3c22b814a853e0975a8bc9034ce4575ce4ff`.[1] [2] [3]

| Parameter | Value |
|---|---|
| Repository | `https://github.com/maxaihappy/project-harness-bootstrap-kit` |
| Requirement authority | GitHub Issue #1 — *Extract reusable project harness from Continuum H0* [1] |
| Pull-request provenance | GitHub PR #2 — draft, `main` ← `foundation/extract-project-harness` [2] |
| Imported H0 baseline | `7c8e04e1e864ee70bd18ffdad29d6517aecde1f7` [3] |
| Sole implementation candidate | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` [4] |
| Review boundary | Exact two-SHA diff only; no moving branch tip substituted |
| Excluded later PR commit | `e1090d9eeb2f9373ac26e0198a6c531429757f81`, described on PR #2 as evidence-only; it was not inspected as implementation source [2] |

The review made no source edit, commit, push, merge, deployment, infrastructure change, auto-merge change, or template-mode change. The prior BLOCK artifact was neither opened for revision nor overwritten. This report is a new, separately named deliverable.

## Isolation and checkout verification

A new isolated clone was created at `/home/ubuntu/reviews/issue-1-independent-d10a3c22b814a853e0975a8bc9034ce4575ce4ff`. The repository was cloned with `git clone --no-checkout --no-tags`, the exact baseline and candidate objects were fetched by SHA, and the candidate was checked out with `git checkout --detach d10a3c22b814a853e0975a8bc9034ce4575ce4ff`.

| Required verification | Exact observed result |
|---|---|
| Clone path | `/home/ubuntu/reviews/issue-1-independent-d10a3c22b814a853e0975a8bc9034ce4575ce4ff` |
| `git remote get-url origin` | `https://github.com/maxaihappy/project-harness-bootstrap-kit.git` |
| `git rev-parse HEAD` | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` |
| Detached state | `git symbolic-ref -q HEAD` produced no output and exited `1`, confirming detached `HEAD` |
| `git status --short` before review | No output |
| `git ls-files --others --exclude-standard` before review | No output; no untracked files existed |
| Baseline relationship | `git merge-base --is-ancestor 7c8e04… d10a3c…` exited `0` |
| `git status --short` after validation | No output |
| Untracked files after validation | None |

Before substantive review, public access to Issue #1, PR #2, and `AGENTS.md` was confirmed. `AGENTS.md` was the first repository-content document read. It directs the reviewer to the configuration, architecture policy, active plan, validation dossier, ADRs, and authoritative scripts.[5]

## Materials reviewed

The review relied exclusively on the detached repository candidate and GitHub evidence. Historical H0 material was treated as provenance only, consistent with the repository’s own authority rules; it was not treated as validation for Issue #1.[5] [6] [7]

| Material | Review purpose |
|---|---|
| Issue #1 and PR #2 | Scope, acceptance criteria, branch/commit provenance, and governance controls [1] [2] |
| `AGENTS.md`, `harness-config.toml`, `ARCHITECTURE.md`, `architecture-boundaries.toml` | Governing navigation, configuration separation, architecture policy, and residual-reference scope [5] [8] [9] |
| Active Issue #1 execution plan and validation dossier | Required command contract, candidate evidence state, rollback, and closeout boundaries [6] [7] |
| ADR-0001 and ADR-0002 | Imported-H0 provenance and the approved harness-extraction design [10] [11] |
| `scripts/`, `.github/workflows/ci.yml`, `pyproject.toml`, `uv.lock` | Authoritative validation, CI trigger/permissions, and locked dependency surface [12] [13] [14] |
| `.secrets.baseline` and `.pre-commit-config.yaml` | Secret-detection controls and preserved-review exclusions [15] [16] |
| Generator, reference policy, template tree, and associated tests | Generated-project behavior, provenance boundary, residual-reference detection, and test coverage [17] [18] [19] [20] |
| Live Actions run metadata | Exact-SHA CI status for runs `30191530863` and `30191532008` [21] [22] |
| Live PR/repository metadata | Draft/unmerged/auto-merge state and `is_template` setting [23] [24] |

## Diff summary

`git diff --check 7c8e04e1e864ee70bd18ffdad29d6517aecde1f7 d10a3c22b814a853e0975a8bc9034ce4575ce4ff` exited `0`; no whitespace errors were reported. The exact diff contains **60 changed files**, **1,932 insertions**, and **102 deletions**. It includes the new harness configuration, neutral domain placeholders, generator and reference policy, product-repository templates, generation and clean-room tests, Issue #1 documentation/ADR, and CI trigger expansion.

The implementation substantially advances the intended product-neutral design. The generated output excludes the named harness-only paths, contains no residual `Continuum`, `/Users/`, `bootstrap/h0`, or unresolved `{{…}}` markers in the reviewer’s manual clean-room scan, and keeps the generated lineage document limited to harness provenance rather than H0 validation claims.[11] [17] [18]

However, the review found that the nominal clean-room design succeeds only after an **undocumented `git init` precondition**, and that the generator silently deletes a pre-existing target directory. Those behaviors directly affect the documented generation, safety, and rollback claims.

## Commands executed

All commands below were run independently from the detached candidate checkout unless a generated-repository target is explicitly named. The source checkout remained clean and at the exact candidate SHA afterward.

| Context | Exact command | Actual result |
|---|---|---|
| Exact diff | `git diff --check 7c8e04e1e864ee70bd18ffdad29d6517aecde1f7 d10a3c22b814a853e0975a8bc9034ce4575ce4ff` | Exit `0`; no output. |
| Candidate root | `bash scripts/bootstrap` | Exit `0`; `45 passed in 8.38s`; Detect secrets passed. |
| Candidate root | `bash scripts/test` | Exit `0`; `45 passed in 2.54s`. |
| Candidate root | `bash scripts/secrets-check` | Exit `0`; Detect secrets passed. |
| Candidate root | `bash scripts/check` | Exit `0`; format and lint passed; `45 passed in 2.29s`; Detect secrets passed. |
| Architecture | `uv run pytest -q tests/architecture/test_package_boundaries.py` | Exit `0`; `10 passed in 0.03s`. |
| Traceability | `uv run pytest -q tests/test_traceability.py` | Exit `0`; `31 passed in 0.11s`. |
| Residual references | `uv run pytest -q tests/test_residual_references.py` | Exit `0`; `1 passed in 0.01s`. |
| Template generation | `uv run pytest -q tests/test_template_generation.py` | Exit `0`; `2 passed in 0.09s`. |
| Clean-room test | `uv run pytest -q tests/test_clean_room_generation.py` | Exit `0`; `1 passed in 2.12s`. |

For independent manual clean-room evidence, a new disposable target was generated outside the source checkout with:

```bash
bash scripts/generate-project /home/ubuntu/review-scratch/issue-1-d10a3c22b814a853e0975a8bc9034ce4575ce4ff/manual-clean-room-product manual-clean-room-product "Manual Clean Room Product"
```

Generation exited `0` and reported six substitutions. After an explicit **undocumented** `git init`, `uv lock`, `bash scripts/bootstrap`, `bash scripts/test`, `bash scripts/secrets-check`, and `bash scripts/check` each exited `0`. The generated repository’s tests reported `3 passed`; the generated secret scan returned success but displayed `Skipped` because no files were yet tracked in that newly initialized Git repository.

The following reviewer checks exposed failures that the passing suite did not cover:

| Scenario | Commands / condition | Actual result |
|---|---|---|
| Exact runbook sequence, no Git repository | `generate-project`; `uv lock`; `bash scripts/bootstrap` | Generation `0`; lock `0`; bootstrap `1` with `FatalError: git failed. Is it installed, and are you in a Git repository directory?` |
| Exact runbook sequence, no Git repository | `bash scripts/test`; `bash scripts/secrets-check`; `bash scripts/check` | Test `0` (`3 passed`); secret scan `1`; full check `1`, both due to the same Git/pre-commit fatal error. |
| Advertised generated secret-baseline target | `make secrets-baseline` in Git-initialized generated repository | Exit `2`; `bash: scripts/secrets-baseline: No such file or directory`. |
| Existing-target safety | Generate into a scratch directory containing a nested sentinel file | Generator exited `0`; sentinel was **removed**. No source-checkout file was touched. |

## Findings

### Blocker

**B-01 — The documented procedure for creating and validating a generated repository fails before it can complete the required validation contract.**

The authoritative new-repository checklist instructs an operator to generate a target, enter it, run `uv lock`, and then run `bash scripts/bootstrap`. Only later does the checklist say to initialize a new Git repository.[25] The generated `bootstrap` script delegates to `uv run pre-commit install`, which requires a Git working tree.[12] The reviewer reproduced the documented sequence in a fresh non-Git target: generation and `uv lock` succeeded, while `bash scripts/bootstrap` exited `1`; `bash scripts/secrets-check` and `bash scripts/check` also exited `1` because `pre-commit` returned `FatalError: git failed. Is it installed, and are you in a Git repository directory?`.

> The clean-room test masks this mismatch by running `git init` **before** `uv lock` and the four validation commands.[20]

This is a direct failure of the required documented clean-new-repository workflow and of the claim that a disposable generated repository passes the documented validation commands. It also explains why the local suite and exact-SHA CI can pass while the operator-facing workflow fails. The issue affects acceptance criteria 4 and 5 and prevents approval.

### High

**H-01 — The authoritative generator silently and recursively deletes an existing target directory by default.**

`generate_project` deletes any existing `target_dir` through `shutil.rmtree(target_dir)` when its default `clean=True` is in effect.[17] The public shell entry point exposes no confirmation, `--force`, or non-destructive default; it directly calls that function with its default behavior.[18] Although the checklist says a target may be “overwritten intentionally,” it provides no command-level guard that distinguishes an intentional overwrite from a path mistake.[25]

The reviewer safely reproduced the behavior only in a disposable scratch directory: an existing nested sentinel file was removed and the generation command exited `0`. The same control flow can delete an arbitrary pre-existing path supplied to the canonical generator. This is a material safety and rollback defect in a tool whose stated job is to create repositories.

### Medium

**M-01 — Every generated repository advertises a broken `secrets-baseline` command.**

The generated template’s Makefile declares `secrets-baseline` and delegates it to `bash scripts/secrets-baseline`, but the template contains no such script.[26] In a Git-initialized generated clean-room repository, `make secrets-baseline` exited `2` with `bash: scripts/secrets-baseline: No such file or directory`.

The root harness does contain a `scripts/secrets-baseline` path, but the generator does not copy it. This leaves generated repositories without the advertised controlled path for maintaining the detect-secrets baseline, weakening the portability of the secret-scanning control.

**M-02 — The residual-reference test does not scan the new `harness/` implementation it claims to protect.**

The configuration’s `scan_roots` include scripts, CI, packages, docs, and top-level policy files, but omit `harness/`.[8] The residual-reference test simply invokes the configured roots.[19] Consequently, a future unintended Continuum reference introduced into the generator or other harness implementation code would not be detected by this test, despite the test name asserting it checks the harness. The current candidate’s manual scan found no active product coupling in generated output; this is a coverage/evidence-boundary gap rather than a demonstrated present-day generated-output leak.

### Low

**L-01 — The exact candidate’s Issue #1 status records are internally stale and do not identify the implementation candidate.**

The active plan calls itself the active plan for Issue #1 while stating that implementation “has not started” and listing the implementation candidate as pending, even though later portions of that same file state implementation and local validation are completed.[6] The validation dossier similarly sets `reviewed_implementation_candidate: not-yet-identified` and says the candidate will be recorded after the implementation commit lands.[7]

The independently reviewed candidate commit exists and the two requested CI runs are attributable to it. The repository’s stale status text therefore reduces documentation accuracy and exact-SHA provenance within the candidate. This finding is low severity because closeout evidence was expressly pending; it remains material to a review process that relies on artifacts as records of fact.

### Observation

Both exact-candidate CI runs completed successfully, but GitHub displayed an annotation that the pinned actions target deprecated Node.js 20 and were forced to run on Node.js 24.[21] [22] This did not fail the runs and is not a basis for the recommendation, but it is recorded because it limits the permanence of the current CI environment assumptions.

## Acceptance-criteria assessment

| # | Acceptance criterion | Assessment | Evidence and rationale |
|---:|---|---|---|
| 1 | Project-specific values are configurable or clearly documented | **Pass** | `harness-config.toml` centralizes harness metadata, provenance, layout, and residual-reference policy; runbooks document its role.[8] [27] |
| 2 | Remaining Continuum references are intentional provenance or examples | **Partially met** | Manual generated-output scan found none, and documented provenance boundaries are clear. However, the residual-reference test omits `harness/`, leaving an operational-code coverage gap. [8] [17] [19] |
| 3 | No machine-specific local paths remain in operational templates | **Pass** | Manual generated-output scan found no `/Users/` references; the template output contained no inherited H0 artifacts or unresolved placeholders. [17] [18] |
| 4 | A documented process can create a clean new product repository | **Fail** | The documented sequence fails at generated `bash scripts/bootstrap` because it omits the required prior Git initialization. See B-01. [25] [12] |
| 5 | A disposable generated repository passes all documented validation commands | **Fail** | It passes only after the test’s undocumented `git init`; under the documented sequence, bootstrap, secret scan, and full check fail. See B-01. [20] [25] |
| 6 | Generated repositories do not misrepresent Continuum evidence as their own | **Pass** | Generated lineage explicitly disclaims H0 validation ownership; manual scan confirmed harness-only provenance files are absent. [28] [17] |
| 7 | CI passes on the exact implementation commit | **Pass** | Both specified completed-success CI runs have the exact candidate `head_sha`. [21] [22] |
| 8 | Independent review uses an isolated clone pinned to an exact 40-character SHA | **Pass** | This review used the new detached clone and exact `HEAD` documented above. |
| 9 | Independent-review evidence is preserved byte-for-byte | **Pass for this reviewer deliverable** | This new Markdown report is finalized without later edits and has a separately recorded SHA-256 sidecar; the reviewer did not alter repository evidence. |
| 10 | Final PR-head CI is green | **Pending / out of this candidate review’s source scope** | PR #2 has a later evidence-only head commit. Per the review instruction, it was not used as implementation or CI evidence; a later-head/delta check remains distinct work. [2] |
| 11 | Post-review commits receive a narrow delta review when applicable | **Pending** | A later PR commit exists and was intentionally excluded from this exact-candidate review. [2] |
| 12 | Product-owner approval is required before merge | **Guardrail intact; merge pending** | Live PR metadata shows the PR remains draft, open, and unmerged. [23] |
| 13 | Auto-merge remains disabled | **Pass at review time** | Live PR metadata returned `"auto_merge": null`; no reviewer mutation was performed. [23] |
| 14 | Template-repository mode is enabled only after validated merge | **Pass at review time** | Live repository metadata returned `is_template: false`; PR #2 remains unmerged. [23] [24] |

## CI evidence review

| Run ID | Event | Status / conclusion | Exact `head_sha` check | Result |
|---:|---|---|---|---|
| [30191530863](https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30191530863) | `push` | `completed` / `success` | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` — exact match | Supports candidate-root validation only. [21] |
| [30191532008](https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30191532008) | `pull_request` | `completed` / `success` | `d10a3c22b814a853e0975a8bc9034ce4575ce4ff` — exact match | Supports candidate-root validation only. [22] |

The live run pages show a single `validate` job in each case and the repository workflow delegates CI validation to `bash scripts/check` after `uv sync --locked`.[13] The public signed-out view did not permit job-log inspection. More importantly, successful candidate-root CI does not demonstrate the operator workflow in the new-repository checklist: CI does not create a repository through that runbook sequence, and the clean-room test inserts `git init` before testing. Therefore, the green CI evidence is valid but insufficient to overcome B-01.

## Limitations

This review deliberately did not inspect source, diff, or tests from the later PR-head evidence commit. Accordingly, it does not provide the required narrow delta review for that later commit and does not make a claim about final PR-head CI. The review also did not use any user-local workspace, did not access implementation-chat context, and did not make GitHub state changes.

The live GitHub Actions pages were accessible for run metadata and job status, but their detailed logs required sign-in. The report therefore relies on publicly visible status/conclusion/head-SHA metadata together with independently executed local validation. All safety experiments that created, initialized, overwrote, or validated generated repositories ran solely in dedicated sandbox scratch directories outside the detached source checkout.

The earlier prior BLOCK report remains outside this review artifact and was not changed. The evidence preservation claim for this review applies to the attached Markdown report and its separately generated SHA-256 sidecar; it is not an in-repository commit because the reviewer was explicitly constrained not to modify the source repository.

## Final recommendation

**BLOCK**

Approval is not supported for `d10a3c22b814a853e0975a8bc9034ce4575ce4ff`. The required operator-facing clean-room workflow fails when executed as documented, so the candidate does not meet the Issue #1 generation and validation acceptance criteria. Separately, the canonical generator silently deletes an existing target, creating a material data-loss risk. The root suite, focused tests, two exact-SHA CI runs, and generated output scan all pass, but they do not test the documented no-Git creation path or the destructive overwrite behavior. A new candidate and a new exact-SHA review would be required after remediation; no remediation was performed in this review.

## References

[1]: https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1 "GitHub Issue #1 — Extract reusable project harness from Continuum H0"
[2]: https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2 "GitHub PR #2 — Extract reusable project harness bootstrap kit"
[3]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/7c8e04e1e864ee70bd18ffdad29d6517aecde1f7 "Imported H0 baseline commit"
[4]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/d10a3c22b814a853e0975a8bc9034ce4575ce4ff "Exact implementation candidate"
[5]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/AGENTS.md "AGENTS.md at exact candidate"
[6]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/exec-plans/active/issue-1-project-harness-extraction.md "Issue #1 active execution plan at exact candidate"
[7]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/validation/issue-1-project-harness-extraction.md "Issue #1 validation dossier at exact candidate"
[8]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/harness-config.toml "Harness configuration at exact candidate"
[9]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/ARCHITECTURE.md "Architecture policy at exact candidate"
[10]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/decisions/adr-0001-h0-repository-bootstrap.md "ADR-0001 H0 bootstrap"
[11]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/decisions/adr-0002-project-harness-extraction.md "ADR-0002 harness extraction"
[12]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/scripts/bootstrap "Authoritative bootstrap script"
[13]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/.github/workflows/ci.yml "CI workflow at exact candidate"
[14]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/pyproject.toml "Dependency manifest at exact candidate"
[15]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/.secrets.baseline "Detect-secrets baseline at exact candidate"
[16]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/.pre-commit-config.yaml "Pre-commit configuration at exact candidate"
[17]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/harness/generator/render.py "Generator implementation at exact candidate"
[18]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/scripts/generate-project "Authoritative generator entry point"
[19]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/tests/test_residual_references.py "Residual-reference test at exact candidate"
[20]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/tests/test_clean_room_generation.py "Clean-room generation test at exact candidate"
[21]: https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30191530863 "GitHub Actions run 30191530863"
[22]: https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30191532008 "GitHub Actions run 30191532008"
[23]: https://api.github.com/repos/maxaihappy/project-harness-bootstrap-kit/pulls/2 "Live GitHub API metadata for PR #2"
[24]: https://api.github.com/repos/maxaihappy/project-harness-bootstrap-kit "Live GitHub API repository metadata"
[25]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/runbooks/new-repository-checklist.md "New repository checklist at exact candidate"
[26]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/templates/product-repo/Makefile "Generated-repository Makefile template at exact candidate"
[27]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/docs/runbooks/initialize-harness.md "Harness initialization runbook at exact candidate"
[28]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/d10a3c22b814a853e0975a8bc9034ce4575ce4ff/templates/product-repo/docs/lineage.md "Generated-repository lineage template at exact candidate"
