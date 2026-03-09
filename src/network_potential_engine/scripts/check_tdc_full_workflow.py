from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from network_potential_engine.scripts.check_A1_tdc_well_posedness import (
    run_all_checks as run_a1,
)
from network_potential_engine.scripts.check_A2_tdc_equilibrium_existence import (
    run_all_checks as run_a2,
)
from network_potential_engine.scripts.check_A3a_tdc_equilibrium_regularity import (
    run_all_checks as run_a3_regularity,
)
from network_potential_engine.scripts.check_A3b_tdc_interior_nondegeneracy import (
    run_all_checks as run_a3_interior,
)
from network_potential_engine.scripts.check_B1_tdc_hessian_coupling_identity import (
    run_all_checks as run_b1,
)
from network_potential_engine.scripts.check_B2_tdc_tridiagonal_coupling_structure import (
    run_all_checks as run_b2,
)
from network_potential_engine.scripts.check_C1_tdc_equilibrium_response_identity import (
    run_all_checks as run_c1,
)
from network_potential_engine.scripts.check_D1_tdc_inverse_positivity import (
    run_all_checks as run_d1,
)
from network_potential_engine.scripts.check_D2_tdc_mixed_block_positivity import (
    run_all_checks as run_d2,
)
from network_potential_engine.scripts.check_D3_tdc_response_positivity import (
    run_all_checks as run_d3,
)
from network_potential_engine.scripts.check_E1_tdc_region import run_all_checks as run_e1
from network_potential_engine.scripts.check_E2_tdc_segment_certificate import (
    run_all_checks as run_e2,
)
from network_potential_engine.scripts.check_E3_tdc_local_weak_ordering import (
    run_all_checks as run_e3,
)
from network_potential_engine.scripts.check_S1_motif_cross_partials import (
    run_all_checks as run_s1,
)
from network_potential_engine.scripts.check_S2_row_dominance_tdc import (
    run_all_checks as run_s2,
)
from network_potential_engine.scripts.check_S3_mmatrix_tdc import run_all_checks as run_s3
from network_potential_engine.scripts.check_S1_motif_cross_partials import (
    check_s1_tdc_motif_cross_partials,
)
from network_potential_engine.scripts.check_S2_row_dominance_tdc import (
    check_s2_tdc_row_dominance,
)
from network_potential_engine.scripts.check_S3_mmatrix_tdc import check_s3_tdc_mmatrix
from network_potential_engine.scripts.check_tdc_chain_witness import main as run_chain_witness
from network_potential_engine.scripts.check_tdc_path_summary import main as run_path_summary

from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.theorem.tdc_bounds import check_tdc_analytic_bounds
from network_potential_engine.theorem.tdc_chain_witness import build_tdc_chain_witness
from network_potential_engine.theorem.tdc_conditions import check_tdc_conditions
from network_potential_engine.theorem.tdc_path_summary import build_tdc_path_summary
from network_potential_engine.theorem.tdc_region import in_tdc_region


def _print_section_break(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88 + "\n")


def _run_stage(label: str, fn) -> bool:
    _print_section_break(label)
    try:
        fn()
        print("\nRESULT: PASS")
        return True
    except Exception as exc:
        print(f"\nRESULT: FAIL ({type(exc).__name__}: {exc})")
        return False


def _default_theta_points() -> list[np.ndarray]:
    return [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]


def _build_tdc_gradient_fn(*, n: int, q: float, alpha: float, c: float):
    w, theta = make_symbols(n, n)
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    grad = gradient_of_potential(phi, w)
    return lambdify_matrix(grad, w, theta)


