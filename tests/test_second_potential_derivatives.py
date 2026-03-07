import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block


def test_second_potential_gradient_has_column_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    assert isinstance(grad, sp.MatrixBase)
    assert grad.shape == (3, 1)


def test_second_potential_hessian_has_square_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    assert isinstance(hess, sp.MatrixBase)
    assert hess.shape == (3, 3)


def test_second_potential_hessian_is_symmetric() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    assert sp.simplify(hess - hess.T) == sp.zeros(3, 3)


def test_second_potential_hessian_depends_on_theta() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    hess_str = str(hess)
    assert "theta0" in hess_str or "theta1" in hess_str or "theta2" in hess_str


def test_second_potential_mixed_block_has_square_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    assert isinstance(mixed, sp.MatrixBase)
    assert mixed.shape == (3, 3)


def test_second_potential_mixed_block_is_not_identity() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    assert sp.simplify(mixed - sp.eye(3)) != sp.zeros(3, 3)
