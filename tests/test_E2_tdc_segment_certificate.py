import numpy as np

from network_potential_engine.theorem.tdc_segment import check_tdc_segment_in_region


def test_E2_tdc_segment_certificate_holds_for_representative_step() -> None:
    theta_left = np.array([0.0, -0.1, -0.2], dtype=float)
    theta_right = np.array([0.1, 0.0, -0.1], dtype=float)

    check = check_tdc_segment_in_region(
        theta_left,
        theta_right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.segment_in_region is True