def _print_compact_numeric_chain_summary() -> None:
    """Print a compact numeric summary for the default 5-point TDC chain.

    This is intentionally not the full detailed diagnostic output.
    It reuses the same underlying theorem computations.
    """

    q = 1.0
    alpha = 0.2
    c = 0.5
    n = 3
    tol = 1e-10

    theta_points = _default_theta_points()
    w0 = np.zeros(n, dtype=float)
    grad_fn = _build_tdc_gradient_fn(n=n, q=q, alpha=alpha, c=c)

    summary = build_tdc_path_summary(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
    )
    witness = build_tdc_chain_witness(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
    )

    w_stars: list[np.ndarray] = []
    if witness.local_witnesses:
        w_stars.append(np.asarray(witness.local_witnesses[0].w_left, dtype=float).reshape(-1))
        for lw in witness.local_witnesses:
            w_stars.append(np.asarray(lw.w_right, dtype=float).reshape(-1))

    print("Parameters:")
    print(f"- q={q}")
    print(f"- alpha={alpha}")
    print(f"- c={c}")

    print("\nPer-point compact summary (E1 + D-layer endpoint margins):")
    for i, theta in enumerate(summary.theta_points, start=1):
        region = in_tdc_region(
            theta_values=theta,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
            tol=tol,
        )
        w_star = w_stars[i - 1] if (i - 1) < len(w_stars) else None
        if w_star is not None:
            conditions = check_tdc_conditions(
                theta_values=theta,
                w_star=w_star,
                base_quadratic_weight=q,
                theta_curvature_weight=alpha,
            )
            bounds = check_tdc_analytic_bounds(
                theta_values=theta,
                base_quadratic_weight=q,
                theta_curvature_weight=alpha,
            )
            min_q_alpha_theta = float(np.min(conditions.curvature_margins))
            min_mixed_block = float(np.min(conditions.mixed_block_margins))
            alpha_w_inf_bound = float(alpha * bounds.equilibrium_infinity_bound)
        else:
            min_q_alpha_theta = float("nan")
            min_mixed_block = float("nan")
            alpha_w_inf_bound = float("nan")

        print("-" * 72)
        print(f"Point {i}: theta={theta}")
        print(
            "  E1: in_region="
            f"{region.in_region}, min_curvature_margin={region.min_curvature_margin:.6g}, "
            f"theta_inf={region.theta_infinity_norm:.6g}"
        )
        print(
            "  D:  min(q+alpha*theta_i)="
            f"{min_q_alpha_theta:.6g}, min(1-alpha*w*_i)={min_mixed_block:.6g}, "
            f"alpha*||w*||_inf_bound={alpha_w_inf_bound:.6g}"
        )

    print("\nPer-segment compact summary (E2 + E3):")
    for i, lw in enumerate(witness.local_witnesses, start=1):
        thm = lw.theorem_check
        seg = thm.segment_certificate

        ratio = (
            alpha * seg.segment_max_theta_infinity_norm / seg.segment_min_curvature_margin
            if seg.segment_min_curvature_margin > 0.0
            else float("inf")
        )

        delta_w = np.asarray(lw.delta_w, dtype=float).reshape(-1)
        min_delta = float(np.min(delta_w))
        argmin_delta = int(np.argmin(delta_w))

        print("-" * 72)
        print(f"Segment {i}:")
        print(
            "  E2: segment_in_region="
            f"{seg.segment_in_region}, m_seg={seg.segment_min_curvature_margin:.6g}, "
            f"M_seg={seg.segment_max_theta_infinity_norm:.6g}, alpha*M/m={ratio:.6g}"
        )
        print(
            "  E3: endpoint_order_holds="
            f"{thm.endpoint_order_holds}, hypothesis_holds={thm.theorem_hypothesis_holds}, "
            f"min(delta_w)={min_delta:.6g} at index {argmin_delta}"
        )


def run_full_workflow(*, verbose: bool = False) -> None:
    _print_section_break("S-LAYER EVIDENCE (S1–S3)")

    _print_section_break("S1 — Structural Z-Matrix evidence (TDC)")
    check_s1_tdc_motif_cross_partials(
        artifact_path=Path("docs/artifacts/S1/tdc_motif_cross_partials.json"),
        verbose=verbose,
    )

    _print_section_break("S2 — Structural Diagonal Dominance evidence (TDC)")
    report_s2 = check_s2_tdc_row_dominance(
        verbose=verbose,
        artifact_path=Path("docs/artifacts/S2/tdc_row_dominance_report.json"),
    )
    if verbose:
        print("\nS2 report summary:")
        print(f"- all_rows_strictly_dominant: {report_s2.all_rows_strictly_dominant}")
        print(f"- minimum_dominance_margin: {report_s2.minimum_dominance_margin}")
        print(
            f"- expected_margin_formula_recovered: {report_s2.expected_margin_formula_recovered}"
        )
        print("- wrote artifact: docs/artifacts/S2/tdc_row_dominance_report.json")

    _print_section_break("S3 — Structural M-Matrix evidence (TDC)")
    report_s3 = check_s3_tdc_mmatrix(
        verbose=verbose,
        artifact_path=Path("docs/artifacts/S3/tdc_mmatrix_report.json"),
    )
    if verbose:
        print("\nS3 report summary:")
        print(f"- all_offdiagonals_nonpositive: {report_s3.all_offdiagonals_nonpositive}")
        print(f"- all_rows_strictly_dominant: {report_s3.all_rows_strictly_dominant}")
        print(f"- s3_mmatrix_preconditions_met: {report_s3.s3_mmatrix_preconditions_met}")
        print(
            f"- expected_margin_formula_recovered: {report_s3.expected_margin_formula_recovered}"
        )
        print(f"- inverse_nonnegative_small_n: {report_s3.inverse_nonnegative_small_n}")
        print("- wrote artifact: docs/artifacts/S3/tdc_mmatrix_report.json")

    _print_section_break("A1–E3 CHAIN DIAGNOSTICS (TDC)")

    _print_section_break("TDC PATH SUMMARY (A1–E3 aligned)")
    run_path_summary()

    _print_section_break("TDC CHAIN WITNESS (A1–E3 aligned)")
    run_chain_witness()


