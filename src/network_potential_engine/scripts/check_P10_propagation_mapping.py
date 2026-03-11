from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def main() -> None:
    print("P10 propagation mapping smoke-check")
    print("Definition: v = G s where G(w,θ) = C(w,θ)^{-1} (when C is invertible)")
    print("Equivalent linear system: C(w,θ) v = s")
    print()

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

    print("Coupling operator:")
    print("C(w, θ) =")
    print(C)
    print()

    G = sp.simplify(C.inv())

    print("Inverse response operator:")
    print("G(w, θ) = C(w, θ)^{-1} =")
    print(G)
    print()

    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    s = sp.Matrix([s1, s2, s3])

    print("Source vector:")
    print("s =")
    print(s)
    print()

    v = sp.simplify(G * s)

    print("Propagated value field:")
    print("v = G s =")
    print(v)
    print()

    residual = sp.simplify(C * v - s)

    print("Consistency check residual: C v - s =")
    print(residual)
    assert residual == sp.zeros(C.rows, 1)
    print()

    print("P10 propagation mapping smoke-check: PASS")


if __name__ == "__main__":
    main()
