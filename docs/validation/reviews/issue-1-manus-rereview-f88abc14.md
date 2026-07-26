# Independent Review Report — Issue #1

**Review date:** 2026-07-26 PDT  
**Reviewer role:** Independent reviewer; review-only  
**Exact candidate reviewed:** `f88abc14fed9b784db6e9481afa22975868718a8`  
**Final recommendation:** **BLOCK**

> **Decision:** The fixed candidate resolves the prior self-overwrite and generated quick-start defects, and its local and GitHub Actions validation is green. Approval is nevertheless not supported because GitHub reports that `main` has no enabled branch protection, so the stated prohibition on direct pushes and requirement for product-owner approval are not technically enforced. In addition, a newly generated repository’s documented first-run secret check succeeds without scanning any untracked files, including a deliberately injected pattern-only fake GitHub token.

## 1. Review boundary and checkout gate

This was a read-only review of **only** commit `f88abc14fed9b784db6e9481afa22975868718a8` for GitHub Issue #1. The review used the isolated fixed-SHA checkout plus read-only GitHub evidence. No repository source file was edited, no commit was created, and no push, merge, deployment, infrastructure action, auto-merge action, or template-mode action was performed. The review began with the committed `AGENTS.md`, as required.[1]

| Required checkout fact | Actual result |
|---|---|
| Fresh isolated clone path | `/home/ubuntu/reviews/project-harness-bootstrap-kit-f88abc14-20260726T195544641119643` |
| Origin URL | `https://github.com/maxaihappy/project-harness-bootstrap-kit` |
| Exact `HEAD` | `f88abc14fed9b784db6e9481afa22975868718a8` |
| Checkout state | Detached `HEAD` |
| Initial `git status --short` | No output |
| Initial untracked-file check | `git ls-files --others --exclude-standard` produced no output |
| Final checkout integrity | Exact `HEAD` unchanged; status, untracked-file, staged-diff, and unstaged-diff checks all clean |

The live Issue #1 is open and defines the required validation commands, exact-SHA review, green final PR-head CI, product-owner approval before merge, disabled auto-merge, and delayed template activation.[2] Its owner comment authorizes the Issue #1 scope but expressly does **not** authorize merge, deployment, infrastructure creation, template activation, or auto-merge.[3]

## 2. GitHub and narrow-delta evidence

GitHub reports that PR #2 is open and draft, with `main` as base and `foundation/extract-project-harness` as head. At the final refresh, its head was exactly the reviewed SHA, it was unmerged, and `auto_merge` was `null`; the repository was not in template mode.[4] [5]

| Evidence item | Actual result |
|---|---|
| Candidate parent | `b5d62179864fed7a68e2210e396e83d9835ee464` |
| Baseline ancestry | The imported H0 baseline and prior blocked candidate are ancestors of the candidate |
| Narrow delta | 9 files changed, 463 insertions, 23 deletions |
| Candidate CI — PR event | Run `30216115194`, `completed` / `success`, exact head SHA match |
| Candidate CI — push event | Run `30216113536`, `completed` / `success`, exact head SHA match |
| Check runs | Two `validate` jobs, both `completed` / `success` |
| Formal PR reviews | Zero formal review records; consistent with an open draft PR |

The narrow delta contains the expected second-pass remediation areas: overlap rejection in the generator, canonical quick-start commands in generated documentation, focused regression coverage, and current remediation-status documentation.[6] The live PR body remains a planning-era description that says no extraction implementation is included and that independent review has not begun. That statement does not describe the current seven-commit PR head and is recorded as an advisory traceability issue below.[4]

## 3. Validation performed

The following commands were run sequentially from the exact detached checkout. Their full stdout/stderr and exit statuses are preserved in the attached validation log. A passing suite is reported as evidence, not treated as a substitute for the manual safety review.

