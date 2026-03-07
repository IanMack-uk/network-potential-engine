import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.numeric.lambdified import (
    lambdify_scalar,
    lambdify_matrix,
)


def test_lambdify_scalar_returns_float() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)

    phi_fn = lambdify_scalar(phi, w, theta)
    value = phi_fn([1.0, 2.0, 3.0], [0.5, 0.25, -0.5])

    assert isinstance(value, float)


def test_lambdify_gradient_returns_1d_array() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    grad_fn = lambdify_matrix(grad, w, theta)
    value = grad_fn([1.0, 2.0, 3.0], [0.5, 0.25, -0.5])

    assert isinstance(value, np.ndarray)
    assert value.shape == (3,)


def test_lambdify_hessian_returns_2d_array() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    hess_fn = lambdify_matrix(hess, w, theta)
    value = hess_fn([1.0, 2.0, 3.0], [0.5, 0.25, -0.5])

    assert isinstance(value, np.ndarray)
    assert value.shape == (3, 3)
