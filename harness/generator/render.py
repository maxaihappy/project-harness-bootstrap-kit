"""Project repository generation from harness templates."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from harness.reference_policy import find_residual_references

PLACEHOLDER_PATTERN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

HARNESS_ONLY_PATHS = (
    "docs/reference/approved-inputs",
    "docs/reference/exports",
    "docs/exec-plans/completed",
    "docs/validation/h0-repository-bootstrap.md",
    "docs/validation/reviews",
    "docs/strategy/project-continuum-proposal.md",
    "harness-config.toml",
    "templates",
    "scripts/generate-project",
)


IGNORED_TEMPLATE_PARTS = {".ruff_cache", "__pycache__", ".git", ".pytest_cache", ".venv"}
TEXT_SUFFIXES = {".md", ".toml", ".yaml", ".yml", ".py", ".sh", ""}


def _iter_template_files(template_root: Path) -> list[Path]:
    files: list[Path] = []
    for source in template_root.rglob("*"):
        if source.is_dir():
            continue
        if any(part in IGNORED_TEMPLATE_PARTS for part in source.parts):
            continue
        if source.suffix not in TEXT_SUFFIXES and source.name not in {
            "Makefile",
            ".gitignore",
            ".pre-commit-config.yaml",
            ".python-version",
            ".secrets.baseline",
        }:
            continue
        files.append(source)
    return sorted(files)


@dataclass(frozen=True)
class GenerationResult:
    target: Path
    substituted_files: int


def _substitute_content(content: str, values: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise KeyError(f"Missing template value: {key}")
        return values[key]

    return PLACEHOLDER_PATTERN.sub(replace, content)


def _build_values(project_name: str, display_name: str, description: str) -> dict[str, str]:
    return {
        "PROJECT_NAME": project_name,
        "PROJECT_DISPLAY_NAME": display_name,
        "PROJECT_DESCRIPTION": description,
    }


def _target_is_non_empty(target_dir: Path) -> bool:
    if not target_dir.exists():
        return False
    return any(target_dir.iterdir())


def generate_project(
    harness_root: Path,
    target_dir: Path,
    project_name: str,
    display_name: str,
    *,
    description: str | None = None,
    overwrite: bool = False,
) -> GenerationResult:
    template_root = harness_root / "templates" / "product-repo"
    if not template_root.is_dir():
        raise FileNotFoundError(f"Template tree not found: {template_root}")

    if target_dir.exists():
        if _target_is_non_empty(target_dir):
            if not overwrite:
                raise FileExistsError(
                    f"Target directory is not empty: {target_dir}. "
                    "Use --overwrite to replace an existing directory intentionally."
                )
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
    else:
        target_dir.mkdir(parents=True, exist_ok=True)

    values = _build_values(
        project_name,
        display_name,
        description or f"Product repository for {display_name}",
    )
    substituted = 0

    for source in _iter_template_files(template_root):
        rel = source.relative_to(template_root)
        destination = target_dir / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = source.read_text(encoding="utf-8")
        if "{{" in content:
            content = _substitute_content(content, values)
            substituted += 1
        destination.write_text(content, encoding="utf-8")

    for script in (target_dir / "scripts").glob("*"):
        if script.is_file():
            script.chmod(0o755)

    return GenerationResult(target=target_dir, substituted_files=substituted)


def assert_no_harness_provenance(target_dir: Path) -> list[str]:
    missing: list[str] = []
    for rel in HARNESS_ONLY_PATHS:
        if (target_dir / rel).exists():
            missing.append(rel)
    return missing


def assert_clean_room_references(target_dir: Path) -> list[str]:
    return find_residual_references(
        target_dir,
        allow_prefixes=(),
        scan_roots_list=(
            "AGENTS.md",
            "README.md",
            "ARCHITECTURE.md",
            "pyproject.toml",
            "architecture-boundaries.toml",
            "scripts/",
            "tests/",
            "docs/",
            "packages/",
        ),
    )


def run_generated_check(target_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", "scripts/check"],
        cwd=target_dir,
        capture_output=True,
        text=True,
        check=False,
    )
