from pathlib import Path

from network_potential_engine.theorem.runner import run_check


def test_runner_artifact_contains_provenance_fields(tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"

    report = run_check(
        "provenance_test",
        lambda: None,
        artifact_mode=True,
        artifact_path=artifact_path,
        tolerances={"tol": 1e-10},
        regime_tag="strict_diag_dom_z_matrix",
        matrix_fingerprint="abc123",
    )

    assert report.passed is True
    assert artifact_path.exists()

    data = artifact_path.read_text(encoding="utf-8")
    assert "timestamp_utc" in data
    assert "git_commit" in data
    assert "python_version" in data
    assert "numpy_version" in data
    assert "platform" in data
    assert "tolerances" in data
    assert "regime_tag" in data
    assert "matrix_fingerprint" in data
