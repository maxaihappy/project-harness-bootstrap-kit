# New Repository Checklist

Use this checklist when creating a product repository from the harness.

## Before generation

- [ ] Harness repository passes `bash scripts/check`
- [ ] Target product name and display name are chosen
- [ ] Target directory does not already exist (or use `--overwrite` intentionally)
- [ ] Product owner approves repository creation

## Generation

```bash
bash scripts/generate-project /path/to/new-repo <project-name> "<Display Name>"
cd /path/to/new-repo
git init
uv lock
bash scripts/bootstrap
bash scripts/test
bash scripts/secrets-check
bash scripts/check
```

To replace an existing non-empty directory intentionally:

```bash
bash scripts/generate-project --overwrite /path/to/new-repo <project-name> "<Display Name>"
```

## After generation

- [ ] `docs/lineage.md` records harness provenance only
- [ ] No H0 validation dossiers or imported product strategy documents are present
- [ ] `bash scripts/check` passes in the generated repository
- [ ] `make secrets-baseline` succeeds when baseline maintenance is required
- [ ] Residual-reference validation shows no unintended import references
- [ ] Set the product remote on the initialized Git repository
- [ ] Create product-specific governance documents as needed
- [ ] Do not claim harness H0 evidence as product evidence

## Generated repository must not include

- `docs/reference/approved-inputs/`
- `docs/validation/h0-*` or `docs/validation/reviews/h0-*`
- Imported product strategy proposal under `docs/strategy/`
- `harness-config.toml` or `templates/`

## Rollback

Delete the generated directory and regenerate from the harness at a known commit.
