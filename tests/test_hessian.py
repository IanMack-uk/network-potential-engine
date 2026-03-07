import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import (
    hessian_of_potential,
    jacobian_of_gradient,
)


def test_hessian_has_square_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    assert isinstance(hess, sp.MatrixBase)
    assert hess.shape == (3, 3)


def test_hessian_is_symmetric() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    assert sp.simplify(hess - hess.T) == sp.zeros(3, 3)


def test_hessian_matches_jacobian_of_gradient() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    hess = hessian_of_potential(phi, w)
    jac = jacobian_of_gradient(grad, w)

    assert sp.simplify(hess - jac) == sp.zeros(3, 3)
