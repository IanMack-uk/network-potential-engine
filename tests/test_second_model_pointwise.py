import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.pointwise import check_pointwise_conditions


def test_second_model_pointwise_check_runs_and_returns_shapes() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)
    w0 = np.zeros(3, dtype=float)

    result = check_pointwise_conditions(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta_values=theta_values,
        w0=w0,
    )

    assert result.equilibrium.success is True
    assert result.equilibrium.w_star.shape == (3,)
    assert result.response.hessian_matrix.shape == (3, 3)
    assert result.response.coupling_matrix.shape == (3, 3)
    assert result.response.mixed_block.shape == (3, 3)
    assert result.response.response_matrix.shape == (3, 3)


def test_second_model_pointwise_check_has_symmetric_coupling() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)
    w0 = np.zeros(3, dtype=float)

    result = check_pointwise_conditions(
        gradient_fn=grad_fn,
        hessian_fn=hess_fn,
        mixed_block_fn=mixed_fn,
        theta_values=theta_values,
        w0=w0,
    )

    assert result.is_c_symmetric is True
