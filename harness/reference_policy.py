"""Shared residual-reference policy for harness validation and generation."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

FORBIDDEN_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?i)\bcontinuum\b"),
    re.compile(r"maxaihappy/continuum"),
    re.compile(r"Project Continuum"),
    re.compile(r"/Users/"),
    re.compile(r"bootstrap/h0"),
)

SCAN_EXTENSIONS = {
    ".md",
    ".toml",
    ".yaml",
    ".yml",
    ".py",
    ".sh",
    ".json",
}


def load_harness_config(root: Path) -> dict:
    config_path = root / "harness-config.toml"
    return tomllib.loads(config_path.read_text(encoding="utf-8"))


def provenance_allow_prefixes(config: dict) -> tuple[str, ...]:
    prefixes = config.get("residual_references", {}).get("allow_prefixes", [])
    return tuple(prefixes)


def scan_roots(config: dict) -> tuple[str, ...]:
    roots = config.get("residual_references", {}).get("scan_roots", [])
    return tuple(roots)


def is_allowlisted(rel_path: str, allow_prefixes: tuple[str, ...]) -> bool:
    return any(
        rel_path == prefix.rstrip("/") or rel_path.startswith(prefix) for prefix in allow_prefixes
    )


def iter_scanned_files(root: Path, scan_roots_list: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for entry in scan_roots_list:
        path = root / entry
        if path.is_file():
            files.append(path)
            continue
        if not path.is_dir():
            continue
        for candidate in path.rglob("*"):
            if not candidate.is_file():
                continue
            if candidate.suffix in SCAN_EXTENSIONS or candidate.name in {"AGENTS.md", "Makefile"}:
                files.append(candidate)
    return sorted(set(files))


def find_residual_references(
    root: Path,
    *,
    allow_prefixes: tuple[str, ...],
    scan_roots_list: tuple[str, ...],
) -> list[str]:
    offenders: list[str] = []
    for file_path in iter_scanned_files(root, scan_roots_list):
        rel = file_path.relative_to(root).as_posix()
        if is_allowlisted(rel, allow_prefixes):
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(content):
                offenders.append(f"{rel}: matched {pattern.pattern}")
                break
    return offenders
