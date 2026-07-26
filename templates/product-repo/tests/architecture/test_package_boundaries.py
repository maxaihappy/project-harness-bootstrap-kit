from pathlib import Path

from tests.architecture.boundary_checker import check_placeholder_directories, check_policy

ROOT = Path(__file__).resolve().parents[2]
MAIN_POLICY = ROOT / "architecture-boundaries.toml"


def test_main_policy_has_no_violations() -> None:
    violations = check_policy(MAIN_POLICY, ROOT)
    assert not violations


def test_placeholder_directories_are_clean() -> None:
    import tomllib

    policy = tomllib.loads(MAIN_POLICY.read_text(encoding="utf-8"))
    violations = check_placeholder_directories(policy, ROOT)
    assert not violations
