import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.mixed_derivatives import (
    mixed_derivative_block,
    mixed_derivative_from_potential,
)


def test_tdc_mixed_block_formula_matches_derived_diagonal_matrix() -> None:
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
    mixed = mixed_derivative_block(grad, theta)

    expected = sp.Matrix(
        [
            [1 - alpha * w[0, 0], 0, 0],
            [0, 1 - alpha * w[1, 0], 0],
            [0, 0, 1 - alpha * w[2, 0]],
        ]
    )

    assert sp.simplify(mixed - expected) == sp.zeros(3, 3)


def test_tdc_mixed_block_from_gradient_matches_direct_potential_construction() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )
    grad = gradient_of_potential(phi, w)

    mixed_from_grad = mixed_derivative_block(grad, theta)
    mixed_from_phi = mixed_derivative_from_potential(phi, w, theta)

    assert sp.simplify(mixed_from_grad - mixed_from_phi) == sp.zeros(3, 3)


def test_tdc_mixed_block_depends_on_w_but_not_on_theta() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )
    grad = gradient_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    mixed_str = str(mixed)

    assert "w0" in mixed_str or "w1" in mixed_str or "w2" in mixed_str
    assert "theta0" not in mixed_str
    assert "theta1" not in mixed_str
    assert "theta2" not in mixed_str


def test_tdc_mixed_block_is_not_identity_symbolically() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )
    grad = gradient_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    assert sp.simplify(mixed - sp.eye(3)) != sp.zeros(3, 3)
