# Agent Navigation Map

This repository was generated from the project harness bootstrap kit for **{{PROJECT_DISPLAY_NAME}}**.

## Authoritative commands

| Command | Purpose |
|---|---|
| `bash scripts/bootstrap` | Install locked deps, Git hooks, and run full checks |
| `bash scripts/check` | Non-mutating full validation |
| `bash scripts/test` | Run pytest suite |
| `bash scripts/secrets-check` | Run detect-secrets without modifying baseline |

## Governance

- [Document register](docs/governance/document-register.md)
- [Lineage](docs/lineage.md)

## Operating roles

| Role | Accountability |
|---|---|
| Product owner | Approves scope, material decisions, and merge |
| Planner | Produces requirements, plans, and evidence expectations |
| Implementer | Edits repository, runs checks, prepares pull requests |
| Independent reviewer | Reviews repository evidence without planner-chat context |
| Repository authority | Owns issues, branches, CI, and merge record |

Example tools (Cursor, Manus, GitHub) are configuration choices, not runtime requirements.
