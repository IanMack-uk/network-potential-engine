from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_segment import (
    all_consecutive_segments_in_region,
    check_tdc_segment_in_region,
)


def main() -> None:
    theta_points = [
        np.array([0.0, -0.1, -0.2], dtype=float),
        np.array([0.1, 0.0, -0.1], dtype=float),
        np.array([0.2, 0.1, 0.0], dtype=float),
        np.array([0.3, 0.2, 0.1], dtype=float),
        np.array([0.4, 0.3, 0.2], dtype=float),
    ]

    print("=" * 72)
    print("TDC SEGMENT CERTIFICATE CHECK")
    print("=" * 72)

    for left, right in zip(theta_points[:-1], theta_points[1:]):
        check = check_tdc_segment_in_region(
            left,
            right,
            base_quadratic_weight=1.0,
            theta_curvature_weight=0.2,
        )

        print("-" * 72)
        print(f"left endpoint  = {check.theta_left}")
        print(f"right endpoint = {check.theta_right}")
        print(
            f"segment min curvature margin = "
            f"{check.segment_min_curvature_margin:.6f}"
        )
        print(
            f"segment max ||theta||_inf    = "
            f"{check.segment_max_theta_infinity_norm:.6f}"
        )
        print(
            f"curvature condition on segment = "
            f"{check.curvature_condition_holds_on_segment}"
        )
        print(
            f"mixed-block bound on segment  = "
            f"{check.mixed_block_bound_holds_on_segment}"
        )
        print(f"segment in region             = {check.segment_in_region}")

    print("\nSummary:")
    print(
        "All consecutive segments certified: "
        f"{all_consecutive_segments_in_region(theta_points, 1.0, 0.2)}"
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
