import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.numeric.equilibrium import solve_equilibrium
from network_potential_engine.numeric.response import compute_response


def test_compute_response_returns_expected_shapes() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta_values = np.array([0.5, 0.25, -0.5], dtype=float)
    w0 = np.zeros(3, dtype=float)

    eq_result = solve_equilibrium(grad_fn, theta_values, w0)
    response_result = compute_response(
        hess_fn,
        mixed_fn,
        eq_result.w_star,
        theta_values,
    )

    assert response_result.response_matrix.shape == (3, 3)
    assert response_result.hessian_matrix.shape == (3, 3)
    assert response_result.coupling_matrix.shape == (3, 3)
    assert response_result.mixed_block.shape == (3, 3)


def test_compute_response_uses_c_equals_minus_h() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta_values = np.array([0.5, 0.25, -0.5], dtype=float)
    w0 = np.zeros(3, dtype=float)

    eq_result = solve_equilibrium(grad_fn, theta_values, w0)
    response_result = compute_response(
        hess_fn,
        mixed_fn,
        eq_result.w_star,
        theta_values,
    )

    assert np.allclose(
        response_result.coupling_matrix,
        -response_result.hessian_matrix,
    )


def test_compute_response_matches_inverse_formula_in_bootstrap_case() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta_values = np.array([0.5, 0.25, -0.5], dtype=float)
    w0 = np.zeros(3, dtype=float)

    eq_result = solve_equilibrium(grad_fn, theta_values, w0)
    response_result = compute_response(
        hess_fn,
        mixed_fn,
        eq_result.w_star,
        theta_values,
    )

    expected = np.linalg.inv(response_result.coupling_matrix) @ response_result.mixed_block

    assert np.allclose(response_result.response_matrix, expected)
