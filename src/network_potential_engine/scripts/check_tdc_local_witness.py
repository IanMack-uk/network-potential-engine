from __future__ import annotations

import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_local_witness import (
    build_tdc_local_witness,
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

    theta_left = np.array([0.2, 0.1, 0.0], dtype=float)
    theta_right = np.array([0.3, 0.2, 0.1], dtype=float)
    w0 = np.zeros(3, dtype=float)

    witness = build_tdc_local_witness(
        gradient_fn=grad_fn,
        theta_left=theta_left,
        theta_right=theta_right,
        w0_left=w0,
        w0_right=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC LOCAL THEOREM WITNESS")
    print("=" * 72)

    print(f"\nLeft endpoint  = {witness.theorem_check.theta_left}")
    print(f"Right endpoint = {witness.theorem_check.theta_right}")
    print(f"Endpoint order holds       : {witness.theorem_check.endpoint_order_holds}")
    print(
        f"Segment in admissible set  : "
        f"{witness.theorem_check.segment_certificate.segment_in_region}"
    )
    print(
        f"Theorem hypothesis holds   : "
        f"{witness.theorem_check.theorem_hypothesis_holds}"
    )

    print(f"\nw*(left)  = {witness.w_left}")
    print(f"w*(right) = {witness.w_right}")
    print(f"delta_w   = {witness.delta_w}")
    print(f"Observed equilibrium order : {witness.observed_equilibrium_order_holds}")
    print(f"Witness consistent         : {witness.witness_consistent}")

    print("\nDone.")


if __name__ == "__main__":
    main()