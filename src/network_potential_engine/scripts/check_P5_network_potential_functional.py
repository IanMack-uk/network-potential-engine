from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def main() -> None:
    print("P5 network potential functional smoke-check")
    print("Canonical signature (core objects): Φ(w, θ)")
    print("Dependency-map notation: Φ(w ; s , θ)")
    print("Reconciliation used in P5: treat s as part of the parameter bundle, i.e. Φ(w ; s , θ) := Φ(w, \\tilde{θ})")
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

    print("Example model instantiation (repo anchor: symbolic/potential.py):")
    print("Φ_tdc(w, θ) =")
    print(phi)
    print()

    subs: dict[sp.Symbol, sp.Expr] = {
        q: sp.Rational(3, 2),
        alpha: sp.Rational(1, 5),
        c: sp.Rational(1, 2),
        w[0, 0]: sp.Rational(1, 2),
        w[1, 0]: sp.Rational(1, 4),
        w[2, 0]: sp.Rational(1, 8),
        theta[0, 0]: 2,
        theta[1, 0]: 0,
        theta[2, 0]: -1,
    }

    print("Sample point (w, θ) and parameter values:")
    for i in range(n):
        print(f"  w_{i} = {subs[w[i, 0]]}")
    for i in range(n):
        print(f"  θ_{i} = {subs[theta[i, 0]]}")
    print(f"  q = {subs[q]}")
    print(f"  alpha = {subs[alpha]}")
    print(f"  c = {subs[c]}")
    print()

    value = sp.simplify(phi.subs(subs))
    print("Evaluation:")
    print("  Φ_tdc(w, θ) =", value)
    assert value.is_real is True or value.is_real is None
    assert value.is_finite
    print()
    print("P5 network potential functional smoke-check: PASS")


if __name__ == "__main__":
    main()
