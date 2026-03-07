import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.theorem.tdc_local_witness import (
    build_tdc_local_witness,
    is_equilibrium_ordered,
)


def test_is_equilibrium_ordered_detects_monotone_pair() -> None:
    w_left = np.array([0.1, 0.2, 0.3], dtype=float)
    w_right = np.array([0.2, 0.2, 0.4], dtype=float)

    assert is_equilibrium_ordered(w_left, w_right) is True


def test_is_equilibrium_ordered_detects_nonmonotone_pair() -> None:
    w_left = np.array([0.1, 0.2, 0.3], dtype=float)
    w_right = np.array([0.2, 0.1, 0.4], dtype=float)

    assert is_equilibrium_ordered(w_left, w_right) is False


def test_tdc_local_witness_matches_current_scan_step() -> None:
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

    theta_left = np.array([0.2, 0.1, 0.0], dtype=float)
    theta_right = np.array([0.3, 0.2, 0.1], dtype=float)
    w0 = np.zeros(3, dtype=float)

    witness = build_tdc_local_witness(
        gradient_fn=grad_fn,
        theta_left=theta_left,
        theta_right=theta_right,
        w0_left=w0,
        w0_right=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert witness.theorem_check.theorem_hypothesis_holds is True
    assert witness.observed_equilibrium_order_holds is True
    assert witness.witness_consistent is True
    assert witness.delta_w.shape == (3,)
    assert np.all(witness.delta_w >= 0.0)


def test_tdc_local_witness_fails_consistency_when_endpoint_order_fails() -> None:
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

    theta_left = np.array([0.2, 0.1, 0.0], dtype=float)
    theta_right = np.array([0.1, 0.2, 0.0], dtype=float)
    w0 = np.zeros(3, dtype=float)

    witness = build_tdc_local_witness(
        gradient_fn=grad_fn,
        theta_left=theta_left,
        theta_right=theta_right,
        w0_left=w0,
        w0_right=w0,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert witness.theorem_check.theorem_hypothesis_holds is False
    assert witness.witness_consistent is False