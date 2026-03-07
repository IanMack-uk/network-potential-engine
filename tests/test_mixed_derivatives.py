import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.mixed_derivatives import (
    mixed_derivative_block,
    mixed_derivative_from_potential,
)


def test_mixed_derivative_has_square_shape_in_bootstrap_case() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    mixed = mixed_derivative_block(grad, theta)

    assert isinstance(mixed, sp.MatrixBase)
    assert mixed.shape == (3, 3)


def test_mixed_derivative_matches_direct_construction() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    mixed_from_grad = mixed_derivative_block(grad, theta)
    mixed_from_phi = mixed_derivative_from_potential(phi, w, theta)

    assert sp.simplify(mixed_from_grad - mixed_from_phi) == sp.zeros(3, 3)


def test_mixed_derivative_is_identity_for_bootstrap_potential() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    mixed = mixed_derivative_block(grad, theta)

    assert sp.simplify(mixed - sp.eye(3)) == sp.zeros(3, 3)
