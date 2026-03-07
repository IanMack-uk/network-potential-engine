import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential


def test_gradient_has_column_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    assert isinstance(grad, sp.MatrixBase)
    assert grad.shape == (3, 1)


def test_gradient_contains_expected_symbols() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    grad_str = str(grad)
    assert "theta0" in grad_str
    assert "theta1" in grad_str
    assert "theta2" in grad_str
    assert "w0" in grad_str
    assert "w1" in grad_str
    assert "w2" in grad_str
