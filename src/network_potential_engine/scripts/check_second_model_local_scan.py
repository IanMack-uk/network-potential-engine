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
from network_potential_engine.theorem.local_scan import (
    all_equilibrium_differences_nonnegative,
    all_pointwise_checks_pass,
    equilibrium_differences,
    minimum_scan_margin,
    scan_pointwise_along_line,
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
    diffs = equilibrium_differences(records)

    print("=" * 72)
    print("SECOND MODEL LOCAL SCAN CHECK")
    print("=" * 72)
    print(f"\nBasepoint theta0: {theta0}")
    print(f"Direction       : {direction}")
    print(f"t-values        : {t_values}")

    print("\nPer-sample results:")
    for record in records:
        check = record.pointwise
        print("-" * 72)
        print(f"t = {record.t:+.3f}")
        print(f"theta(t) = {record.theta}")
        print(f"w*(theta(t)) = {check.equilibrium.w_star}")
        print(f"success  = {check.equilibrium.success}")
        print(f"residual = {check.equilibrium.residual_norm:.6e}")
        print(f"min DD margin = {check.c_min_diagonal_dominance_margin:.6f}")
        print(f"C symmetric = {check.is_c_symmetric}")
        print(f"C SDD       = {check.is_c_strictly_diagonally_dominant}")
        print(f"C Z-pattern = {check.has_c_nonpositive_off_diagonals}")
        print(f"R >= 0      = {check.response_is_entrywise_nonnegative}")

    print("\nConsecutive equilibrium differences:")
    for diff in diffs:
        print("-" * 72)
        print(f"t: {diff.t_left:+.3f} -> {diff.t_right:+.3f}")
        print(f"delta_theta = {diff.delta_theta}")
        print(f"delta_w     = {diff.delta_w}")
        print(f"delta_w >= 0: {diff.delta_w_is_entrywise_nonnegative}")

    print("\nSummary:")
    print(f"All sampled pointwise checks pass      : {all_pointwise_checks_pass(records)}")
    print(
        "All consecutive equilibrium differences >= 0: "
        f"{all_equilibrium_differences_nonnegative(records)}"
    )
    print(f"Minimum scan margin                    : {minimum_scan_margin(records):.6f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
