"""Documented runbook workflow alignment tests."""

from __future__ import annotations

import re
from pathlib import Path

from harness.generator.workflow import OPERATOR_COMMANDS_IN_TARGET

ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = ROOT / "docs/runbooks/new-repository-checklist.md"


def _extract_generation_commands(runbook_text: str) -> list[str]:
    match = re.search(r"## Generation\s+```bash\n(.*?)```", runbook_text, re.DOTALL)
    assert match, "Generation code block not found in runbook"
    commands: list[str] = []
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("bash scripts/generate-project"):
            continue
        if stripped.startswith("cd "):
            continue
        commands.append(stripped)
    return commands


def test_runbook_documents_operator_workflow_exactly() -> None:
    runbook_text = RUNBOOK_PATH.read_text(encoding="utf-8")
    documented = _extract_generation_commands(runbook_text)
    assert documented == list(OPERATOR_COMMANDS_IN_TARGET)


def test_documented_workflow_fails_without_git_init(tmp_path: Path) -> None:
    from harness.generator.render import generate_project
    from harness.generator.workflow import run_operator_commands

    target = tmp_path / "no-git-product"
    generate_project(ROOT, target, "no-git-product", "No Git Product")

    try:
        run_operator_commands(target, ("uv lock", "bash scripts/bootstrap"))
        raise AssertionError("Expected bootstrap to fail without git init")
    except RuntimeError as exc:
        assert "bash scripts/bootstrap" in str(exc)
