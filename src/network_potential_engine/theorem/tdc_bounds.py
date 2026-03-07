from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class TDCBoundCheck:
    """
    Analytic bound summary for the TDC local ordering theorem.

    Attributes
    ----------
    theta_values
        Theta vector at which the bounds are evaluated.
    min_curvature_margin
        The minimum diagonal-dominance / curvature margin
            min_i (q + alpha * theta_i).
    inverse_infinity_bound
        The analytic bound
            ||C(theta)^(-1)||_inf <= 1 / min_curvature_margin.
    theta_infinity_norm
        The norm ||theta||_inf.
    equilibrium_infinity_bound
        The analytic bound
            ||w*(theta)||_inf <= ||theta||_inf / min_curvature_margin.
    mixed_block_condition_bound_holds
        Whether the analytic equilibrium bound is strong enough to imply
            1 - alpha * w_i^*(theta) >= 0
        for all i.
    """

    theta_values: np.ndarray
    min_curvature_margin: float
    inverse_infinity_bound: float
    theta_infinity_norm: float
    equilibrium_infinity_bound: float
    mixed_block_condition_bound_holds: bool


def tdc_min_curvature_margin(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> float:
    """
    Compute the minimum curvature margin

        min_i (q + alpha * theta_i).

    Parameters
    ----------
    theta_values
        Theta vector.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.

    Returns
    -------
    float
        Minimum curvature margin.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    q = float(base_quadratic_weight)
    alpha = float(theta_curvature_weight)

    margins = q + alpha * theta_arr
    return float(np.min(margins))


def tdc_inverse_infinity_bound(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> float:
    """
    Compute the analytic inverse bound

        ||C(theta)^(-1)||_inf <= 1 / min_i (q + alpha * theta_i).

    Parameters
    ----------
    theta_values
        Theta vector.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.

    Returns
    -------
    float
        Analytic infinity-norm bound for C(theta)^(-1).
    """
    min_margin = tdc_min_curvature_margin(
        theta_values,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )

    if min_margin <= 0.0:
        raise ValueError(
            "Inverse infinity bound is only valid when the minimum curvature margin is positive."
        )

    return 1.0 / min_margin


def tdc_equilibrium_infinity_bound(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> float:
    """
    Compute the analytic equilibrium bound

        ||w*(theta)||_inf <= ||theta||_inf / min_i (q + alpha * theta_i).

    Parameters
    ----------
    theta_values
        Theta vector.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.

    Returns
    -------
    float
        Analytic infinity-norm bound for the equilibrium.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    theta_inf = float(np.linalg.norm(theta_arr, ord=np.inf))
    inverse_bound = tdc_inverse_infinity_bound(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )

    return theta_inf * inverse_bound


def check_tdc_analytic_bounds(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> TDCBoundCheck:
    """
    Compute the analytic TDC theorem bounds at a fixed theta.

    In particular, this checks whether the sup-norm bound is sufficient to imply

        1 - alpha * w_i^*(theta) >= 0

    by requiring

        alpha * ||w*(theta)||_inf <= 1.

    Parameters
    ----------
    theta_values
        Theta vector.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.

    Returns
    -------
    TDCBoundCheck
        Structured analytic bound summary.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    alpha = float(theta_curvature_weight)

    min_margin = tdc_min_curvature_margin(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )
    inverse_bound = tdc_inverse_infinity_bound(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )
    theta_inf = float(np.linalg.norm(theta_arr, ord=np.inf))
    equilibrium_bound = tdc_equilibrium_infinity_bound(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )

    mixed_block_bound_ok = bool(alpha * equilibrium_bound <= 1.0)

    return TDCBoundCheck(
        theta_values=theta_arr,
        min_curvature_margin=min_margin,
        inverse_infinity_bound=inverse_bound,
        theta_infinity_norm=theta_inf,
        equilibrium_infinity_bound=equilibrium_bound,
        mixed_block_condition_bound_holds=mixed_block_bound_ok,
    )