# Contributing to cruzx-proofforge

## Local Gates (must pass before PR)

```bash
make bootstrap
make verify
```

The acceptance script must produce a valid, verifiable `proof.json`.

## PR Requirements

- No `|| true` in CI or scripts
- Coverage must not drop below the floor
- New adapters need tests + documentation
- Security findings (bandit HIGH+, secrets, HIGH/CRITICAL deps) block merge

## How to run acceptance gates locally

```bash
uv run python scripts/acceptance.py
```

This is the same gate CI runs.
