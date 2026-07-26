# Project Harness Bootstrap Kit

Reusable repository harness and bootstrap kit for agent-first engineering workflows.

This repository generalizes a validated H0 governance foundation into a product-neutral harness. Historical import artifacts under `docs/reference/`, `docs/validation/h0-*`, and `docs/exec-plans/completed/` are intentional provenance only.

## Status

Issue #1 extraction is in progress on branch `foundation/extract-project-harness` ([PR #2](https://github.com/maxaihappy/project-harness-bootstrap-kit/pull/2)). See [AGENTS.md](AGENTS.md) for navigation and [docs/exec-plans/active/issue-1-project-harness-extraction.md](docs/exec-plans/active/issue-1-project-harness-extraction.md) for the active execution plan.

## Prerequisites

- Git
- Python 3.12
- [uv](https://docs.astral.sh/uv/) package manager

## Quick start

```bash
bash scripts/bootstrap
```

## Generate a new product repository

```bash
bash scripts/generate-project /path/to/new-repo example-product "Example Product"
```

See [docs/runbooks/initialize-harness.md](docs/runbooks/initialize-harness.md) and [docs/runbooks/new-repository-checklist.md](docs/runbooks/new-repository-checklist.md).

## Validation

```bash
bash scripts/check
```

## Configuration

Project-specific values live in [harness-config.toml](harness-config.toml).
