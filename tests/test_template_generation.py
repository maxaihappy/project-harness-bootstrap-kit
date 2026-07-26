"""Template generation validation for Issue #1."""

from __future__ import annotations

import subprocess
from pathlib import Path

from harness.generator.render import generate_project

ROOT = Path(__file__).resolve().parents[1]


def test_generate_project_substitutes_placeholders(tmp_path: Path) -> None:
    target = tmp_path / "generated-product"
    result = generate_project(
        ROOT,
        target,
        "demo-product",
        "Demo Product",
        description="Demo product repository",
    )
    assert result.target == target
    readme = (target / "README.md").read_text(encoding="utf-8")
    assert "Demo Product" in readme
    assert "{{PROJECT_NAME}}" not in readme
    pyproject = (target / "pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "demo-product"' in pyproject


def test_generate_project_script_entrypoint(tmp_path: Path) -> None:
    target = tmp_path / "cli-product"
    completed = subprocess.run(
        ["bash", "scripts/generate-project", str(target), "cli-product", "CLI Product"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert (target / "AGENTS.md").is_file()
