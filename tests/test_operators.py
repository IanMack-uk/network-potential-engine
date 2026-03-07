import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.symbolic.operators import (
    coupling_operator_from_hessian,
    response_operator,
)


def test_coupling_operator_is_negative_hessian() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    hess = hessian_of_potential(phi, w)

    coupling = coupling_operator_from_hessian(hess)

    assert isinstance(coupling, sp.MatrixBase)
    assert sp.simplify(coupling + hess) == sp.zeros(3, 3)


def test_response_operator_has_expected_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    coupling = coupling_operator_from_hessian(hess)
    response = response_operator(coupling, mixed)

    assert isinstance(response, sp.MatrixBase)
    assert response.shape == (3, 3)


def test_response_operator_equals_c_inverse_for_bootstrap_case() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    coupling = coupling_operator_from_hessian(hess)
    response = response_operator(coupling, mixed)

    # For the bootstrap potential, H_{w,theta} = I, so R = C^{-1}.
    assert sp.simplify(response - coupling.inv()) == sp.zeros(3, 3)
