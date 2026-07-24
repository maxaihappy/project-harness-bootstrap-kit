# Architecture

Project Continuum uses a monorepo with explicit package boundaries. During H0, product directories contain README placeholders only; no importable product packages exist.

## Policy sources

| Artifact | Role |
|---|---|
| `architecture-boundaries.toml` | Machine-readable dependency and import policy |
| `tests/architecture/test_package_boundaries.py` | AST-based enforcement |
| This document | Human-readable intent |

## H0 dependency intent

```text
product boundary placeholders  ──future──> contracts
harness tooling                ──────────> contracts and standard library only
tests                          ──────────> test utilities and documented public boundaries
```

## Rules

1. Product-domain directories may eventually depend on `contracts`, but not directly on another product-domain implementation.
2. Harness tooling must not depend on product-domain implementations.
3. Telegram, model-provider, database, and cloud SDK imports are location-restricted, not permanently banned.
4. In H0, no adapter or infrastructure source directory is approved, so such imports are prohibited in executable H0 files.
5. In H1+, an adapter directory is approved by updating the architecture policy and an ADR—not by weakening or bypassing the test.
6. Placeholder product directories must contain no executable source files during H0.

## Remediation

When the architecture test fails, it names the violating file, import, applicable policy rule, and remediation path (update policy via ADR or remove the import).
