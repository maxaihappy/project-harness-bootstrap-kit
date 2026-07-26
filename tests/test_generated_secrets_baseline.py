"""Generated-repository secrets-baseline command tests."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from harness.generator.workflow import run_documented_new_repository_workflow

ROOT = Path(__file__).resolve().parents[1]


def _subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    return env


def test_generated_repository_make_secrets_baseline_succeeds(tmp_path: Path) -> None:
    target = tmp_path / "secrets-baseline-product"
    run_documented_new_repository_workflow(
        ROOT,
        target,
        "secrets-baseline-product",
        "Secrets Baseline Product",
    )

    completed = subprocess.run(
        ["make", "secrets-baseline"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
        env=_subprocess_env(),
    )
    assert completed.returncode == 0, f"{completed.stderr}\n{completed.stdout}"
    assert (target / "scripts/secrets-baseline").is_file()
