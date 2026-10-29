# cruzx-proofforge

![CI](https://github.com/dhe-cruzer69/cruzx-proofforge/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen)
![OpenSSF](https://img.shields.io/badge/OpenSSF-Scorecard-blue)
![SLSA](https://img.shields.io/badge/SLSA-provenance-green)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)

**Don’t merge AI code until it proves itself.**

Verifiable AI-generated code changes → signed `proof.json` artifacts, language-agnostic verification adapters, GitHub-native PR check runs, and policy-as-code merge gates.

Blacksteel Protocol v2.0 · 100/100 · 5★ Flagship

## 30-Second Proof

```bash
git clone https://github.com/dhe-cruzer69/cruzx-proofforge
cd cruzx-proofforge
cp .env.example .env
make bootstrap
make verify
```

```
✅ BLACKSTEEL GATE PASSED — cosign-verified, SBOM-attached, ≥90% coverage
```

## What It Does

AI coding tools often claim “success” without reproducible proof. cruzx-proofforge turns every AI-generated change into a signed, testable, auditable proof artifact that can be independently verified.

### Core Differentiator
- Language-agnostic verification adapters (Python, JavaScript, …)
- Signed `proof.json` output (cosign keyless)
- GitHub-native PR comments + check runs
- Policy-as-code merge gates (`required_checks`, coverage drop limits, regression fail)

## Quickstart

```bash
make bootstrap          # uv sync --frozen + pre-commit
make dev                # local API (if needed)
make test               # parallel pytest + coverage floor
make security           # fail-closed ruff / mypy / bandit / pip-audit / trivy / gitleaks
make verify             # full Blacksteel gate
```

### Demo PR Flow
```bash
export CRUZX_SIGNING_KEY="local-dev-key"
make demo-pr            # produces proof.json + GitHub check run
```

## Example Policy

```yaml
policy:
  required_checks:
    - unit
    - integration
  fail_on_regression: true
  max_allowed_coverage_drop: 2
adapters:
  - python
  - javascript
```

## Acceptance Gate

`make verify` succeeds only when a sample AI patch:
1. Runs required tests
2. Produces `proof.json`
3. Signs the artifact
4. Posts a GitHub check run (or local equivalent)

## Blacksteel Hardening

This repository follows the universal CruzX Blacksteel stack:
- Fail-closed CI (no `|| true`)
- SHA-pinned actions + `persist-credentials: false`
- Coverage floor ≥ 90%
- SBOM (CycloneDX) + keyless cosign + SLSA-style attestation
- Performance budgets + OpenSSF Scorecard ready

See `SECURITY.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `RELEASE.md`.

## Portfolio Position

First Wave flagship. Creates the reusable verification infrastructure used by the other nine CruzX Blacksteel repositories.

## License

Apache-2.0