| Exact command | Actual result |
|---|---|
| `bash scripts/bootstrap` | Exit `0`; locked environment synchronized; format and lint passed; `64 passed in 11.94s`; detect-secrets passed |
| `bash scripts/test` | Exit `0`; `64 passed in 6.42s` |
| `bash scripts/secrets-check` | Exit `0`; detect-secrets passed |
| `bash scripts/check` | Exit `0`; format and lint passed; `64 passed in 6.32s`; detect-secrets passed |
| `uv lock --check` | Exit `0`; resolved 24 packages |
| `uv run pytest -q tests/architecture/test_package_boundaries.py` | Exit `0`; `10 passed` |
| `uv run pytest -q tests/test_traceability.py` | Exit `0`; `31 passed` |
| `uv run pytest -q tests/test_residual_references.py` | Exit `0`; `3 passed` |
| `uv run pytest -q tests/test_template_generation.py` | Exit `0`; `2 passed` |
| `uv run pytest -q tests/test_clean_room_generation.py` | Exit `0`; `1 passed` |
| `uv run pytest -q tests/test_generated_secrets_baseline.py` | Exit `0`; `1 passed` |
| `uv run pytest -q tests/test_generator_target_safety.py` | Exit `0`; `11 passed` |
| `uv run pytest -q tests/test_documented_runbook_workflow.py` | Exit `0`; `5 passed` |

The manifest and lock file are consistent with the documented Python 3.12 tooling contract, and CI executes `uv sync --locked` followed by `bash scripts/check` with read-only repository contents permission and SHA-pinned actions.[7] [8]

## 4. Independent disposable-path reproductions

I ran the following scenarios in a separate scratch area and a sacrificial copy of the exact candidate, never in the reviewed checkout itself. The resulting evidence supports both the fixed generator behavior and the finding below about first-run secret scanning.

| Scenario | Actual result |
|---|---|
| `--overwrite` with target `.` in a sacrificial exact-candidate copy | Exit `1` with `Unsafe generation target`; harness sentinel and `.git` directory remained present |
| Non-empty external target without `--overwrite` | Exit `1`; sentinel remained unchanged |
| External target with explicit `--overwrite` | Exit `0`; sentinel removed and generated `README.md` present |
| Documented workflow (`generate`, `git init`, `uv lock`, bootstrap, test, secrets, check, `make secrets-baseline`) | Every command exited `0`; generated test suite reported `3 passed` |
| Generated-output boundary | All listed harness-only provenance paths were absent; `docs/lineage.md` expressly disclaimed importing or claiming H0 validation evidence |
| Generated `bash scripts/secrets-check` before an initial commit | Exit `0`, but output was `Detect secrets...(no files to check)Skipped` |
| Untracked pattern-only fake GitHub token | Exit `0` and skipped; the generated files and token were all untracked |
| Same fake token after `git add` | Exit `1`; detect-secrets identified `Secret Type: GitHub Token` in the staged probe |

The canonical workflow and generated quick-start now consistently put `git init` and `uv lock` before bootstrap.[9] [10] The generator rejects any source/target overlap before it can delete the target, including the harness root, an ancestor, and a nested path; the candidate regression suite covers these cases.[11] [12]

## 5. Findings

### Critical findings

**None.** No committed secret, deployment behavior, infrastructure action, or destructive behavior in the reviewed checkout was identified.

### High findings

| ID | Finding | Evidence, impact, and required disposition |
|---|---|---|
| **H-01** | **The stated `main`-branch safety gates are not technically enforced by GitHub.** | GitHub’s public `main`-branch metadata reported `protected: false`, `protection.enabled: false`, and required-status-check enforcement `off` at `2026-07-26T20:09:04Z`.[13] The Issue and repository guidance say not to push directly to `main` and require explicit product-owner approval before merge.[1] [2] With no branch protection, a principal with direct write access can bypass the PR, successful CI, and owner-approval workflow. The detailed protection endpoint required administration authorization, so no stronger hidden safeguard can be claimed. This is a material governance and rollback-control gap; approval is not supported until GitHub-level protection enforces the intended pull-request, review, and CI gates. |

### Medium findings

| ID | Finding | Evidence, impact, and required disposition |
|---|---|---|
| **M-01** | **The generated repository’s documented first-run secret check can pass without scanning any generated or newly added untracked files.** | The generated workflow begins with `git init`, `uv lock`, and bootstrap, but it does not create an initial commit or stage files.[9] The generated secret-check script delegates to `pre-commit run detect-secrets --all-files`.[14] In the independent generated-repository reproduction, the command exited `0` with `(no files to check)Skipped`; an untracked, pattern-only fake GitHub token was likewise skipped, while the identical staged probe was correctly rejected. This allows a secret introduced during initial repository setup to evade the required documented security validation. The generated validation design needs a scanning path that actually covers untracked initial files, with a regression test proving that a probe secret fails before the initial commit. |

