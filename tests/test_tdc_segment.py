import numpy as np

from network_potential_engine.theorem.tdc_segment import (
    all_consecutive_segments_in_region,
    check_tdc_segment_in_region,
)


def test_tdc_segment_certificate_holds_for_current_scan_step() -> None:
    left = np.array([0.0, -0.1, -0.2], dtype=float)
    right = np.array([0.1, 0.0, -0.1], dtype=float)

    check = check_tdc_segment_in_region(
        left,
        right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert np.isclose(check.segment_min_curvature_margin, 0.96)
    assert np.isclose(check.segment_max_theta_infinity_norm, 0.2)
    assert check.curvature_condition_holds_on_segment is True
    assert check.mixed_block_bound_holds_on_segment is True
    assert check.segment_in_region is True


def test_all_consecutive_tdc_scan_segments_are_certified() -> None:
    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]

    assert all_consecutive_segments_in_region(
        theta_points,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    ) is True


def test_tdc_segment_certificate_fails_when_curvature_margin_breaks() -> None:
    left = np.array([-6.0, 0.0, 0.0], dtype=float)
    right = np.array([-5.5, 0.0, 0.0], dtype=float)

    check = check_tdc_segment_in_region(
        left,
        right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.curvature_condition_holds_on_segment is False
    assert check.segment_in_region is False