def run_trace_all(
    *,
    verbose: bool = False,
    detailed_de: bool = False,
    compact_de: bool = False,
) -> int:
    """Run the entire A1–E3 workflow (including S-layer) as an ordered trace.

    This mode is output-oriented: it calls the existing check routines used by tests.
    It does not change any mathematics.
    """

    ok = True

    ok &= _run_stage("A1 — Well-posedness (TDC)", run_a1)
    ok &= _run_stage("A2 — Equilibrium existence (TDC)", run_a2)
    ok &= _run_stage("A3a — Equilibrium regularity (TDC)", run_a3_regularity)
    ok &= _run_stage("A3b — Interior nondegeneracy (TDC)", run_a3_interior)

    ok &= _run_stage("B1 — Hessian–coupling identity (TDC)", run_b1)
    ok &= _run_stage("B2 — Tridiagonal coupling structure (TDC)", run_b2)

    ok &= _run_stage("S1 — Structural Z-matrix evidence (TDC)", run_s1)
    ok &= _run_stage("S2 — Structural diagonal dominance evidence (TDC)", run_s2)
    ok &= _run_stage("S3 — Structural M-matrix evidence (TDC)", run_s3)

    ok &= _run_stage("C1 — Equilibrium response identity (TDC)", run_c1)

    ok &= _run_stage("D1 — Inverse positivity (TDC)", run_d1)
    ok &= _run_stage("D2 — Mixed-block positivity (TDC)", run_d2)
    ok &= _run_stage("D3 — Response positivity (TDC)", run_d3)

    ok &= _run_stage("E1 — Region checks (TDC)", run_e1)
    ok &= _run_stage("E2 — Segment certificate (TDC)", run_e2)
    ok &= _run_stage("E3 — Local weak ordering (TDC)", run_e3)

    if compact_de:
        ok &= _run_stage(
            "DE COMPACT SUMMARY — 5-point chain (E1/E2/E3 + D-layer endpoint margins)",
            _print_compact_numeric_chain_summary,
        )

    if detailed_de:
        ok &= _run_stage(
            "DE DETAIL — TDC path summary (A1–E3 aligned; includes D-layer numerics)",
            run_path_summary,
        )
        ok &= _run_stage(
            "DE DETAIL — TDC chain witness (A1–E3 aligned; includes D-layer numerics)",
            run_chain_witness,
        )

    _print_section_break("TRACE COMPLETE")
    print(f"Overall result: {'PASS' if ok else 'FAIL'}")

    return 0 if ok else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Run the full TDC workflow and print end-to-end output: "
            "S1–S3 evidence followed by A1–E3 chain diagnostics."
        )
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print stepwise intermediate symbolic calculations for S1/S2/S3.",
    )
    parser.add_argument(
        "--trace-all",
        action="store_true",
        help=(
            "Run all existing check routines A1–E3 in order (including S1–S3) "
            "and print per-stage trace blocks with PASS/FAIL."
        ),
    )
    parser.add_argument(
        "--trace-all-detailed",
        action="store_true",
        help=(
            "When used with --trace-all, also run the detailed DE-style numeric diagnostics "
            "from the path summary and chain witness scripts."
        ),
    )
    parser.add_argument(
        "--trace-all-compact",
        action="store_true",
        help=(
            "When used with --trace-all, also print a compact endpoint/segment numeric "
            "summary for the 5-point chain (key E1/E2/E3 and D-layer margins)."
        ),
    )
    args = parser.parse_args()
    if args.trace_all:
        raise SystemExit(
            run_trace_all(
                verbose=args.verbose,
                detailed_de=args.trace_all_detailed,
                compact_de=args.trace_all_compact,
            )
        )
    run_full_workflow(verbose=args.verbose)
