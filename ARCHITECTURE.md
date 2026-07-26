# Architecture

The project harness uses a monorepo with explicit package boundaries. Product directories contain README placeholders only during harness bootstrap; no importable product packages exist until a generated repository implements them.

## Policy sources

| Artifact | Role |
|---|---|
| `architecture-boundaries.toml` | Machine-readable dependency and import policy |
| `harness-config.toml` | Project-specific package layout and configuration |
| `tests/architecture/test_package_boundaries.py` | AST-based enforcement |
| This document | Human-readable intent |

## Dependency intent

```text
product boundary placeholders  ──future──> contracts
harness tooling                ──────────> contracts and standard library only
tests                          ──────────> test utilities and documented public boundaries
```

## Rules

1. Product-domain directories may eventually depend on `contracts`, but not directly on another product-domain implementation.
2. Harness tooling must not depend on product-domain implementations.
3. Channel, model-provider, database, and cloud SDK imports are location-restricted, not permanently banned.
4. During harness bootstrap, no adapter or infrastructure source directory is approved, so such imports are prohibited in executable harness files.
5. In later stages, an adapter directory is approved by updating the architecture policy and an ADR—not by weakening or bypassing the test.
6. Placeholder product directories must contain no executable source files during harness bootstrap.

## Remediation

When the architecture test fails, it names the violating file, import, applicable policy rule, and remediation path (update policy via ADR or remove the import).
