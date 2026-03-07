import numpy as np

from network_potential_engine.theorem.tdc_bounds import (
    check_tdc_analytic_bounds,
    tdc_equilibrium_infinity_bound,
    tdc_inverse_infinity_bound,
    tdc_min_curvature_margin,
)


def test_tdc_min_curvature_margin_matches_formula() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    min_margin = tdc_min_curvature_margin(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert np.isclose(min_margin, 1.0)


def test_tdc_inverse_infinity_bound_matches_formula() -> None:
    theta_values = np.array([0.0, -0.1, -0.2], dtype=float)

    bound = tdc_inverse_infinity_bound(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    # min_i (q + alpha * theta_i) = min(1.0, 0.98, 0.96) = 0.96
    assert np.isclose(bound, 1.0 / 0.96)


def test_tdc_equilibrium_infinity_bound_matches_formula() -> None:
    theta_values = np.array([0.4, 0.3, 0.2], dtype=float)

    bound = tdc_equilibrium_infinity_bound(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    expected = 0.4 / 1.04
    assert np.isclose(bound, expected)


def test_check_tdc_analytic_bounds_holds_for_current_example() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = check_tdc_analytic_bounds(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert np.isclose(check.min_curvature_margin, 1.0)
    assert np.isclose(check.theta_infinity_norm, 0.2)
    assert np.isclose(check.inverse_infinity_bound, 1.0)
    assert np.isclose(check.equilibrium_infinity_bound, 0.2)
    assert check.mixed_block_condition_bound_holds is True