"""Documented operator workflow for generated product repositories."""

from __future__ import annotations

import os
import subprocess
from collections.abc import Sequence
from pathlib import Path

from harness.generator.render import generate_project

# Canonical post-generation commands executed inside the generated repository.
# docs/runbooks/new-repository-checklist.md must list these in this exact order.
OPERATOR_COMMANDS_IN_TARGET: tuple[str, ...] = (
    "git init",
    "uv lock",
    "bash scripts/bootstrap",
    "bash scripts/test",
    "bash scripts/secrets-check",
    "bash scripts/check",
)

# Commands advertised in generated README and AGENTS quick-start guidance.
QUICK_START_COMMANDS: tuple[str, ...] = OPERATOR_COMMANDS_IN_TARGET[:3]


def format_command_block(commands: Sequence[str]) -> str:
    return "\n".join(commands)


def subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    return env


def run_operator_commands(
    target_dir: Path, commands: Sequence[str] = OPERATOR_COMMANDS_IN_TARGET
) -> None:
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=target_dir,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
            env=subprocess_env(),
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"Operator command failed ({command}):\n{completed.stderr}\n{completed.stdout}"
            )


def run_documented_new_repository_workflow(
    harness_root: Path,
    target_dir: Path,
    project_name: str,
    display_name: str,
    *,
    overwrite: bool = False,
) -> None:
    generate_project(
        harness_root,
        target_dir,
        project_name,
        display_name,
        overwrite=overwrite,
    )
    run_operator_commands(target_dir)
