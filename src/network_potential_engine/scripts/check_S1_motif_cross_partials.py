from __future__ import annotations

from pathlib import Path

import sympy as sp

from network_potential_engine.symbolic.motif_analysis import (
    build_cross_partial_report_for_groups,
    decompose_tdc_into_admissible_grammar_terms,
    write_report_json,
)
from network_potential_engine.symbolic.symbols import make_symbols


def _nonzero_offdiag_entries(entries: list) -> list:
    return [e for e in entries if e.coupling_entry != "0"]


def check_s1_tdc_motif_cross_partials(
    *,
    artifact_path: str | Path,
    verbose: bool = False,
):
    w, theta = make_symbols(5, 5)

    groups = decompose_tdc_into_admissible_grammar_terms(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    report = build_cross_partial_report_for_groups(
        model="tdc",
        groups=groups,
        w=w,
        theta=theta,
    )

    print("S1 admissible-grammar cross-partial report (TDC)")
    print(f"- groups: {[g.group_id for g in groups]}")
    print(f"- aggregated_is_zmatrix: {report.aggregated_is_zmatrix}")

    if verbose:
        print("- aggregated_off_diagonal_entries (nonzero only):")
        for e in _nonzero_offdiag_entries(report.aggregated_off_diagonal_entries):
            print(
                f"  (i={e.i}, j={e.j}) H_ij={e.hessian_entry} ({e.hessian_sign}), "
                f"C_ij={e.coupling_entry} ({e.coupling_sign})"
            )

        print("- per-group off_diagonal_entries (nonzero only):")
        for g in report.groups:
            nonzero = _nonzero_offdiag_entries(g.off_diagonal_entries)
            if not nonzero:
                continue
            print(f"  group_id={g.group_id}, taxonomy_class={g.taxonomy_class}")
            for e in nonzero:
                print(
                    f"    (i={e.i}, j={e.j}) H_ij={e.hessian_entry} ({e.hessian_sign}), "
                    f"C_ij={e.coupling_entry} ({e.coupling_sign})"
                )

    write_report_json(report, artifact_path)
    print(f"- wrote artifact: {artifact_path}")

    return report


def run_all_checks() -> None:
    artifact_path = Path("docs/artifacts/S1/tdc_motif_cross_partials.json")
    check_s1_tdc_motif_cross_partials(artifact_path=artifact_path)


if __name__ == "__main__":
    run_all_checks()
