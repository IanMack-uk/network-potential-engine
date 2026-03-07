import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian


def test_tdc_hessian_formula_matches_derived_matrix() -> None:
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
    hess = hessian_of_potential(phi, w)

    expected = sp.Matrix(
        [
            [-(q + alpha * theta[0, 0] + c), c, 0],
            [c, -(q + alpha * theta[1, 0] + 2 * c), c],
            [0, c, -(q + alpha * theta[2, 0] + c),],
        ]
    )

    assert sp.simplify(hess - expected) == sp.zeros(3, 3)


def test_tdc_coupling_operator_equals_minus_hessian() -> None:
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
    hess = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hess)

    expected_coupling = sp.Matrix(
        [
            [q + alpha * theta[0, 0] + c, -c, 0],
            [-c, q + alpha * theta[1, 0] + 2 * c, -c],
            [0, -c, q + alpha * theta[2, 0] + c],
        ]
    )

    assert sp.simplify(coupling - expected_coupling) == sp.zeros(3, 3)
    assert sp.simplify(coupling + hess) == sp.zeros(3, 3)


def test_tdc_hessian_depends_on_theta_but_not_on_w() -> None:
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
    hess = hessian_of_potential(phi, w)

    hess_str = str(hess)

    assert "theta0" in hess_str or "theta1" in hess_str or "theta2" in hess_str
    assert "w0" not in hess_str
    assert "w1" not in hess_str
    assert "w2" not in hess_str
