import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.local_scan import (
    all_equilibrium_differences_nonnegative,
    all_pointwise_checks_pass,
    equilibrium_differences,
    minimum_scan_margin,
    scan_pointwise_along_line,
)


def test_scan_pointwise_along_line_returns_records() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta0 = np.array([0.5, 0.25, -0.5], dtype=float)
    direction = np.array([1.0, 0.0, 0.0], dtype=float)
    t_values = [-0.1, 0.0, 0.1]
    w0 = np.zeros(3, dtype=float)

    records = scan_pointwise_along_line(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta0=theta0,
        direction=direction,
        t_values=t_values,
        w0=w0,
    )

    assert len(records) == 3
    assert np.allclose(records[0].theta, np.array([0.4, 0.25, -0.5]))
    assert np.allclose(records[1].theta, np.array([0.5, 0.25, -0.5]))
    assert np.allclose(records[2].theta, np.array([0.6, 0.25, -0.5]))


def test_all_pointwise_checks_pass_for_bootstrap_scan() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta0 = np.array([0.5, 0.25, -0.5], dtype=float)
    direction = np.array([1.0, 1.0, 1.0], dtype=float)
    t_values = [-0.1, 0.0, 0.1]
    w0 = np.zeros(3, dtype=float)

    records = scan_pointwise_along_line(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta0=theta0,
        direction=direction,
        t_values=t_values,
        w0=w0,
    )

    assert all_pointwise_checks_pass(records) is True
    assert np.isclose(minimum_scan_margin(records), 1.0)


def test_equilibrium_differences_are_entrywise_nonnegative_for_positive_direction() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta0 = np.array([0.5, 0.25, -0.5], dtype=float)
    direction = np.array([1.0, 1.0, 1.0], dtype=float)
    t_values = [-0.2, -0.1, 0.0, 0.1, 0.2]
    w0 = np.zeros(3, dtype=float)

    records = scan_pointwise_along_line(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta0=theta0,
        direction=direction,
        t_values=t_values,
        w0=w0,
    )

    diffs = equilibrium_differences(records)

    assert len(diffs) == 4
    assert all_equilibrium_differences_nonnegative(records) is True

    for diff in diffs:
        assert diff.delta_w.shape == (3,)
        assert diff.delta_w_is_entrywise_nonnegative is True
