import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_chain_witness import (
    build_tdc_chain_witness,
)


def test_tdc_chain_witness_matches_current_scan_chain() -> None:
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

    witness = build_tdc_chain_witness(
        gradient_fn=grad_fn,
        theta_points=theta_points,
        w0=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert len(witness.local_witnesses) == 4
    assert witness.all_hypotheses_hold is True
    assert witness.all_observed_orders_hold is True
    assert witness.chain_consistent is True

    for local_witness in witness.local_witnesses:
        assert local_witness.theorem_check.theorem_hypothesis_holds is True
        assert local_witness.observed_equilibrium_order_holds is True
        assert local_witness.witness_consistent is True
        assert np.all(local_witness.delta_w >= 0.0)


def test_tdc_chain_witness_requires_at_least_two_points() -> None:
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

    theta_points = [np.array([0.2, 0.1, 0.0], dtype=float)]
    w0 = np.zeros(3, dtype=float)

    try:
        build_tdc_chain_witness(
            gradient_fn=grad_fn,
            theta_points=theta_points,
            w0=w0,
            base_quadratic_weight=1.0,
            theta_curvature_weight=0.2,
        )
    except ValueError as exc:
        assert "at least two points" in str(exc)
    else:
        raise AssertionError("Expected ValueError for a chain with fewer than two points.")