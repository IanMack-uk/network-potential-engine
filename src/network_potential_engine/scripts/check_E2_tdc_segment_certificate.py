from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_segment import check_tdc_segment_in_region


def run_all_checks() -> None:
    theta_left = np.array([0.0, -0.1, -0.2], dtype=float)
    theta_right = np.array([0.1, 0.0, -0.1], dtype=float)

    check = check_tdc_segment_in_region(
        theta_left,
        theta_right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.segment_in_region is True

    print("Running E2 segment certificate checks (TDC model)")
    print("✓ Segment is certified to lie inside the admissible region ℛ")
    print("E2 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
