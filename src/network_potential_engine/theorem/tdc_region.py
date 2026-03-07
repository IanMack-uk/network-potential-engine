from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.theorem.tdc_bounds import (
    check_tdc_analytic_bounds,
    tdc_min_curvature_margin,
)


@dataclass
class TDCRegionCheck:
    """
    Membership check for the TDC theorem-ready admissible region

        R = {theta : m(theta) > 0 and alpha * ||theta||_inf / m(theta) <= 1}.
    """

    theta_values: np.ndarray
    min_curvature_margin: float
    theta_infinity_norm: float
    equilibrium_infinity_bound: float
    curvature_region_condition: bool
    mixed_block_region_condition: bool
    in_region: bool


def in_tdc_region(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> TDCRegionCheck:
    """
    Check whether theta lies in the theorem-ready TDC admissible region

        R = {theta : m(theta) > 0 and alpha * ||theta||_inf / m(theta) <= 1}.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)

    min_margin = tdc_min_curvature_margin(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )
    theta_inf = float(np.linalg.norm(theta_arr, ord=np.inf))
    curvature_ok = bool(min_margin > tol)

    if not curvature_ok:
        return TDCRegionCheck(
            theta_values=theta_arr,
            min_curvature_margin=min_margin,
            theta_infinity_norm=theta_inf,
            equilibrium_infinity_bound=float("inf"),
            curvature_region_condition=False,
            mixed_block_region_condition=False,
            in_region=False,
        )

    bound_check = check_tdc_analytic_bounds(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )

    alpha = float(theta_curvature_weight)
    mixed_ok = bool(alpha * bound_check.equilibrium_infinity_bound <= 1.0 + tol)

    return TDCRegionCheck(
        theta_values=theta_arr,
        min_curvature_margin=bound_check.min_curvature_margin,
        theta_infinity_norm=bound_check.theta_infinity_norm,
        equilibrium_infinity_bound=bound_check.equilibrium_infinity_bound,
        curvature_region_condition=True,
        mixed_block_region_condition=mixed_ok,
        in_region=(True and mixed_ok),
    )


def all_points_in_tdc_region(
    theta_points: list[np.ndarray] | list[list[float]],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> bool:
    """
    Return True if every theta point lies in the TDC admissible region.
    """
    return all(
        in_tdc_region(
            theta_values=theta,
            base_quadratic_weight=base_quadratic_weight,
            theta_curvature_weight=theta_curvature_weight,
            tol=tol,
        ).in_region
        for theta in theta_points
    )