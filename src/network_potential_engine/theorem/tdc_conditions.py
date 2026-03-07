from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class TDCConditionCheck:
    """
    Structured sufficient-condition check for the TDC local ordering theorem.

    Attributes
    ----------
    theta_values
        The theta vector at which the conditions are checked.
    w_star
        The equilibrium vector w*(theta).
    curvature_margins
        The row-wise curvature / diagonal-dominance margins q + alpha * theta_i.
    mixed_block_margins
        The mixed-block margins 1 - alpha * w_i^*(theta).
    curvature_condition_holds
        Whether q + alpha * theta_i > 0 for all i (up to tolerance).
    mixed_block_condition_holds
        Whether 1 - alpha * w_i^*(theta) >= 0 for all i (up to tolerance).
    all_conditions_hold
        Whether both sufficient conditions hold.
    """

    theta_values: np.ndarray
    w_star: np.ndarray
    curvature_margins: np.ndarray
    mixed_block_margins: np.ndarray
    curvature_condition_holds: bool
    mixed_block_condition_holds: bool
    all_conditions_hold: bool


def tdc_curvature_margins(
    theta_values: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> np.ndarray:
    """
    Compute the TDC curvature margins

        q + alpha * theta_i.

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
    np.ndarray
        Curvature margins q + alpha * theta_i.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    q = float(base_quadratic_weight)
    alpha = float(theta_curvature_weight)

    return q + alpha * theta_arr


def tdc_mixed_block_margins(
    w_star: np.ndarray | list[float],
    theta_curvature_weight: float,
) -> np.ndarray:
    """
    Compute the TDC mixed-block margins

        1 - alpha * w_i^*(theta).

    Parameters
    ----------
    w_star
        Equilibrium vector.
    theta_curvature_weight
        Theta-curvature parameter alpha.

    Returns
    -------
    np.ndarray
        Mixed-block margins 1 - alpha * w_i^*(theta).
    """
    w_arr = np.asarray(w_star, dtype=float).reshape(-1)
    alpha = float(theta_curvature_weight)

    return 1.0 - alpha * w_arr


def check_tdc_conditions(
    theta_values: np.ndarray | list[float],
    w_star: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> TDCConditionCheck:
    """
    Check the sufficient TDC local-ordering conditions at a fixed theta.

    The conditions are:
    1. q + alpha * theta_i > 0 for all i,
    2. 1 - alpha * w_i^*(theta) >= 0 for all i.

    Parameters
    ----------
    theta_values
        Theta vector.
    w_star
        Equilibrium vector.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.
    tol
        Numerical tolerance.

    Returns
    -------
    TDCConditionCheck
        Structured condition check result.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    w_arr = np.asarray(w_star, dtype=float).reshape(-1)

    if theta_arr.shape != w_arr.shape:
        raise ValueError("theta_values and w_star must have the same shape.")

    curvature = tdc_curvature_margins(
        theta_arr,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
    )
    mixed = tdc_mixed_block_margins(
        w_arr,
        theta_curvature_weight=theta_curvature_weight,
    )

    curvature_ok = bool(np.all(curvature > tol))
    mixed_ok = bool(np.all(mixed >= -tol))

    return TDCConditionCheck(
        theta_values=theta_arr,
        w_star=w_arr,
        curvature_margins=curvature,
        mixed_block_margins=mixed,
        curvature_condition_holds=curvature_ok,
        mixed_block_condition_holds=mixed_ok,
        all_conditions_hold=(curvature_ok and mixed_ok),
    )
