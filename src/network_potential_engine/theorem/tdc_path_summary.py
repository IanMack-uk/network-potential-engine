from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.theorem.tdc_chain_witness import (
    TDCChainWitness,
    build_tdc_chain_witness,
)
from network_potential_engine.theorem.tdc_region import (
    all_points_in_tdc_region,
)


@dataclass
class TDCPathSummary:
    """
    High-level theorem summary for a sampled TDC path.
    """

    theta_points: list[np.ndarray]
    chain_witness: TDCChainWitness
    all_points_in_region: bool
    path_supports_local_ordering_theorem: bool


def build_tdc_path_summary(
    gradient_fn,
    theta_points: list[np.ndarray] | list[list[float]],
    w0: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    residual_tol: float = 1e-10,
    tol: float = 1e-10,
) -> TDCPathSummary:
    """
    Build a full theorem-facing summary for a sampled TDC path.
    """
    points = [np.asarray(theta, dtype=float).reshape(-1) for theta in theta_points]

    chain_witness = build_tdc_chain_witness(
        gradient_fn=gradient_fn,
        theta_points=points,
        w0=w0,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        residual_tol=residual_tol,
        tol=tol,
    )

    points_in_region = all_points_in_tdc_region(
        points,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        tol=tol,
    )

    return TDCPathSummary(
        theta_points=points,
        chain_witness=chain_witness,
        all_points_in_region=points_in_region,
        path_supports_local_ordering_theorem=(
            points_in_region and chain_witness.chain_consistent
        ),
    )