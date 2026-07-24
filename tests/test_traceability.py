"""Repository traceability checks for required H0 artifacts and links."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

OBSOLETE_ACTIVE_PLAN_PATH = "docs/exec-plans/active/h0-bootstrap.md"
COMPLETED_PLAN_PATH = "docs/exec-plans/completed/h0-repository-bootstrap.md"
ACTIVE_PLAN_PATH = "docs/exec-plans/active/h0-repository-bootstrap.md"

REQUIRED_PATHS = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "docs/strategy/project-continuum-proposal.md",
    "docs/reference/exports/project-continuum-proposal-v0.3.docx",
    "docs/reference/approved-inputs/h0-repository-bootstrap-approved.md",
    "docs/governance/document-register.md",
    "docs/decisions/adr-0001-h0-repository-bootstrap.md",
    COMPLETED_PLAN_PATH,
    "docs/validation/h0-repository-bootstrap.md",
    "docs/validation/reviews/h0-manus-review-5f772f2.md",
    "docs/validation/reviews/h0-manus-rereview-19f6765.md",
    "docs/validation/reviews/h0-manus-github-evidence-addendum-19f6765.md",
    ".github/ISSUE_TEMPLATE/requirement.md",
    ".github/PULL_REQUEST_TEMPLATE/pull_request_template.md",
    ".github/workflows/ci.yml",
]

APPROVED_BASELINE_SHA256 = (
    "d543f9c3f2e299faa12b2ca7f0513e1f8dee941bf478fc8f339c62daf72cd1c0"  # pragma: allowlist secret
)

OBSOLETE_PATH_EXCLUDE_PREFIXES = (
    "docs/validation/reviews/",
    "docs/reference/approved-inputs/",
    "docs/exec-plans/completed/",
)

LINK_PATTERN = re.compile(
    r"`(?P<backtick>[^`\n]+)`|"
    r"\[[^\]]+\]\((?P<markdown>[^)\s]+)\)"
)


def _iter_active_documents() -> list[Path]:
    documents: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/"):
            continue
        if any(rel.startswith(prefix) for prefix in OBSOLETE_PATH_EXCLUDE_PREFIXES):
            continue
        if path.suffix in {".md", ".toml", ".yaml", ".yml"} or rel == "AGENTS.md":
            documents.append(path)
    return documents


def _extract_linked_paths(content: str) -> set[str]:
    linked: set[str] = set()
    for match in LINK_PATTERN.finditer(content):
        candidate = match.group("backtick") or match.group("markdown")
        if not candidate:
            continue
        candidate = candidate.split("#", 1)[0].strip()
        if candidate.startswith(("http://", "https://", "mailto:")):
            continue
        if candidate.startswith("/"):
            continue
        if not (
            candidate.startswith("docs/")
            or candidate.startswith(".github/")
            or candidate.startswith("reviews/")
            or candidate in {"AGENTS.md", "ARCHITECTURE.md", "architecture-boundaries.toml"}
        ):
            continue
        linked.add(candidate)
    return linked


@pytest.mark.parametrize("relative_path", REQUIRED_PATHS)
def test_required_h0_paths_exist(relative_path: str) -> None:
    assert (ROOT / relative_path).is_file(), f"Missing required path: {relative_path}"


def test_completed_plan_replaced_active_plan() -> None:
    assert (ROOT / COMPLETED_PLAN_PATH).is_file()
    assert not (ROOT / ACTIVE_PLAN_PATH).exists()


def test_agents_md_points_to_completed_plan() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert COMPLETED_PLAN_PATH in agents
    assert ACTIVE_PLAN_PATH not in agents


def test_approved_baseline_hash_matches() -> None:
    import hashlib

    baseline = ROOT / "docs/reference/approved-inputs/h0-repository-bootstrap-approved.md"
    digest = hashlib.sha256(baseline.read_bytes()).hexdigest()
    assert digest == APPROVED_BASELINE_SHA256


def test_no_obsolete_active_plan_path_in_active_documents() -> None:
    offenders: list[str] = []
    for path in _iter_active_documents():
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")
        if OBSOLETE_ACTIVE_PLAN_PATH in content:
            offenders.append(rel)
    assert not offenders, "Obsolete active-plan path found in:\n" + "\n".join(offenders)


def test_validation_dossier_links_all_manus_reports() -> None:
    dossier = (ROOT / "docs/validation/h0-repository-bootstrap.md").read_text(encoding="utf-8")
    for report in (
        "h0-manus-review-5f772f2.md",
        "h0-manus-rereview-19f6765.md",
        "h0-manus-github-evidence-addendum-19f6765.md",
    ):
        assert report in dossier


def test_required_document_links_resolve() -> None:
    missing: list[str] = []
    link_sources = [
        "AGENTS.md",
        "docs/governance/document-register.md",
        "docs/validation/h0-repository-bootstrap.md",
    ]
    for relative_path in link_sources:
        path = ROOT / relative_path
        content = path.read_text(encoding="utf-8")
        for linked in _extract_linked_paths(content):
            if (
                linked.startswith("docs/")
                or linked.startswith(".github/")
                or linked
                in {
                    "AGENTS.md",
                    "ARCHITECTURE.md",
                    "architecture-boundaries.toml",
                }
            ):
                target = ROOT / linked
            elif linked.startswith("reviews/"):
                target = path.parent / linked
            else:
                continue
            if not target.exists():
                missing.append(f"{relative_path} -> {linked}")
    assert not missing, "Broken links:\n" + "\n".join(sorted(missing))


def test_document_register_authority_entries() -> None:
    register = (ROOT / "docs/governance/document-register.md").read_text(encoding="utf-8")
    assert "h0-repository-bootstrap-approved.md" in register
    assert "immutable" in register.lower() or "Immutable" in register
    assert COMPLETED_PLAN_PATH in register
    assert "ready-for-merge" in register
    assert "project-continuum-proposal-v0.3.docx" in register
    assert "Non-authoritative" in register or "non-authoritative" in register
