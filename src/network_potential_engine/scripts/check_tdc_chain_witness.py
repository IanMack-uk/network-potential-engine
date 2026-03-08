from __future__ import annotations

import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_bounds import (
    check_tdc_analytic_bounds,
)
from network_potential_engine.theorem.tdc_chain_witness import (
    build_tdc_chain_witness,
)
from network_potential_engine.theorem.tdc_conditions import (
    check_tdc_conditions,
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

    witness = build_tdc_chain_witness(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC CHAIN WITNESS")
    print("=" * 72)
    print("LEGACY OUTPUT (old-pipeline style)")
    print("=" * 72)

    for i, local_witness in enumerate(witness.local_witnesses, start=1):
        print("-" * 72)
        print(f"Segment {i}")
        print(f"left endpoint   = {local_witness.theorem_check.theta_left}")
        print(f"right endpoint  = {local_witness.theorem_check.theta_right}")
        print(
            f"hypothesis holds = {local_witness.theorem_check.theorem_hypothesis_holds}"
        )
        print(f"w*(left)        = {local_witness.w_left}")
        print(f"w*(right)       = {local_witness.w_right}")
        print(f"delta_w         = {local_witness.delta_w}")
        print(
            f"observed order   = {local_witness.observed_equilibrium_order_holds}"
        )
        print(f"witness consistent = {local_witness.witness_consistent}")

    print("\nSummary:")
    print(f"All hypotheses hold    : {witness.all_hypotheses_hold}")
    print(f"All observed orders    : {witness.all_observed_orders_hold}")
    print(f"Chain consistent       : {witness.chain_consistent}")

    print("\n" + "=" * 72)
    print("NEW PIPELINE DETAIL (A1–E3 aligned diagnostics)")
    print("=" * 72)
    print("Parameters:")
    print("  base_quadratic_weight (q)   : 1.0")
    print("  theta_curvature_weight (α)  : 0.2")
    print("  coupling_weight (c)         : 0.5")

    q = 1.0
    alpha = 0.2

    for i, local_witness in enumerate(witness.local_witnesses, start=1):
        thm = local_witness.theorem_check
        seg = thm.segment_certificate
        left = thm.theta_left
        right = thm.theta_right

        left_region = in_tdc_region(
            theta_values=left,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )
        right_region = in_tdc_region(
            theta_values=right,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )

        left_bounds = check_tdc_analytic_bounds(
            theta_values=left,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )
        right_bounds = check_tdc_analytic_bounds(
            theta_values=right,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )

        left_conditions = check_tdc_conditions(
            theta_values=left,
            w_star=local_witness.w_left,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )
        right_conditions = check_tdc_conditions(
            theta_values=right,
            w_star=local_witness.w_right,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
        )

        delta_w = np.asarray(local_witness.delta_w, dtype=float).reshape(-1)
        min_delta = float(np.min(delta_w))
        argmin_delta = int(np.argmin(delta_w))

        print("-" * 72)
        print(f"Segment {i} diagnostics")
        print(f"E3 endpoint order holds         : {thm.endpoint_order_holds}")
        print(f"E1 left endpoint in region      : {left_region.in_region}")
        print(f"E1 right endpoint in region     : {right_region.in_region}")
        print(f"E2 segment certified in region  : {seg.segment_in_region}")
        print(f"E3 theorem hypothesis holds     : {thm.theorem_hypothesis_holds}")
        print("\nE1 region margins (left endpoint):")
        print(f"  min_curvature_margin          : {left_region.min_curvature_margin:.6g}")
        print(f"  theta_infinity_norm           : {left_region.theta_infinity_norm:.6g}")
        print(
            "  alpha * equilibrium_inf_bound : "
            f"{alpha * left_region.equilibrium_infinity_bound:.6g}"
        )
        print("E1 region margins (right endpoint):")
        print(f"  min_curvature_margin          : {right_region.min_curvature_margin:.6g}")
        print(f"  theta_infinity_norm           : {right_region.theta_infinity_norm:.6g}")
        print(
            "  alpha * equilibrium_inf_bound : "
            f"{alpha * right_region.equilibrium_infinity_bound:.6g}"
        )
        print("\nE2 segment certificate quantities:")
        print(
            "  m_seg = segment_min_curvature_margin : "
            f"{seg.segment_min_curvature_margin:.6g}"
        )
        print(
            "  M_seg = segment_max_theta_inf_norm   : "
            f"{seg.segment_max_theta_infinity_norm:.6g}"
        )
        if seg.segment_min_curvature_margin > 0.0:
            ratio = alpha * seg.segment_max_theta_infinity_norm / seg.segment_min_curvature_margin
        else:
            ratio = float("inf")
        print(f"  alpha * M_seg / m_seg                : {ratio:.6g}")
        print(
            "\nD-layer sufficient conditions (numeric, at endpoints):"
        )
        print("  Left endpoint:")
        print(f"    min(q + α θ_i)            : {float(np.min(left_conditions.curvature_margins)):.6g}")
        print(f"    min(1 - α w*_i)           : {float(np.min(left_conditions.mixed_block_margins)):.6g}")
        print(f"    all conditions hold       : {left_conditions.all_conditions_hold}")
        print(f"    analytic ||w*||_inf bound  : {left_bounds.equilibrium_infinity_bound:.6g}")
        print(
            "    analytic α||w*||_inf bound : "
            f"{alpha * left_bounds.equilibrium_infinity_bound:.6g}"
        )
        print("  Right endpoint:")
        print(f"    min(q + α θ_i)            : {float(np.min(right_conditions.curvature_margins)):.6g}")
        print(f"    min(1 - α w*_i)           : {float(np.min(right_conditions.mixed_block_margins)):.6g}")
        print(f"    all conditions hold       : {right_conditions.all_conditions_hold}")
        print(f"    analytic ||w*||_inf bound  : {right_bounds.equilibrium_infinity_bound:.6g}")
        print(
            "    analytic α||w*||_inf bound : "
            f"{alpha * right_bounds.equilibrium_infinity_bound:.6g}"
        )
        print("\nObserved conclusion (numeric):")
        print(
            f"  min(delta_w) = {min_delta:.6g} at index {argmin_delta}"
        )
        print(
            f"  delta_w >= 0 (tol)           : {local_witness.observed_equilibrium_order_holds}"
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
