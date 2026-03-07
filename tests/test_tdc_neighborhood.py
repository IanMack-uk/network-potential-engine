import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.local_scan import scan_pointwise_along_line
from network_potential_engine.theorem.tdc_neighborhood import (
    summarize_tdc_conditions_on_scan,
)


def test_tdc_neighborhood_summary_matches_current_scan() -> None:
    w, theta = make_symbols(3, 3)

    base_q = 1.0
    alpha = 0.2
    coupling = 0.5

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=base_q,
        theta_curvature_weight=alpha,
        coupling_weight=coupling,
    )
    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_block(grad, theta)

    grad_fn = lambdify_matrix(grad, w, theta)
    hess_fn = lambdify_matrix(hess, w, theta)
    mixed_fn = lambdify_matrix(mixed, w, theta)

    theta0 = np.array([0.2, 0.1, 0.0], dtype=float)
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

    summary = summarize_tdc_conditions_on_scan(
        records,
        base_quadratic_weight=base_q,
        theta_curvature_weight=alpha,
    )

    assert summary.curvature_condition_holds_everywhere is True
    assert summary.mixed_block_condition_holds_everywhere is True
    assert summary.all_conditions_hold_everywhere is True

    assert np.isclose(summary.min_curvature_margin, 0.96)
    assert summary.min_mixed_block_margin > 0.93