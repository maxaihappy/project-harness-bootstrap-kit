"""Generator target-directory safety tests."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from harness.generator.render import generate_project

ROOT = Path(__file__).resolve().parents[1]


def test_generate_into_missing_target(tmp_path: Path) -> None:
    target = tmp_path / "missing-target"
    result = generate_project(ROOT, target, "missing-target", "Missing Target")
    assert result.target == target
    assert (target / "README.md").is_file()


def test_generate_into_empty_target(tmp_path: Path) -> None:
    target = tmp_path / "empty-target"
    target.mkdir()
    result = generate_project(ROOT, target, "empty-target", "Empty Target")
    assert result.target == target
    assert (target / "README.md").is_file()


def test_generate_refuses_non_empty_target_without_overwrite(tmp_path: Path) -> None:
    target = tmp_path / "occupied-target"
    target.mkdir()
    sentinel = target / "sentinel.txt"
    sentinel.write_text("preserve-me", encoding="utf-8")

    with pytest.raises(FileExistsError, match="not empty"):
        generate_project(ROOT, target, "occupied-target", "Occupied Target")

    assert sentinel.is_file()
    assert sentinel.read_text(encoding="utf-8") == "preserve-me"


def test_generate_overwrites_non_empty_target_when_requested(tmp_path: Path) -> None:
    target = tmp_path / "overwrite-target"
    target.mkdir()
    sentinel = target / "sentinel.txt"
    sentinel.write_text("remove-me", encoding="utf-8")

    result = generate_project(
        ROOT,
        target,
        "overwrite-target",
        "Overwrite Target",
        overwrite=True,
    )
    assert result.target == target
    assert not sentinel.exists()
    assert (target / "README.md").is_file()


def test_generate_project_script_requires_explicit_overwrite(tmp_path: Path) -> None:
    target = tmp_path / "cli-occupied"
    target.mkdir()
    (target / "sentinel.txt").write_text("preserve-me", encoding="utf-8")

    completed = subprocess.run(
        ["bash", "scripts/generate-project", str(target), "cli-occupied", "CLI Occupied"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode != 0
    assert (target / "sentinel.txt").read_text(encoding="utf-8") == "preserve-me"

    completed_overwrite = subprocess.run(
        [
            "bash",
            "scripts/generate-project",
            "--overwrite",
            str(target),
            "cli-occupied",
            "CLI Occupied",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed_overwrite.returncode == 0, completed_overwrite.stderr
    assert not (target / "sentinel.txt").exists()
