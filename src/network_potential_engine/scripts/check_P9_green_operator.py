from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def check_p9_green_operator():
    w, theta = make_symbols(3, 3)

    q, alpha, c = sp.symbols("q alpha c", real=True)
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    H = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(H)
    G = sp.simplify(C.inv())
    left_residual = sp.simplify(C * G - sp.eye(C.rows))
    right_residual = sp.simplify(G * C - sp.eye(C.rows))

    return C, G, left_residual, right_residual


def main() -> None:
    print("P9 Green operator smoke-check")
    print("Definition: Green operator G(w,θ) = C(w,θ)^{-1} (when C is invertible)")
    print()

    C, G, left_residual, right_residual = check_p9_green_operator()

    print("Coupling operator:")
    print("C(w, θ) =")
    print(C)
    print()

    print("Green operator:")
    print("G(w, θ) = C(w, θ)^{-1} =")
    print(G)
    print()

    print("Identity check residual: C*G - I =")
    print(left_residual)
    print()

    print("Identity check residual: G*C - I =")
    print(right_residual)
    assert left_residual == sp.zeros(C.rows, C.cols)
    assert right_residual == sp.zeros(C.rows, C.cols)
    print()

    print("P9 Green operator smoke-check: PASS")


if __name__ == "__main__":
    main()