### Low findings

**None.** No separate low-severity source defect was identified.

### Advisories

| ID | Advisory | Evidence and effect |
|---|---|---|
| **A-01** | **PR #2’s description is stale.** | The live PR body still describes the planning commit, says no extraction implementation is included, and says independent review has not started, while the current head is the reviewed seventh commit.[4] This weakens reviewer-facing traceability but does not outweigh the fixed-SHA, raw GitHub, and repository evidence used in this report. |
| **A-02** | **Generic `git diff --check` is not clean because preserved review reports deliberately retain trailing whitespace.** | The base-to-candidate and prior-candidate-to-current-candidate checks each returned exit `2` only for two Markdown hard-break lines in preserved reports. The pre-commit configuration excludes Issue #1 reports from whitespace and EOF normalization to preserve them byte-for-byte.[15] This is an explicit preservation trade-off, not a source-code formatting failure. |
| **A-03** | **The root secret baseline contains two unverified review-report detections.** | Direct inspection shows the flagged lines are historical command and validation prose rather than a credential; however, the baseline still records both with `is_verified: false`.[16] These entries should remain explicitly classified during future baseline maintenance rather than being treated as proof of a real secret or silently ignored. |

## 6. Acceptance-criteria assessment

| # | Issue #1 acceptance criterion | Assessment | Evidence and boundary |
|---:|---|---|---|
| 1 | Project-specific values are configurable or clearly documented | **PASS** | `harness-config.toml`, navigation, and runbooks separate configuration from reusable harness artifacts.[1] [17] |
| 2 | Remaining Continuum references are intentional provenance or examples | **PASS** | Focused residual-reference suite passed, including the `harness/` scan requirement; intentional provenance is documented.[18] |
| 3 | No machine-specific local paths remain in operational templates | **PASS** | Template-generation and clean-room validation passed; the residual policy covers machine-path patterns.[18] |
| 4 | A documented process can create a clean new product repository | **PARTIAL** | The documented workflow runs successfully and excludes harness-only provenance, but its first-run secret-scan step is not a meaningful scan of untracked files; see M-01.[9] [14] |
| 5 | A disposable generated repository passes all documented validation commands | **PARTIAL** | Commands exited `0`, but the secret-check command skipped all files before an initial commit; the acceptance criterion requires actual security validation, not only a zero exit code. |
| 6 | Generated repositories do not misrepresent Continuum evidence as their own | **PASS** | Generated lineage explicitly records provenance only and disclaims H0 evidence; prohibited harness paths were absent in the reproduction.[19] |
| 7 | CI passes on the exact implementation commit | **PASS** | Both exact-head-SHA workflow runs and both `validate` check runs were completed successfully.[5] [20] |
| 8 | Independent review uses an isolated clone pinned to an exact 40-character SHA | **PASS** | Checkout gate in Section 1; no moving branch tip was used. |
| 9 | Independent-review evidence is preserved byte-for-byte | **PASS WITH BOUNDARY** | The two reports already present in the prior candidate have identical Git blob IDs at this candidate; the prior re-review report is newly committed here. This final report is delivered with a SHA-256 sidecar. No claim is made that the new historical report can be compared to an unavailable external pre-commit copy. |
| 10 | Final PR-head CI is green | **PASS** | The reviewed SHA remains the current PR head, with a successful pull-request CI run.[4] [5] |
| 11 | Any commits after the independently reviewed implementation commit receive a narrow delta review | **PASS** | This report evaluates the direct parent-to-candidate delta and the exact PR head. |
| 12 | Product-owner approval is required before merge | **FAIL AS AN ENFORCED CONTROL** | The written policy requires it, but `main` is publicly unprotected; see H-01.[1] [2] [13] |
| 13 | Auto-merge remains disabled | **PASS AT REVIEW TIME** | GitHub reported `auto_merge: null` and the PR remains draft and unmerged.[4] |
| 14 | Template-repository mode is enabled only after validated merge | **PASS AT REVIEW TIME** | GitHub reported `is_template: false` and the PR remains unmerged.[4] [5] |

## 7. Preservation, rollback, and evidence boundaries

The two pre-existing Issue #1 review files have identical Git blob IDs between `b5d62179864fed7a68e2210e396e83d9835ee464` and this candidate. The candidate adds the preserved prior re-review report; its current SHA-256 is recorded in the attached integrity log. The active plan and validation dossier correctly continue to present Issue #1 as in remediation, not merged or ready for closeout.[21] [22]

