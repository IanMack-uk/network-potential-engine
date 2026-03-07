from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.theorem.tdc_segment import (
    TDCSegmentCheck,
    check_tdc_segment_in_region,
)


@dataclass
class TDCLocalTheoremCheck:
    """
    Structured hypothesis check for the TDC local ordering theorem.

    Attributes
    ----------
    theta_left
        Left endpoint.
    theta_right
        Right endpoint.
    endpoint_order_holds
        Whether theta_right >= theta_left coordinatewise.
    segment_certificate
        Rigorous sufficient certificate that the full segment lies in the
        TDC admissible region.
    theorem_hypothesis_holds
        Whether both endpoint order and segment admissibility hold.
    """

    theta_left: np.ndarray
    theta_right: np.ndarray
    endpoint_order_holds: bool
    segment_certificate: TDCSegmentCheck
    theorem_hypothesis_holds: bool


def is_coordinatewise_ordered(
    theta_left: np.ndarray | list[float],
    theta_right: np.ndarray | list[float],
    tol: float = 1e-10,
) -> bool:
    """
    Return True if theta_right >= theta_left coordinatewise up to tolerance.
    """
    left = np.asarray(theta_left, dtype=float).reshape(-1)
    right = np.asarray(theta_right, dtype=float).reshape(-1)

    if left.shape != right.shape:
        raise ValueError("theta_left and theta_right must have the same shape.")

    return bool(np.all(right - left >= -tol))


def check_tdc_local_theorem_hypothesis(
    theta_left: np.ndarray | list[float],
    theta_right: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> TDCLocalTheoremCheck:
    """
    Check whether the TDC local ordering theorem hypothesis holds for a pair
    of endpoints.

    The hypothesis is:
    1. theta_right >= theta_left coordinatewise,
    2. the full segment between the endpoints lies in the TDC admissible region.
    """
    left = np.asarray(theta_left, dtype=float).reshape(-1)
    right = np.asarray(theta_right, dtype=float).reshape(-1)

    if left.shape != right.shape:
        raise ValueError("theta_left and theta_right must have the same shape.")

    endpoint_order = is_coordinatewise_ordered(left, right, tol=tol)
    segment_check = check_tdc_segment_in_region(
        left,
        right,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        tol=tol,
    )

    return TDCLocalTheoremCheck(
        theta_left=left,
        theta_right=right,
        endpoint_order_holds=endpoint_order,
        segment_certificate=segment_check,
        theorem_hypothesis_holds=(endpoint_order and segment_check.segment_in_region),
    )