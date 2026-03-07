from __future__ import annotations

import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_chain_witness import (
    build_tdc_chain_witness,
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

    print("\nDone.")


if __name__ == "__main__":
    main()
