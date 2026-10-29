#!/usr/bin/env python3
"""Blacksteel acceptance gate for cruzx-proofforge.

Succeeds when a sample AI patch:
1. Runs required tests (simulated)
2. Produces proof.json
3. Signs the artifact
4. Can be verified
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Ensure package is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.proof import ProofEngine


def main() -> int:
    engine = ProofEngine(signing_key="acceptance-key")

    # Simulate an AI-generated change
    sample_payload = {
        "change_id": "demo-ai-patch-001",
        "files": ["src/example.py"],
        "tests_passed": True,
        "checks": ["unit", "integration"],
        "policy": {
            "required_checks": ["unit", "integration"],
            "fail_on_regression": True,
            "max_allowed_coverage_drop": 2,
        },
    }

    proof = engine.generate(sample_payload)

    # Write proof artifact
    out = Path("proof.json")
    out.write_text(json.dumps(proof, indent=2))
    print(f"Wrote {out}")

    # Verify
    if not engine.verify(proof, sample_payload):
        print("FAIL: proof verification failed")
        return 1

    # Required fields check
    required = ["version", "timestamp", "payload_sha256", "signature", "status"]
    missing = [k for k in required if k not in proof]
    if missing:
        print(f"FAIL: missing fields {missing}")
        return 1

    if proof["status"] != "verified":
        print("FAIL: status is not verified")
        return 1

    print("✅ Acceptance gate passed — proof generated, signed, and verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
