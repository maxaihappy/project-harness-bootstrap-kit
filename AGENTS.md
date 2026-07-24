# Agent Navigation Map

This repository is the system of record for Project Continuum. Read documents in this order:

1. [Canonical proposal](docs/strategy/project-continuum-proposal.md) — product strategy and constraints
2. [Architecture policy](ARCHITECTURE.md) and [architecture-boundaries.toml](architecture-boundaries.toml) — dependency rules
3. [Approved H0 baseline](docs/reference/approved-inputs/h0-repository-bootstrap-approved.md) — immutable approved execution input
4. [Active execution plan](docs/exec-plans/active/h0-repository-bootstrap.md) — mutable execution record and status
5. [ADRs](docs/decisions/) — technical decisions
6. [Validation evidence](docs/validation/h0-repository-bootstrap.md) — test results and review outcomes

**Document authority:** Markdown sources override presentation exports. The approved H0 baseline is immutable; the active execution plan is mutable. See [document register](docs/governance/document-register.md).

## Authoritative commands

All commands run from the repository root:

| Command | Purpose |
|---|---|
| `bash scripts/bootstrap` | Install locked deps, Git hooks, and run full checks |
| `bash scripts/check` | Non-mutating full validation (format, lint, test, secrets) |
| `bash scripts/test` | Run pytest suite |
| `bash scripts/secrets-check` | Run detect-secrets without modifying baseline |

Makefile targets delegate to these scripts for convenience.

## Branch policy

- Work on feature branches; do not push directly to `main`.
- H0 work occurs on `bootstrap/h0`.
- Merge requires explicit product-owner approval.

## Approval gates

- Material product or architecture decisions require product-owner approval and an ADR.
- Secret baseline changes require explicit review in the pull request.
- Do not merge, deploy, or enable auto-merge without approval.

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

## H0 scope reminder

H0 delivers repository harness only. No Telegram, model providers, database, cloud infrastructure, deployment, memory, trust, or other Continuum product behavior.
