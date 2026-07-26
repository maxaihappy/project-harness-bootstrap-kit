"""Residual Continuum reference detection for the harness repository."""

from __future__ import annotations

from pathlib import Path

from harness.reference_policy import (
    find_residual_references,
    load_harness_config,
    provenance_allow_prefixes,
    scan_roots,
)

ROOT = Path(__file__).resolve().parents[1]


def test_no_unintended_residual_references_in_harness() -> None:
    config = load_harness_config(ROOT)
    offenders = find_residual_references(
        ROOT,
        allow_prefixes=provenance_allow_prefixes(config),
        scan_roots_list=scan_roots(config),
    )
    assert not offenders, "Unintended residual references:\n" + "\n".join(offenders)


def test_harness_is_in_configured_scan_roots() -> None:
    config = load_harness_config(ROOT)
    assert "harness/" in scan_roots(config)


def test_unintended_reference_inside_harness_is_detected(tmp_path: Path) -> None:
    harness_dir = tmp_path / "harness"
    harness_dir.mkdir()
    probe = harness_dir / "probe.py"
    probe.write_text('MESSAGE = "unexpected Continuum coupling"\n', encoding="utf-8")

    offenders = find_residual_references(
        tmp_path,
        allow_prefixes=(),
        scan_roots_list=("harness/",),
    )
    assert offenders, "Expected residual reference detection in harness/"
