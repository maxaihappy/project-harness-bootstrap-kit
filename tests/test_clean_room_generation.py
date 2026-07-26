"""Clean-room generated repository validation for Issue #1."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from harness.generator.render import (
    assert_clean_room_references,
    assert_no_harness_provenance,
    generate_project,
    run_generated_check,
)

ROOT = Path(__file__).resolve().parents[1]


def _subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    return env


def test_clean_room_generation_passes_validation(tmp_path: Path) -> None:
    target = tmp_path / "clean-room-product"
    generate_project(
        ROOT,
        target,
        "clean-room-product",
        "Clean Room Product",
    )

    provenance_hits = assert_no_harness_provenance(target)
    assert not provenance_hits, f"Harness provenance leaked: {provenance_hits}"

    residual_hits = assert_clean_room_references(target)
    assert not residual_hits, "Residual references:\n" + "\n".join(residual_hits)

    subprocess.run(["git", "init"], cwd=target, check=True, capture_output=True)

    lock = subprocess.run(
        ["uv", "lock"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
        env=_subprocess_env(),
    )
    assert lock.returncode == 0, lock.stderr

    for command in (
        ["bash", "scripts/bootstrap"],
        ["bash", "scripts/test"],
        ["bash", "scripts/secrets-check"],
        ["bash", "scripts/check"],
    ):
        completed = subprocess.run(
            command,
            cwd=target,
            capture_output=True,
            text=True,
            check=False,
            env=_subprocess_env(),
        )
        assert completed.returncode == 0, (
            f"{command} failed:\n{completed.stderr}\n{completed.stdout}"
        )

    check = run_generated_check(target)
    assert check.returncode == 0, check.stderr
