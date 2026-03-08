from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)


def test_tdc_domain_is_nonempty_via_explicit_point() -> None:
    w, theta = make_symbols(3, 3)

    # Explicit witness point for non-emptiness of the ambient/TDC domain
    subs = {
        w[0, 0]: 0,
        w[1, 0]: 0,
        w[2, 0]: 0,
        theta[0, 0]: 0,
        theta[1, 0]: 0,
        theta[2, 0]: 0,
    }

    q, alpha, c = sp.symbols("q alpha c", real=True)
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    value = phi.subs(subs | {q: 1, alpha: 0, c: 0})
    assert value.is_finite


def test_tdc_potential_is_well_defined_on_sample_numeric_points() -> None:
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
        assert value.is_finite