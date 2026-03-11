from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def main() -> None:
    print("P8 coupling operator smoke-check")
    print("Definitions: H(w,θ)=∇²_{ww}Φ(w,θ),  C(w,θ)=−H(w,θ)")
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

    print("Example potential (TDC instantiation):")
    print("Φ_tdc(w, θ) =")
    print(phi)
    print()

    H = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(H)

    print("State Hessian:")
    print("H(w, θ) =")
    print(H)
    print()

    print("Coupling operator:")
    print("C(w, θ) = −H(w, θ) =")
    print(C)
    print()

    residual = sp.simplify(C + H)
    print("Identity check residual: C + H =")
    print(residual)
    assert residual == sp.zeros(*H.shape)
    print()

    print("P8 coupling operator smoke-check: PASS")


if __name__ == "__main__":
    main()
