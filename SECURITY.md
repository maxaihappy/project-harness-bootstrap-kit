# Security

## H0 scope

H0 establishes secret detection and secure CI practices. No production services, credentials, or external integrations exist.

## Secret handling

- Never commit secrets, tokens, API keys, or credentials.
- Run `bash scripts/secrets-check` before pushing.
- Baseline changes require explicit pull-request review via `bash scripts/secrets-baseline` only when intentional.
- A detected real secret must be removed and rotated; baselining is not proof a finding is safe.

## CI

- GitHub Actions workflows use least privilege (`contents: read`).
- Actions are pinned to full commit SHAs.
- No repository secrets are used in H0 CI.

## Reporting

Report security concerns to the product owner through GitHub issues or private channels as defined by project policy.
