import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)


def test_theta_dependent_curvature_potential_returns_scalar_expression() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)

    assert isinstance(phi, sp.Expr)


def test_theta_dependent_curvature_potential_uses_expected_symbols() -> None:
    w, theta = make_symbols(3, 3)
    phi = theta_dependent_curvature_potential(w, theta)

    phi_str = str(phi)
    assert "w0" in phi_str
    assert "w1" in phi_str
    assert "w2" in phi_str
    assert "theta0" in phi_str
    assert "theta1" in phi_str
    assert "theta2" in phi_str
