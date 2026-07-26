# Initialize the Project Harness

## Prerequisites

- Git
- Python 3.12
- [uv](https://docs.astral.sh/uv/) package manager

## Bootstrap the harness repository

```bash
git clone https://github.com/maxaihappy/project-harness-bootstrap-kit.git
cd project-harness-bootstrap-kit
bash scripts/bootstrap
```

`scripts/bootstrap` installs locked dependencies, configures Git hooks, and runs the full validation suite.

## Configure project-specific values

Edit [harness-config.toml](../../harness-config.toml) for harness metadata. Generated repositories receive substituted values at creation time.

## Operating roles

| Role | Example tool | Responsibility |
|---|---|---|
| Product owner | Human | Approves scope, decisions, and merge |
| Planner | ChatGPT, Gemini | Requirements, plans, evidence expectations |
| Implementer | Cursor | Repository edits, validation, pull requests |
| Independent reviewer | Manus | Evidence-only review without planner context |
| Repository authority | GitHub | Issues, branches, CI, merge record |

Example tools are configuration choices, not runtime dependencies.

## Authoritative commands

| Command | Purpose |
|---|---|
| `bash scripts/bootstrap` | Install deps, hooks, full validation |
| `bash scripts/check` | Format, lint, test, secrets |
| `bash scripts/generate-project` | Create a new product repository |

## Next steps

- [New repository checklist](new-repository-checklist.md)
- [Harness versus generated boundary](../design-docs/harness-generated-boundary.md)
- [Active Issue #1 execution plan](../exec-plans/active/issue-1-project-harness-extraction.md)
