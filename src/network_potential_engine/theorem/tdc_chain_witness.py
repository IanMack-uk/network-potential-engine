from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.theorem.tdc_local_witness import (
    TDCLocalWitness,
    build_tdc_local_witness,
)


@dataclass
class TDCChainWitness:
    """
    Combined witness for a monotone chain of TDC theta points.

    Attributes
    ----------
    theta_points
        The list of theta points in the chain.
    local_witnesses
        The list of local witnesses for each consecutive segment.
    all_hypotheses_hold
        Whether every consecutive pair satisfies the local theorem hypothesis.
    all_observed_orders_hold
        Whether every consecutive pair exhibits coordinatewise equilibrium ordering.
    chain_consistent
        Whether all local witnesses are consistent across the full chain.
    """

    theta_points: list[np.ndarray]
    local_witnesses: list[TDCLocalWitness]
    all_hypotheses_hold: bool
    all_observed_orders_hold: bool
    chain_consistent: bool


def build_tdc_chain_witness(
    gradient_fn,
    theta_points: list[np.ndarray] | list[list[float]],
    w0: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    residual_tol: float = 1e-10,
    tol: float = 1e-10,
) -> TDCChainWitness:
    """
    Build a full chain witness from consecutive local TDC witnesses.

    Parameters
    ----------
    gradient_fn
        Numerical gradient function F(w, theta).
    theta_points
        Sequence of theta points in order.
    w0
        Initial guess used for both endpoint solves on each segment.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.
    residual_tol
        Residual tolerance for equilibrium solves.
    tol
        Numerical tolerance for order checks.

    Returns
    -------
    TDCChainWitness
        Structured chain witness.
    """
    if len(theta_points) < 2:
        raise ValueError("theta_points must contain at least two points.")

    points = [np.asarray(theta, dtype=float).reshape(-1) for theta in theta_points]
    w0_arr = np.asarray(w0, dtype=float).reshape(-1)

    local_witnesses = [
        build_tdc_local_witness(
            gradient_fn=gradient_fn,
            theta_left=points[i],
            theta_right=points[i + 1],
            w0_left=w0_arr,
            w0_right=w0_arr,
            base_quadratic_weight=base_quadratic_weight,
            theta_curvature_weight=theta_curvature_weight,
            residual_tol=residual_tol,
            tol=tol,
        )
        for i in range(len(points) - 1)
    ]

    all_hypotheses_hold = all(
        witness.theorem_check.theorem_hypothesis_holds
        for witness in local_witnesses
    )
    all_observed_orders_hold = all(
        witness.observed_equilibrium_order_holds
        for witness in local_witnesses
    )

    return TDCChainWitness(
        theta_points=points,
        local_witnesses=local_witnesses,
        all_hypotheses_hold=all_hypotheses_hold,
        all_observed_orders_hold=all_observed_orders_hold,
        chain_consistent=(all_hypotheses_hold and all_observed_orders_hold),
    )