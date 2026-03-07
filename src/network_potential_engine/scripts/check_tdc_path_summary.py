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
    print(f"\nAll sampled points in region     : {summary.all_points_in_region}")
    print(f"All local hypotheses hold        : {summary.chain_witness.all_hypotheses_hold}")
    print(f"All observed equilibrium orders  : {summary.chain_witness.all_observed_orders_hold}")
    print(f"Chain consistent                 : {summary.chain_witness.chain_consistent}")
    print(
        f"Path supports local ordering     : "
        f"{summary.path_supports_local_ordering_theorem}"
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
