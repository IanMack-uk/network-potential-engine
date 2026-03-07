import numpy as np

from network_potential_engine.theorem.tdc_region import (
    all_points_in_tdc_region,
    in_tdc_region,
)


def test_in_tdc_region_holds_for_current_basepoint() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = in_tdc_region(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert np.isclose(check.min_curvature_margin, 1.0)
    assert np.isclose(check.theta_infinity_norm, 0.2)
    assert np.isclose(check.equilibrium_infinity_bound, 0.2)

    assert check.curvature_region_condition is True
    assert check.mixed_block_region_condition is True
    assert check.in_region is True


def test_in_tdc_region_holds_for_current_scan_points() -> None:
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


def test_in_tdc_region_fails_when_curvature_margin_is_nonpositive() -> None:
    theta_values = np.array([-6.0, 0.0, 0.0], dtype=float)

    check = in_tdc_region(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.curvature_region_condition is False
    assert check.in_region is False