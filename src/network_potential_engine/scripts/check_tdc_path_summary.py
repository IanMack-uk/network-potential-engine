from __future__ import annotations

import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_path_summary import (
    build_tdc_path_summary,
)
from network_potential_engine.theorem.tdc_region import (
    in_tdc_region,
)


def main() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    grad = gradient_of_potential(phi, w)
    grad_fn = lambdify_matrix(grad, w, theta)

    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]
    w0 = np.zeros(3, dtype=float)

    summary = build_tdc_path_summary(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC PATH SUMMARY")
    print("=" * 72)

    print("LEGACY OUTPUT (old-pipeline style)")
    print("=" * 72)
    print(f"\nAll sampled points in region     : {summary.all_points_in_region}")
    print(
        f"All local hypotheses hold        : "
        f"{summary.chain_witness.all_hypotheses_hold}"
    )
    print(
        f"All observed equilibrium orders  : "
        f"{summary.chain_witness.all_observed_orders_hold}"
    )
    print(f"Chain consistent                 : {summary.chain_witness.chain_consistent}")
    print(
        f"Path supports local ordering     : "
        f"{summary.path_supports_local_ordering_theorem}"
    )

    print("\n" + "=" * 72)
    print("NEW PIPELINE DETAIL (A1–E3 aligned diagnostics)")
    print("=" * 72)
    print("Parameters:")
    print("  base_quadratic_weight (q)   : 1.0")
    print("  theta_curvature_weight (α)  : 0.2")
    print("  coupling_weight (c)         : 0.5")

    q = 1.0
    alpha = 0.2
    tol = 1e-10

    region_checks = [
        in_tdc_region(
            theta_values=theta,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
            tol=tol,
        )
        for theta in summary.theta_points
    ]

    print("\nPer-point region checks (E1):")
    for i, check in enumerate(region_checks, start=1):
        print("-" * 72)
        print(f"Point {i}")
        print(f"theta                 : {check.theta_values}")
        print(f"in_region              : {check.in_region}")
        print(f"min_curvature_margin   : {check.min_curvature_margin:.6g}")
        print(f"theta_infinity_norm    : {check.theta_infinity_norm:.6g}")
        print(f"equilibrium_inf_bound  : {check.equilibrium_infinity_bound:.6g}")
        print(
            "alpha * equilibrium_inf_bound : "
            f"{alpha * check.equilibrium_infinity_bound:.6g}"
        )

    min_region_margin = float(min(c.min_curvature_margin for c in region_checks))
    max_alpha_equilibrium_bound = float(
        max(alpha * c.equilibrium_infinity_bound for c in region_checks)
    )

    print("\nPer-segment certificate checks (E2) and hypotheses (E3):")
    max_segment_ratio = -float("inf")
    min_segment_mseg = float("inf")
    max_segment_Mseg = -float("inf")

    for i, local_witness in enumerate(summary.chain_witness.local_witnesses, start=1):
        thm = local_witness.theorem_check
        seg = thm.segment_certificate
        if seg.segment_min_curvature_margin > 0.0:
            ratio = alpha * seg.segment_max_theta_infinity_norm / seg.segment_min_curvature_margin
        else:
            ratio = float("inf")

        max_segment_ratio = max(max_segment_ratio, ratio)
        min_segment_mseg = min(min_segment_mseg, seg.segment_min_curvature_margin)
        max_segment_Mseg = max(max_segment_Mseg, seg.segment_max_theta_infinity_norm)

        print("-" * 72)
        print(f"Segment {i}")
        print(f"endpoint_order_holds   : {thm.endpoint_order_holds}")
        print(f"segment_in_region      : {seg.segment_in_region}")
        print(f"theorem_hypothesis      : {thm.theorem_hypothesis_holds}")
        print(f"m_seg                  : {seg.segment_min_curvature_margin:.6g}")
        print(f"M_seg                  : {seg.segment_max_theta_infinity_norm:.6g}")
        print(f"alpha * M_seg / m_seg   : {ratio:.6g}")

    print("\nAggregate tightest margins:")
    print(f"min min_curvature_margin over points      : {min_region_margin:.6g}")
    print(f"max alpha*equilibrium_inf_bound over points: {max_alpha_equilibrium_bound:.6g}")
    print(f"min m_seg over segments                   : {min_segment_mseg:.6g}")
    print(f"max M_seg over segments                   : {max_segment_Mseg:.6g}")
    print(f"max alpha*M_seg/m_seg over segments       : {max_segment_ratio:.6g}")

    print("\nDone.")


if __name__ == "__main__":
    main()
