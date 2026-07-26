# Agent Navigation Map

This repository is the system of record for the **Project Harness Bootstrap Kit**. Read documents in this order:

1. [Harness configuration](harness-config.toml) — project-specific values and provenance metadata
2. [Architecture policy](ARCHITECTURE.md) and [architecture-boundaries.toml](architecture-boundaries.toml) — dependency rules
3. [Active Issue #1 execution plan](docs/exec-plans/active/issue-1-project-harness-extraction.md) — current extraction work
4. [Issue #1 validation dossier](docs/validation/issue-1-project-harness-extraction.md) — extraction evidence record
5. [ADRs](docs/decisions/) — technical decisions
6. [H0 completed execution record](docs/exec-plans/completed/h0-repository-bootstrap.md) — import provenance only

**Document authority:** Markdown sources override presentation exports. H0 provenance artifacts document the imported baseline only; they do not validate Issue #1 or generated repositories. See [document register](docs/governance/document-register.md).

## Harness versus generated repositories

| Concern | Harness repository | Generated product repository |
|---|---|---|
| Purpose | Maintain reusable governance, validation, and generation tooling | Host product-specific work |
| Provenance | Retains H0 import evidence and Issue #1 extraction records | Includes only a lineage document pointer |
| Configuration | `harness-config.toml` at repository root | Substituted project values from generation |
| Generation | Runs `scripts/generate-project` | Is the output of generation |

See [docs/design-docs/harness-generated-boundary.md](docs/design-docs/harness-generated-boundary.md).

## Operating roles (responsibility-based)

| Role | Example tool | Accountability |
|---|---|---|
| Product owner | Human | Approves scope, material decisions, and merge |
| Planner | ChatGPT, Gemini, or equivalent | Produces requirements, plans, and evidence expectations |
| Implementer | Cursor or equivalent | Edits repository, runs checks, prepares pull requests |
| Independent reviewer | Manus or equivalent | Reviews repository evidence without planner-chat context |
| Repository authority | GitHub | Owns issues, branches, CI, review history, and merge record |

Cursor, Manus, and GitHub are example operating configuration, not runtime requirements.

## Authoritative commands

All commands run from the repository root:

| Command | Purpose |
|---|---|
| `bash scripts/bootstrap` | Install locked deps, Git hooks, and run full checks |
| `bash scripts/check` | Non-mutating full validation (format, lint, test, secrets) |
| `bash scripts/test` | Run pytest suite |
| `bash scripts/secrets-check` | Run detect-secrets without modifying baseline |
| `bash scripts/generate-project` | Generate a new product repository from templates |

Makefile targets delegate to these scripts for convenience.

## Branch policy

- Work on feature branches; do not push directly to `main`.
- Issue #1 work occurs on `foundation/extract-project-harness` (PR #2).
- Merge requires explicit product-owner approval.

## Approval gates

- Material product or architecture decisions require product-owner approval and an ADR.
- Secret baseline changes require explicit review in the pull request.
- Do not merge, deploy, enable template-repository mode, or enable auto-merge without approval.

## Escalation

Stop and escalate to the product owner when:

- Repository state conflicts with the active execution plan or issue scope.
- A check fails and the fix would weaken validation or introduce product behavior.
- A secret is detected — remove and rotate; do not baseline without review.
- An undocumented runtime dependency would be required.

## Related policy documents

- [SECURITY.md](SECURITY.md)
- [PRIVACY.md](PRIVACY.md)
- [RELIABILITY.md](RELIABILITY.md)
- [COST.md](COST.md)
- [README.md](README.md)

## Scope reminder

This harness delivers repository governance and validation tooling only. No product runtime behavior, deployment, infrastructure, or template-repository activation before validated merge.
