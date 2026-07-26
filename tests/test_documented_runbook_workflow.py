"""Documented runbook workflow alignment tests."""

from __future__ import annotations

import re
from pathlib import Path

from harness.generator.render import generate_project
from harness.generator.workflow import (
    OPERATOR_COMMANDS_IN_TARGET,
    QUICK_START_COMMANDS,
    format_command_block,
)

ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = ROOT / "docs/runbooks/new-repository-checklist.md"


def _extract_bash_block(markdown_text: str, heading: str) -> list[str]:
    pattern = rf"{re.escape(heading)}(?:.|\n)*?```bash\n(.*?)```"
    match = re.search(pattern, markdown_text, re.DOTALL)
    assert match, f"Bash block not found for heading: {heading}"
    commands: list[str] = []
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if stripped:
            commands.append(stripped)
    return commands


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


def test_generated_readme_quick_start_matches_canonical_workflow(tmp_path: Path) -> None:
    target = tmp_path / "readme-workflow"
    generate_project(ROOT, target, "readme-workflow", "Readme Workflow")
    readme_text = (target / "README.md").read_text(encoding="utf-8")
    documented = _extract_bash_block(readme_text, "## Quick start")
    assert documented == list(QUICK_START_COMMANDS)


def test_generated_agents_setup_matches_canonical_workflow(tmp_path: Path) -> None:
    target = tmp_path / "agents-workflow"
    generate_project(ROOT, target, "agents-workflow", "Agents Workflow")
    agents_text = (target / "AGENTS.md").read_text(encoding="utf-8")
    documented = _extract_bash_block(agents_text, "## First-time setup")
    assert documented == list(QUICK_START_COMMANDS)


def test_generated_quick_start_command_block_helper() -> None:
    assert format_command_block(QUICK_START_COMMANDS) == "\n".join(QUICK_START_COMMANDS)


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
