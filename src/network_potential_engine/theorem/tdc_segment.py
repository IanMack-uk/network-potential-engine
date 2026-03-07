from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class TDCSegmentCheck:
    """
    Rigorous sufficient certificate that the line segment between two theta points
    lies inside the TDC admissible region.

    Attributes
    ----------
    theta_left
        Left endpoint.
    theta_right
        Right endpoint.
    segment_min_curvature_margin
        Lower bound for min_i(q + alpha * theta_i) along the whole segment.
    segment_max_theta_infinity_norm
        Upper bound for ||theta||_inf along the whole segment.
    curvature_condition_holds_on_segment
        Whether the curvature margin is positive along the segment.
    mixed_block_bound_holds_on_segment
        Whether the analytic mixed-block bound is satisfied on the segment.
    segment_in_region
        Whether both sufficient conditions hold on the whole segment.
    """

    theta_left: np.ndarray
    theta_right: np.ndarray
    segment_min_curvature_margin: float
    segment_max_theta_infinity_norm: float
    curvature_condition_holds_on_segment: bool
    mixed_block_bound_holds_on_segment: bool
    segment_in_region: bool


def check_tdc_segment_in_region(
    theta_left: np.ndarray | list[float],
    theta_right: np.ndarray | list[float],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> TDCSegmentCheck:
    """
    Check a rigorous sufficient condition that the full line segment between
    theta_left and theta_right lies in the TDC admissible region.

    The certificate uses:

        m_seg = min_i (q + alpha * min(theta_left_i, theta_right_i))
        M_seg = max(||theta_left||_inf, ||theta_right||_inf)

    and declares the full segment admissible if

        m_seg > 0
        alpha * M_seg / m_seg <= 1.

    Parameters
    ----------
    theta_left
        Left endpoint.
    theta_right
        Right endpoint.
    base_quadratic_weight
        Baseline curvature parameter q.
    theta_curvature_weight
        Theta-curvature parameter alpha.
    tol
        Numerical tolerance.

    Returns
    -------
    TDCSegmentCheck
        Structured segment certificate.
    """
    left = np.asarray(theta_left, dtype=float).reshape(-1)
    right = np.asarray(theta_right, dtype=float).reshape(-1)

    if left.shape != right.shape:
        raise ValueError("theta_left and theta_right must have the same shape.")

    q = float(base_quadratic_weight)
    alpha = float(theta_curvature_weight)

    coordwise_min = np.minimum(left, right)
    segment_min_margin = float(np.min(q + alpha * coordwise_min))

    segment_max_norm = float(
        max(np.linalg.norm(left, ord=np.inf), np.linalg.norm(right, ord=np.inf))
    )

    curvature_ok = bool(segment_min_margin > tol)

    if not curvature_ok:
        return TDCSegmentCheck(
            theta_left=left,
            theta_right=right,
            segment_min_curvature_margin=segment_min_margin,
            segment_max_theta_infinity_norm=segment_max_norm,
            curvature_condition_holds_on_segment=False,
            mixed_block_bound_holds_on_segment=False,
            segment_in_region=False,
        )

    mixed_ok = bool(alpha * segment_max_norm / segment_min_margin <= 1.0 + tol)

    return TDCSegmentCheck(
        theta_left=left,
        theta_right=right,
        segment_min_curvature_margin=segment_min_margin,
        segment_max_theta_infinity_norm=segment_max_norm,
        curvature_condition_holds_on_segment=True,
        mixed_block_bound_holds_on_segment=mixed_ok,
        segment_in_region=(True and mixed_ok),
    )


def all_consecutive_segments_in_region(
    theta_points: list[np.ndarray] | list[list[float]],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    tol: float = 1e-10,
) -> bool:
    """
    Return True if every consecutive segment in a list of theta points is certified
    to lie inside the TDC admissible region.
    """
    if len(theta_points) < 2:
        return True

    return all(
        check_tdc_segment_in_region(
            theta_points[i],
            theta_points[i + 1],
            base_quadratic_weight=base_quadratic_weight,
            theta_curvature_weight=theta_curvature_weight,
            tol=tol,
        ).segment_in_region
        for i in range(len(theta_points) - 1)
    )