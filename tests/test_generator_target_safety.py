"""Generator target-directory safety tests."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from harness.generator.render import generate_project

ROOT = Path(__file__).resolve().parents[1]


def _create_harness_sentinel() -> Path:
    sentinel = ROOT / ".generator-safety-sentinel"
    sentinel.write_text("preserve-harness", encoding="utf-8")
    return sentinel


def _cleanup_harness_sentinel(sentinel: Path) -> None:
    if sentinel.exists():
        sentinel.unlink()


def _assert_harness_metadata_intact() -> None:
    assert (ROOT / ".git").is_dir()
    assert (ROOT / "harness-config.toml").is_file()


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


@pytest.mark.parametrize(
    ("target", "use_overwrite"),
    [
        (".", True),
        (str(ROOT), True),
        (str(ROOT.parent), True),
        (str(ROOT / "nested-target"), True),
    ],
)
def test_generate_rejects_unsafe_harness_overlap(target: str, use_overwrite: bool) -> None:
    sentinel = _create_harness_sentinel()
    nested_target = ROOT / "nested-target"
    nested_target.mkdir(exist_ok=True)
    nested_sentinel = nested_target / "sentinel.txt"
    nested_sentinel.write_text("preserve-nested", encoding="utf-8")

    try:
        command = ["bash", "scripts/generate-project"]
        if use_overwrite:
            command.append("--overwrite")
        command.extend([target, "unsafe-target", "Unsafe Target"])

        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        assert completed.returncode != 0
        assert "Unsafe generation target" in (completed.stderr + completed.stdout)
        assert sentinel.read_text(encoding="utf-8") == "preserve-harness"
        if nested_sentinel.exists():
            assert nested_sentinel.read_text(encoding="utf-8") == "preserve-nested"
        _assert_harness_metadata_intact()
    finally:
        _cleanup_harness_sentinel(sentinel)
        if nested_target.exists():
            shutil.rmtree(nested_target)


def test_generate_rejects_unsafe_overlap_via_python_api() -> None:
    sentinel = _create_harness_sentinel()
    try:
        with pytest.raises(ValueError, match="Unsafe generation target"):
            generate_project(
                ROOT,
                ROOT,
                "self-target",
                "Self Target",
                overwrite=True,
            )
        assert sentinel.read_text(encoding="utf-8") == "preserve-harness"
        _assert_harness_metadata_intact()
    finally:
        _cleanup_harness_sentinel(sentinel)


def test_generate_allows_external_target_with_overwrite(tmp_path: Path) -> None:
    target = tmp_path / "external-overwrite"
    target.mkdir()
    sentinel = target / "sentinel.txt"
    sentinel.write_text("remove-me", encoding="utf-8")

    result = generate_project(
        ROOT,
        target,
        "external-overwrite",
        "External Overwrite",
        overwrite=True,
    )
    assert result.target == target
    assert not sentinel.exists()
    assert (target / "README.md").is_file()
