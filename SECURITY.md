# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

Please report security issues privately.

- Preferred: open a private GitHub security advisory on this repository
- Or email the maintainers (see profile)

**Response SLA**: acknowledgment within 48 hours. We aim to provide a fix or mitigation timeline within 7 days for confirmed high/critical issues.

## Blacksteel Commitments

This repository follows the CruzX Blacksteel Protocol:

- Fail-closed CI (no advisory-only security gates)
- SHA-pinned GitHub Actions
- `persist-credentials: false` on checkout
- Keyless cosign signing of artifacts where applicable
- SBOM generation (CycloneDX)
- No secrets in source or CI logs

If you discover a way to bypass the acceptance gate or produce a false-green proof, please report it — that is a critical finding.
