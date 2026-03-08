import numpy as np

from network_potential_engine.theorem.tdc_region import in_tdc_region


def test_E1_tdc_region_membership_holds_for_basepoint() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = in_tdc_region(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.in_region is True
