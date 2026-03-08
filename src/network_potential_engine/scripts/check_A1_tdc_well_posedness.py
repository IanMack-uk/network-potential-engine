from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import (
    mixed_derivative_from_potential,
)


def check_domain_nonempty() -> None:
    """Exhibit an explicit admissible point."""
    w, theta = make_symbols(3, 3)

    q, alpha, c = sp.symbols("q alpha c", real=True)
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    subs = {
        w[0, 0]: 0,
        w[1, 0]: 0,
        w[2, 0]: 0,
        theta[0, 0]: 0,
        theta[1, 0]: 0,
        theta[2, 0]: 0,
        q: 1,
        alpha: 0,
        c: 0,
    }

    value = sp.simplify(phi.subs(subs))
    assert value.is_finite, "Explicit witness point did not yield a finite potential value."


def check_potential_well_defined_on_sample_points() -> None:
    """Check the TDC potential evaluates finitely on representative sample points."""
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=sp.Rational(3, 2),
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    sample_points = [
        {
            w[0, 0]: 0, w[1, 0]: 0, w[2, 0]: 0,
            theta[0, 0]: 0, theta[1, 0]: 0, theta[2, 0]: 0,
        },
        {
            w[0, 0]: 1, w[1, 0]: -1, w[2, 0]: 2,
            theta[0, 0]: 2, theta[1, 0]: 0, theta[2, 0]: -3,
        },
        {
            w[0, 0]: sp.Rational(1, 3),
            w[1, 0]: sp.Rational(2, 5),
            w[2, 0]: sp.Rational(-4, 7),
            theta[0, 0]: sp.Rational(3, 2),
            theta[1, 0]: sp.Rational(-1, 4),
            theta[2, 0]: sp.Rational(5, 6),
        },
    ]

    for subs in sample_points:
        value = sp.simplify(phi.subs(subs))
        assert value.is_finite, f"Potential not finite at sample point {subs}"


def check_derivative_objects_exist() -> None:
    """Check that F, H, and H_wtheta can all be constructed."""
    w, theta = make_symbols(3, 3)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_from_potential(phi, w, theta)

    assert grad.shape == (3, 1), f"Unexpected gradient shape: {grad.shape}"
    assert hess.shape == (3, 3), f"Unexpected Hessian shape: {hess.shape}"
    assert mixed.shape == (3, 3), f"Unexpected mixed derivative shape: {mixed.shape}"


def check_polynomial_regularity() -> None:
    """Support the A1 TDC claim that the potential is polynomial, hence C^infinity."""
    w, theta = make_symbols(3, 3)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    vars_all = list(w) + list(theta) + [q, alpha, c]
    poly = sp.Poly(sp.expand(phi), *vars_all)
    assert poly is not None, "TDC potential is not polynomial in the expected variables."

    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_from_potential(phi, w, theta)

    for expr in list(grad) + list(hess) + list(mixed):
        assert sp.Poly(sp.expand(expr), *vars_all) is not None, (
            "A derivative object was not polynomial as expected."
        )


def run_all_checks() -> None:
    print("Running A1 well-posedness checks (TDC model)")
    check_domain_nonempty()
    print("✓ domain non-emptiness verified")

    check_potential_well_defined_on_sample_points()
    print("✓ potential well-defined on sample points")

    check_derivative_objects_exist()
    print("✓ derivative objects exist")

    check_polynomial_regularity()
    print("✓ polynomial regularity verified")

    print("A1 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
