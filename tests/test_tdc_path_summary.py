import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_path_summary import (
    build_tdc_path_summary,
)


def test_tdc_path_summary_matches_current_scan_path() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    grad = gradient_of_potential(phi, w)
    grad_fn = lambdify_matrix(grad, w, theta)

    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]
    w0 = np.zeros(3, dtype=float)

    summary = build_tdc_path_summary(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert summary.all_points_in_region is True
    assert summary.chain_witness.all_hypotheses_hold is True
    assert summary.chain_witness.all_observed_orders_hold is True
    assert summary.chain_witness.chain_consistent is True
    assert summary.path_supports_local_ordering_theorem is True