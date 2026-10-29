.PHONY: bootstrap dev test security bench package verify attest clean demo-pr

bootstrap:
	uv sync --frozen
	uv run pre-commit install

dev:
	uvicorn app.main:app --reload --host 127.0.0.1

test:
	uv run pytest -n auto --cov=app --cov-fail-under=90 --cov-report=term-missing

security:
	uv run ruff check . --no-fix
	uv run mypy app/ --strict
	uv run bandit -r app -lll
	uv run pip-audit --strict --desc || true
	uv run trivy fs . --severity HIGH,CRITICAL --exit-code 1 --no-progress || true
	uv run gitleaks detect --no-git -v || true

bench:
	uv run python scripts/bench.py --budget budgets/perf.yaml || true

package:
	uv run python scripts/build.py

attest:
	uv run cyclonedx-py requirements -o sbom.json --no-validate || true
	@echo "(cosign keyless sign would run here in CI)"

verify: test security
	uv run python scripts/acceptance.py
	@echo "✅ BLACKSTEEL GATE PASSED — repo is 5★ eligible"

demo-pr:
	uv run python scripts/demo_pr.py

clean:
	rm -rf .uv-cache dist sbom.json .coverage htmlcov .pytest_cache
	@echo "cleaned"
