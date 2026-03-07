import numpy as np

from network_potential_engine.theorem.tdc_region import (
    all_points_in_tdc_region,
    in_tdc_region,
)


def test_current_tdc_scan_points_all_lie_in_region() -> None:
    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]

    assert all_points_in_tdc_region(
        theta_points,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    ) is True


def test_region_membership_has_positive_slack_on_current_scan() -> None:
    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]

    checks = [
        in_tdc_region(
            theta,
            base_quadratic_weight=1.0,
            theta_curvature_weight=0.2,
        )
        for theta in theta_points
    ]

    assert all(check.in_region for check in checks)
    assert min(check.min_curvature_margin for check in checks) > 0.95