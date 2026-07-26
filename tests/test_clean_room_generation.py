"""Clean-room generated repository validation for Issue #1."""

from __future__ import annotations

from pathlib import Path

from harness.generator.render import assert_clean_room_references, assert_no_harness_provenance
from harness.generator.workflow import run_documented_new_repository_workflow

ROOT = Path(__file__).resolve().parents[1]


def test_clean_room_generation_passes_validation(tmp_path: Path) -> None:
    target = tmp_path / "clean-room-product"
    run_documented_new_repository_workflow(
        ROOT,
        target,
        "clean-room-product",
        "Clean Room Product",
    )

    provenance_hits = assert_no_harness_provenance(target)
    assert not provenance_hits, f"Harness provenance leaked: {provenance_hits}"

    residual_hits = assert_clean_room_references(target)
    assert not residual_hits, "Residual references:\n" + "\n".join(residual_hits)
