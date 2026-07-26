# Harness and Generated Repository Boundary

## Purpose

Define what belongs in the harness repository versus a generated product repository.

## Harness repository

The harness repository maintains:

- Reusable governance, validation, and generation tooling
- Immutable H0 provenance under `docs/reference/` and `docs/validation/h0-*`
- Issue execution plans and extraction evidence
- `harness-config.toml`, `templates/`, and `scripts/generate-project`

## Generated product repository

A generated repository receives:

- Substituted project values (`{{PROJECT_NAME}}`, display name, description)
- Operational scripts, architecture policy, and validation tests
- A minimal `docs/lineage.md` provenance pointer
- Product-specific placeholders under `packages/`

A generated repository must **not** include:

- H0 approved baseline or validation dossiers
- Manus review reports from the harness import
- Imported product strategy documents
- Harness-only configuration (`harness-config.toml`, `templates/`)

## Evidence boundary

H0 and Issue #1 validation evidence in the harness repository does not validate generated repositories. Generated repositories establish their own evidence through local validation and CI after creation.

## Generation contract

`scripts/generate-project` is the authoritative generation entry point. Clean-room validation confirms generated output excludes harness provenance and passes documented validation commands after `uv lock`.
