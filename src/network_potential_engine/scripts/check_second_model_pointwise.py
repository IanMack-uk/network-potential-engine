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
from network_potential_engine.theorem.pointwise import check_pointwise_conditions


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

    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)
    w0 = np.zeros(3, dtype=float)

    result = check_pointwise_conditions(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta_values=theta_values,
        w0=w0,
    )

    print("=" * 72)
    print("SECOND MODEL POINTWISE CHECK")
    print("=" * 72)

    print("\nTheta values:")
    print(theta_values)

    print("\nEquilibrium result:")
    print(f"  success        : {result.equilibrium.success}")
    print(f"  message        : {result.equilibrium.message}")
    print(f"  residual_norm  : {result.equilibrium.residual_norm:.6e}")
    print(f"  w_star         : {result.equilibrium.w_star}")

    print("\nCoupling matrix C = -H:")
    print(result.response.coupling_matrix)

    print("\nDiagonal-dominance margins of C:")
    print(result.c_diagonal_dominance_margins)
    print(f"Minimum margin: {result.c_min_diagonal_dominance_margin:.6f}")

    print("\nResponse matrix R = C^{-1} H_{w,theta}:")
    print(result.response.response_matrix)

    print("\nPointwise theorem flags:")
    print(f"  C symmetric                      : {result.is_c_symmetric}")
    print(
        "  C strictly diagonally dominant  : "
        f"{result.is_c_strictly_diagonally_dominant}"
    )
    print(
        "  C has nonpositive off-diagonals : "
        f"{result.has_c_nonpositive_off_diagonals}"
    )
    print(
        "  R entrywise nonnegative         : "
        f"{result.response_is_entrywise_nonnegative}"
    )

    print("\nRaw Hessian H:")
    print(result.response.hessian_matrix)

    print("\nMixed block H_{w,theta}:")
    print(result.response.mixed_block)

    print("\nDone.")


if __name__ == "__main__":
    main()