The repository’s documented rollback path is to revert the extraction pull request on `main` and preserve the imported source baseline reference.[2] That procedural rollback record is useful, but its effectiveness is weakened by H-01: an unprotected `main` also permits bypassing the intended PR/approval/CI controls.

The detailed branch-protection endpoint returned HTTP `401` without repository-administration authorization. Therefore, this report distinguishes the public observed state (`protected: false`) from any unavailable nonpublic setting and does not speculate beyond the captured GitHub evidence.

## 8. Final recommendation

> **BLOCK**
>
> The exact candidate has green local validation, green exact-SHA CI, a clean detached checkout, a corrected generated quick start, and a successfully reproduced guard against self-overwrite. Those are substantive improvements over the prior blocked candidate.
>
> However, approval is not supportable while the `main` branch has no GitHub protection enforcing the stated direct-push, CI, and product-owner-approval gates, and while a newly generated repository can report a passing secret check without scanning any untracked initial files. Both defects are safety-control failures that remain material despite the passing test suite. No merge, deployment, template activation, or auto-merge should be authorized from this review.

## 9. Supporting evidence artifacts

| Artifact | Purpose |
|---|---|
| `validation-command-log.txt` | Full outputs and exit statuses for required and focused fixed-SHA validation commands |
| `disposable-reproduction-log.txt` | Independent generator-safety and documented-workflow reproduction evidence |
| `generated-secret-scan-probe-log.txt` | Untracked-versus-staged fake-token secret-scan reproduction |
| `integrity-and-delta.txt` | Exact parent/delta, report-blob, `git diff --check`, and final-checkout evidence |
| `external-github-evidence.md` | Raw GitHub evidence inventory, source URLs, and access boundaries |
| `issue-1-independent-review-f88abc14.sha256` | SHA-256 sidecar for this final report, created after finalization |

## References

[1]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/AGENTS.md "AGENTS.md at the exact reviewed candidate"
[2]: https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1 "GitHub Issue #1 — Extract reusable project harness from Continuum H0"
[3]: https://github.com/maxaihappy/project-harness-bootstrap-kit/issues/1#issuecomment-5082290803 "Issue #1 product-owner scope approval"
[4]: https://api.github.com/repos/maxaihappy/project-harness-bootstrap-kit/pulls/2 "Live GitHub API metadata for PR #2"
[5]: https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30216115194 "Successful pull-request CI run for the exact candidate"
[6]: https://github.com/maxaihappy/project-harness-bootstrap-kit/commit/f88abc14fed9b784db6e9481afa22975868718a8 "Exact reviewed remediation commit"
[7]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/pyproject.toml "Candidate Python tooling manifest"
[8]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/.github/workflows/ci.yml "Candidate CI workflow"
[9]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/docs/runbooks/new-repository-checklist.md "Candidate new-repository checklist"
[10]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/templates/product-repo/README.md "Candidate generated README template"
[11]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/harness/generator/render.py "Candidate generator implementation"
[12]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/tests/test_generator_target_safety.py "Candidate generator safety tests"
[13]: https://api.github.com/repos/maxaihappy/project-harness-bootstrap-kit/branches/main "Live public main-branch protection metadata"
[14]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/templates/product-repo/scripts/secrets-check "Candidate generated secret-check script"
[15]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/.pre-commit-config.yaml "Candidate root pre-commit configuration"
[16]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/.secrets.baseline "Candidate root detect-secrets baseline"
[17]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/harness-config.toml "Candidate harness configuration"
[18]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/tests/test_residual_references.py "Candidate residual-reference tests"
[19]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/templates/product-repo/docs/lineage.md "Candidate generated lineage template"
[20]: https://github.com/maxaihappy/project-harness-bootstrap-kit/actions/runs/30216113536 "Successful push CI run for the exact candidate"
[21]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/docs/exec-plans/active/issue-1-project-harness-extraction.md "Candidate active Issue #1 execution plan"
[22]: https://github.com/maxaihappy/project-harness-bootstrap-kit/blob/f88abc14fed9b784db6e9481afa22975868718a8/docs/validation/issue-1-project-harness-extraction.md "Candidate Issue #1 validation dossier"
