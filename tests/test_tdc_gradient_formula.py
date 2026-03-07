import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential


def test_tdc_gradient_formula_matches_derived_components() -> None:
    w, theta = make_symbols(3, 3)

    q = sp.Integer(1)
    alpha = sp.Rational(1, 5)
    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    grad = gradient_of_potential(phi, w)

    expected = sp.Matrix(
        [
            theta[0, 0] - (q + alpha * theta[0, 0] + c) * w[0, 0] + c * w[1, 0],
            theta[1, 0]
            + c * w[0, 0]
            - (q + alpha * theta[1, 0] + 2 * c) * w[1, 0]
            + c * w[2, 0],
            theta[2, 0] + c * w[1, 0] - (q + alpha * theta[2, 0] + c) * w[2, 0],
        ]
    )

    assert sp.simplify(grad - expected) == sp.zeros(3, 1)


def test_tdc_gradient_has_affine_form_theta_minus_c_theta_w() -> None:
    w, theta = make_symbols(3, 3)

    q = sp.Integer(1)
    alpha = sp.Rational(1, 5)
    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    grad = gradient_of_potential(phi, w)

    c_theta = sp.Matrix(
        [
            [q + alpha * theta[0, 0] + c, -c, 0],
            [-c, q + alpha * theta[1, 0] + 2 * c, -c],
            [0, -c, q + alpha * theta[2, 0] + c],
        ]
    )

    expected = theta - c_theta * w

    assert sp.simplify(grad - expected) == sp.zeros(3, 1)
