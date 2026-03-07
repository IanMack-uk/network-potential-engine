from __future__ import annotations

import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.local_scan import scan_pointwise_along_line
from network_potential_engine.theorem.tdc_conditions import check_tdc_conditions


def main() -> None:
    w, theta = make_symbols(3, 3)

    base_q = 1.0
    alpha = 0.2
    coupling = 0.5

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=base_q,
        theta_curvature_weight=alpha,
        coupling_weight=coupling,
    )
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta0 = np.array([0.2, 0.1, 0.0], dtype=float)
    direction = np.array([1.0, 1.0, 1.0], dtype=float)
    t_values = [-0.2, -0.1, 0.0, 0.1, 0.2]
    w0 = np.zeros(3, dtype=float)

    records = scan_pointwise_along_line(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta0=theta0,
        direction=direction,
        t_values=t_values,
        w0=w0,
    )

    print("=" * 72)
    print("TDC CONDITION SCAN")
    print("=" * 72)
    print(f"\nBasepoint theta0: {theta0}")
    print(f"Direction       : {direction}")
    print(f"t-values        : {t_values}")

    overall_ok = True

    for record in records:
        check = check_tdc_conditions(
            theta_values=record.theta,
            w_star=record.pointwise.equilibrium.w_star,
            base_quadratic_weight=base_q,
            theta_curvature_weight=alpha,
        )

        print("-" * 72)
        print(f"t = {record.t:+.3f}")
        print(f"theta(t) = {record.theta}")
        print(f"w*(theta(t)) = {check.w_star}")
        print(f"curvature margins     = {check.curvature_margins}")
        print(f"mixed-block margins   = {check.mixed_block_margins}")
        print(f"curvature condition   = {check.curvature_condition_holds}")
        print(f"mixed-block condition = {check.mixed_block_condition_holds}")
        print(f"all conditions hold   = {check.all_conditions_hold}")

        overall_ok = overall_ok and check.all_conditions_hold

    print("\nSummary:")
    print(f"All sampled sufficient conditions hold: {overall_ok}")
    print("\nDone.")


if __name__ == "__main__":
    main()
