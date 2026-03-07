from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.numeric.equilibrium import solve_equilibrium
from network_potential_engine.theorem.tdc_local_theorem import (
    TDCLocalTheoremCheck,
    check_tdc_local_theorem_hypothesis,
)


@dataclass
class TDCLocalWitness:
    """
    Combined theorem-hypothesis and observed-conclusion check for a pair of TDC endpoints.

    Attributes
    ----------
    theorem_check
        Result of checking the local theorem hypothesis.
    w_left
        Equilibrium at the left endpoint.
    w_right
        Equilibrium at the right endpoint.
    delta_w
        Difference w_right - w_left.
    observed_equilibrium_order_holds
        Whether delta_w >= 0 coordinatewise.
    witness_consistent
        Whether the theorem hypothesis holds and the observed equilibrium ordering
        also holds numerically.
    """

    theorem_check: TDCLocalTheoremCheck
    w_left: np.ndarray
    w_right: np.ndarray
    delta_w: np.ndarray
    observed_equilibrium_order_holds: bool
    witness_consistent: bool


def is_equilibrium_ordered(
    w_left: np.ndarray | list[float],
    w_right: np.ndarray | list[float],
    tol: float = 1e-10,
) -> bool:
    """
    Return True if w_right >= w_left coordinatewise up to tolerance.
    """
    left = np.asarray(w_left, dtype=float).reshape(-1)
    right = np.asarray(w_right, dtype=float).reshape(-1)

    if left.shape != right.shape:
        raise ValueError("w_left and w_right must have the same shape.")

    return bool(np.all(right - left >= -tol))


def build_tdc_local_witness(
    gradient_fn,
    theta_left: np.ndarray | list[float],
    theta_right: np.ndarray | list[float],
    w0_left: np.ndarray | list[float],
    w0_right: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    residual_tol: float = 1e-10,
    tol: float = 1e-10,
) -> TDCLocalWitness:
    """
    Build a combined local theorem witness for a TDC endpoint pair.

    This checks:
    1. whether the theorem hypothesis holds for the endpoint pair, and
    2. whether the observed equilibria satisfy the predicted coordinatewise order.
    """
    left = np.asarray(theta_left, dtype=float).reshape(-1)
    right = np.asarray(theta_right, dtype=float).reshape(-1)
    w0_l = np.asarray(w0_left, dtype=float).reshape(-1)
    w0_r = np.asarray(w0_right, dtype=float).reshape(-1)

    if left.shape != right.shape:
        raise ValueError("theta_left and theta_right must have the same shape.")

    theorem_check = check_tdc_local_theorem_hypothesis(
        left,
        right,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        tol=tol,
    )

    eq_left = solve_equilibrium(
        gradient_fn=gradient_fn,
        theta_values=left,
        w0=w0_l,
        residual_tol=residual_tol,
    )
    eq_right = solve_equilibrium(
        gradient_fn=gradient_fn,
        theta_values=right,
        w0=w0_r,
        residual_tol=residual_tol,
    )

    if not eq_left.success:
        raise RuntimeError(
            f"Left equilibrium solve failed: {eq_left.message} "
            f"(residual={eq_left.residual_norm})"
        )
    if not eq_right.success:
        raise RuntimeError(
            f"Right equilibrium solve failed: {eq_right.message} "
            f"(residual={eq_right.residual_norm})"
        )

    delta_w = np.asarray(eq_right.w_star - eq_left.w_star, dtype=float).reshape(-1)
    observed_order = is_equilibrium_ordered(eq_left.w_star, eq_right.w_star, tol=tol)

    return TDCLocalWitness(
        theorem_check=theorem_check,
        w_left=np.asarray(eq_left.w_star, dtype=float).reshape(-1),
        w_right=np.asarray(eq_right.w_star, dtype=float).reshape(-1),
        delta_w=delta_w,
        observed_equilibrium_order_holds=observed_order,
        witness_consistent=(theorem_check.theorem_hypothesis_holds and observed_order),
    )