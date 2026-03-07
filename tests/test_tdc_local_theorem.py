import numpy as np

from network_potential_engine.theorem.tdc_local_theorem import (
    check_tdc_local_theorem_hypothesis,
    is_coordinatewise_ordered,
)


def test_coordinatewise_order_detects_monotone_pair() -> None:
    left = np.array([0.0, -0.1, -0.2], dtype=float)
    right = np.array([0.1, 0.0, -0.1], dtype=float)

    assert is_coordinatewise_ordered(left, right) is True


def test_coordinatewise_order_detects_nonmonotone_pair() -> None:
    left = np.array([0.2, 0.1, 0.0], dtype=float)
    right = np.array([0.1, 0.2, 0.0], dtype=float)

    assert is_coordinatewise_ordered(left, right) is False


def test_tdc_local_theorem_hypothesis_holds_for_current_scan_step() -> None:
    left = np.array([0.2, 0.1, 0.0], dtype=float)
    right = np.array([0.3, 0.2, 0.1], dtype=float)

    check = check_tdc_local_theorem_hypothesis(
        left,
        right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.endpoint_order_holds is True
    assert check.segment_certificate.segment_in_region is True
    assert check.theorem_hypothesis_holds is True


def test_tdc_local_theorem_hypothesis_fails_when_endpoint_order_fails() -> None:
    left = np.array([0.2, 0.1, 0.0], dtype=float)
    right = np.array([0.1, 0.2, 0.0], dtype=float)

    check = check_tdc_local_theorem_hypothesis(
        left,
        right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.endpoint_order_holds is False
    assert check.theorem_hypothesis_holds is False