# Architecture

{{PROJECT_DISPLAY_NAME}} uses a monorepo with explicit package boundaries. Product directories contain README placeholders until implementation begins.

## Policy sources

| Artifact | Role |
|---|---|
| `architecture-boundaries.toml` | Machine-readable dependency and import policy |
| `tests/architecture/test_package_boundaries.py` | AST-based enforcement |
| This document | Human-readable intent |

## Rules

1. Product-domain directories may depend on `contracts`, but not directly on another product-domain implementation.
2. Harness tooling must not depend on product-domain implementations.
3. Restricted imports require an approved adapter path and ADR update.
4. Placeholder directories must contain no executable source files during bootstrap.
