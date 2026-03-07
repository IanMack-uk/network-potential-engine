from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

import numpy as np

from network_potential_engine.theorem.pointwise import PointwiseTheoremCheck, check_pointwise_conditions


@dataclass
class LocalScanRecord:
    """
    Result of a pointwise theorem check at one sampled theta value along a scan.
    """

    t: float
    theta: np.ndarray
    pointwise: PointwiseTheoremCheck


@dataclass
class EquilibriumDifferenceRecord:
    """
    Finite difference record between two consecutive scan points.

    Attributes
    ----------
    t_left
        Left scan parameter.
    t_right
        Right scan parameter.
    theta_left
        Left theta value.
    theta_right
        Right theta value.
    delta_theta
        Difference theta_right - theta_left.
    w_left
        Equilibrium at theta_left.
    w_right
        Equilibrium at theta_right.
    delta_w
        Difference w_right - w_left.
    delta_w_is_entrywise_nonnegative
        Whether delta_w is entrywise nonnegative up to tolerance.
    """

    t_left: float
    t_right: float
    theta_left: np.ndarray
    theta_right: np.ndarray
    delta_theta: np.ndarray
    w_left: np.ndarray
    w_right: np.ndarray
    delta_w: np.ndarray
    delta_w_is_entrywise_nonnegative: bool


def build_theta_line(
    theta0: np.ndarray | Sequence[float],
    direction: np.ndarray | Sequence[float],
    t: float,
) -> np.ndarray:
    """
    Construct a point on the theta line theta(t) = theta0 + t * direction.
    """
    theta0_arr = np.asarray(theta0, dtype=float).reshape(-1)
    direction_arr = np.asarray(direction, dtype=float).reshape(-1)

    if theta0_arr.shape != direction_arr.shape:
        raise ValueError("theta0 and direction must have the same shape.")

    return theta0_arr + float(t) * direction_arr


def is_vector_entrywise_nonnegative(
    vector: np.ndarray | Sequence[float],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether every entry of a vector is nonnegative up to tolerance.
    """
    arr = np.asarray(vector, dtype=float).reshape(-1)
    return bool(np.all(arr >= -tol))


def scan_pointwise_along_line(
    gradient_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    hessian_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    mixed_block_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    theta0: np.ndarray | Sequence[float],
    direction: np.ndarray | Sequence[float],
    t_values: Sequence[float],
    w0: np.ndarray | Sequence[float],
    residual_tol: float = 1e-10,
    sign_tol: float = 1e-10,
) -> list[LocalScanRecord]:
    """
    Scan pointwise theorem conditions along the line theta(t) = theta0 + t * direction.
    """
    theta0_arr = np.asarray(theta0, dtype=float).reshape(-1)
    direction_arr = np.asarray(direction, dtype=float).reshape(-1)
    w0_arr = np.asarray(w0, dtype=float).reshape(-1)

    if theta0_arr.shape != direction_arr.shape:
        raise ValueError("theta0 and direction must have the same shape.")

    records: list[LocalScanRecord] = []

    for t in t_values:
        theta_t = build_theta_line(theta0_arr, direction_arr, float(t))

        pointwise = check_pointwise_conditions(
            gradient_fn=gradient_fn,
            hessian_fn=hessian_fn,
            mixed_block_fn=mixed_block_fn,
            theta_values=theta_t,
            w0=w0_arr,
            residual_tol=residual_tol,
            sign_tol=sign_tol,
        )

        records.append(
            LocalScanRecord(
                t=float(t),
                theta=theta_t,
                pointwise=pointwise,
            )
        )

    return records


def all_pointwise_checks_pass(records: Sequence[LocalScanRecord]) -> bool:
    """
    Return True if every sampled point passes the key pointwise checks.
    """
    for record in records:
        check = record.pointwise
        if not check.equilibrium.success:
            return False
        if not check.is_c_symmetric:
            return False
        if not check.is_c_strictly_diagonally_dominant:
            return False
        if not check.has_c_nonpositive_off_diagonals:
            return False
        if not check.response_is_entrywise_nonnegative:
            return False

    return True


def minimum_scan_margin(records: Sequence[LocalScanRecord]) -> float:
    """
    Return the smallest diagonal-dominance margin observed across the scan.
    """
    if not records:
        raise ValueError("records must not be empty.")

    return float(
        min(record.pointwise.c_min_diagonal_dominance_margin for record in records)
    )


def equilibrium_differences(
    records: Sequence[LocalScanRecord],
    tol: float = 1e-10,
) -> list[EquilibriumDifferenceRecord]:
    """
    Compute finite equilibrium differences between consecutive scan points.

    Parameters
    ----------
    records
        Scan records ordered by increasing t.
    tol
        Tolerance used for entrywise nonnegativity of delta_w.

    Returns
    -------
    list[EquilibriumDifferenceRecord]
        Consecutive finite-difference records.
    """
    if len(records) < 2:
        return []

    diffs: list[EquilibriumDifferenceRecord] = []

    for left, right in zip(records[:-1], records[1:]):
        theta_left = np.asarray(left.theta, dtype=float).reshape(-1)
        theta_right = np.asarray(right.theta, dtype=float).reshape(-1)
        w_left = np.asarray(left.pointwise.equilibrium.w_star, dtype=float).reshape(-1)
        w_right = np.asarray(right.pointwise.equilibrium.w_star, dtype=float).reshape(-1)

        delta_theta = theta_right - theta_left
        delta_w = w_right - w_left

        diffs.append(
            EquilibriumDifferenceRecord(
                t_left=float(left.t),
                t_right=float(right.t),
                theta_left=theta_left,
                theta_right=theta_right,
                delta_theta=delta_theta,
                w_left=w_left,
                w_right=w_right,
                delta_w=delta_w,
                delta_w_is_entrywise_nonnegative=is_vector_entrywise_nonnegative(
                    delta_w, tol=tol
                ),
            )
        )

    return diffs


def all_equilibrium_differences_nonnegative(
    records: Sequence[LocalScanRecord],
    tol: float = 1e-10,
) -> bool:
    """
    Return True if all consecutive equilibrium differences are entrywise nonnegative.
    """
    diffs = equilibrium_differences(records, tol=tol)
    return all(diff.delta_w_is_entrywise_nonnegative for diff in diffs)
