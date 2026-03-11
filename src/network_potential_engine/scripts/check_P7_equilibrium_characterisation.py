from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def main() -> None:
    print("P7 equilibrium characterisation smoke-check")
    print("Target statement (interior regime): w* interior local maximiser ⇒ ∇_w Φ(w*, \\tilde{θ}) = 0")
    print("In canonical objects: F(w, θ) := ∇_w Φ(w, θ), so stationarity is F(w*, θ)=0")
    print()

    n = 3
    w, theta = make_symbols(n, n)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    F = gradient_of_potential(phi, w)

    print("Example potential (TDC instantiation):")
    print("Φ_tdc(w, θ) =")
    print(phi)
    print()

    print("Stationarity operator:")
    print("F(w, θ) = ∇_w Φ_tdc(w, θ) =")
    print(F)
    print()

    subs: dict[sp.Symbol, sp.Expr] = {
        q: 1,
        alpha: 0,
        c: 0,
        theta[0, 0]: 2,
        theta[1, 0]: -1,
        theta[2, 0]: 3,
        w[0, 0]: 2,
        w[1, 0]: -1,
        w[2, 0]: 3,
    }

    print("Parameter regime chosen for a simple exact stationarity witness:")
    print("  alpha=0, c=0, q=1 ⇒ Φ(w,θ) = Σ_i θ_i w_i − 1/2 Σ_i w_i^2")
    print("  In this regime, stationarity is w = θ.")
    print()

    print("Witness point:")
    for i in range(n):
        print(f"  θ_{i} = {subs[theta[i, 0]]},   w_{i} = {subs[w[i, 0]]}")
    print()

    residual = sp.simplify(F.subs(subs))
    print("Computed stationarity residual F(w,θ) at witness:")
    print(residual)
    assert residual == sp.zeros(n, 1)
    print()

    print("P7 equilibrium characterisation smoke-check: PASS")


if __name__ == "__main__":
    main()
