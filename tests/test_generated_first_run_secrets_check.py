"""First-run and untracked-file secret scanning tests for generated repositories."""

from __future__ import annotations

import subprocess
from pathlib import Path

from harness.generator.render import generate_project
from harness.generator.workflow import (
    OPERATOR_COMMANDS_IN_TARGET,
    run_documented_new_repository_workflow,
    subprocess_env,
)

ROOT = Path(__file__).resolve().parents[1]
FAKE_GITHUB_TOKEN = "ghp_1234567890123456789012345678901234567890"  # pragma: allowlist secret
PRE_COMMIT_COMMANDS = ("git init", "uv lock", "bash scripts/bootstrap")


def _prepare_generated_repository(
    tmp_path: Path,
    project_name: str,
    display_name: str,
) -> Path:
    target = tmp_path / project_name
    generate_project(ROOT, target, project_name, display_name)
    for command in PRE_COMMIT_COMMANDS:
        completed = subprocess.run(
            command,
            cwd=target,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
            env=subprocess_env(),
        )
        assert completed.returncode == 0, (
            f"Setup command failed ({command}):\n{completed.stderr}\n{completed.stdout}"
        )
    return target


def _git_status(target: Path) -> str:
    completed = subprocess.run(
        ["git", "status", "--short"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    return completed.stdout


def _git_diff_index(target: Path) -> str:
    completed = subprocess.run(
        ["git", "diff", "--cached"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    return completed.stdout


def _run_secrets_check(target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", "scripts/secrets-check"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
        env=subprocess_env(),
    )


def _assert_all_files_untracked(target: Path) -> None:
    completed = subprocess.run(
        ["git", "ls-files"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.strip() == "", "Expected no tracked files before first commit"


def test_fresh_generated_repository_has_only_untracked_files(tmp_path: Path) -> None:
    target = _prepare_generated_repository(
        tmp_path,
        "untracked-only-product",
        "Untracked Only Product",
    )
    _assert_all_files_untracked(target)
    assert _git_status(target).strip() != ""


def test_clean_first_run_secret_scan_succeeds_and_scans_files(
    tmp_path: Path,
) -> None:
    target = _prepare_generated_repository(
        tmp_path,
        "first-run-clean-product",
        "First Run Clean Product",
    )
    _assert_all_files_untracked(target)

    completed = _run_secrets_check(target)
    assert completed.returncode == 0, f"{completed.stderr}\n{completed.stdout}"
    assert "no files to check" not in completed.stdout.lower()
    assert "skipped" not in completed.stdout.lower()


def test_untracked_fake_github_token_probe_fails(tmp_path: Path) -> None:
    target = _prepare_generated_repository(
        tmp_path,
        "first-run-probe-product",
        "First Run Probe Product",
    )
    _assert_all_files_untracked(target)
    (target / "probe.txt").write_text(f"{FAKE_GITHUB_TOKEN}\n", encoding="utf-8")

    completed = _run_secrets_check(target)
    assert completed.returncode != 0, completed.stdout
    assert "GitHub Token" in f"{completed.stdout}\n{completed.stderr}"


def test_secret_scan_does_not_stage_or_modify_files(tmp_path: Path) -> None:
    target = _prepare_generated_repository(
        tmp_path,
        "first-run-immutable-product",
        "First Run Immutable Product",
    )
    _assert_all_files_untracked(target)
    status_before = _git_status(target)
    index_before = _git_diff_index(target)
    baseline_before = (target / ".secrets.baseline").read_bytes()

    completed = _run_secrets_check(target)
    assert completed.returncode == 0, f"{completed.stderr}\n{completed.stdout}"

    assert _git_status(target) == status_before
    assert _git_diff_index(target) == index_before
    assert (target / ".secrets.baseline").read_bytes() == baseline_before


def test_post_commit_tracked_file_validation_still_works(tmp_path: Path) -> None:
    target = _prepare_generated_repository(
        tmp_path,
        "post-commit-product",
        "Post Commit Product",
    )

    init_completed = subprocess.run(
        ["git", "add", "-A"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
    )
    assert init_completed.returncode == 0, init_completed.stderr
    commit_completed = subprocess.run(
        ["git", "commit", "-m", "initial"],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
        env={
            **subprocess_env(),
            "GIT_AUTHOR_NAME": "test",
            "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "test",
            "GIT_COMMITTER_EMAIL": "test@example.com",
        },
    )
    assert commit_completed.returncode == 0, commit_completed.stderr

    clean_completed = _run_secrets_check(target)
    assert clean_completed.returncode == 0, f"{clean_completed.stderr}\n{clean_completed.stdout}"

    (target / "probe.txt").write_text(f"{FAKE_GITHUB_TOKEN}\n", encoding="utf-8")
    probe_completed = _run_secrets_check(target)
    assert probe_completed.returncode != 0, probe_completed.stdout
    assert "GitHub Token" in f"{probe_completed.stdout}\n{probe_completed.stderr}"


def test_documented_workflow_exercises_first_run_secret_scan(tmp_path: Path) -> None:
    target = tmp_path / "documented-workflow-product"
    run_documented_new_repository_workflow(
        ROOT,
        target,
        "documented-workflow-product",
        "Documented Workflow Product",
    )
    _assert_all_files_untracked(target)

    completed = _run_secrets_check(target)
    assert completed.returncode == 0, f"{completed.stderr}\n{completed.stdout}"
    assert "no files to check" not in completed.stdout.lower()

    assert list(OPERATOR_COMMANDS_IN_TARGET).index("bash scripts/secrets-check") >= 0
