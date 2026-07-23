from pathlib import Path

import pytest

from tests.architecture.boundary_checker import Violation, check_file, check_policy

ROOT = Path(__file__).resolve().parents[2]
MAIN_POLICY = ROOT / "architecture-boundaries.toml"
FIXTURE_POLICY = ROOT / "tests/fixtures/architecture/policy.toml"


def _format_violations(violations: list[Violation]) -> str:
    return "\n".join(
        f"{v.file}: import '{v.import_name}' violates {v.rule}. {v.remediation}" for v in violations
    )


def test_main_policy_has_no_violations() -> None:
    violations = check_policy(MAIN_POLICY, ROOT)
    assert not violations, _format_violations(violations)


@pytest.mark.parametrize(
    ("fixture_file", "expect_violation"),
    [
        ("harness/allowed_stdlib.py", False),
        ("relationship_core/disallowed_product_cross.py", True),
        ("workspace/disallowed_provider_sdk.py", True),
        ("adapters/model/allowed_adapter_path.py", False),
    ],
)
def test_fixture_policy_cases(fixture_file: str, expect_violation: bool) -> None:
    import tomllib

    policy = tomllib.loads(FIXTURE_POLICY.read_text(encoding="utf-8"))
    rel = Path("tests/fixtures/architecture/cases") / fixture_file
    violations = check_file(rel, policy, ROOT)
    if expect_violation:
        assert violations, f"Expected violation for {fixture_file}"
    else:
        assert not violations, _format_violations(violations)
