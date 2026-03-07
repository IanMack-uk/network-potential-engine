from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_local_theorem import (
    check_tdc_local_theorem_hypothesis,
)


def main() -> None:
    left = np.array([0.2, 0.1, 0.0], dtype=float)
    right = np.array([0.3, 0.2, 0.1], dtype=float)

    check = check_tdc_local_theorem_hypothesis(
        left,
        right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC LOCAL THEOREM HYPOTHESIS CHECK")
    print("=" * 72)

    print(f"\nLeft endpoint  = {check.theta_left}")
    print(f"Right endpoint = {check.theta_right}")
    print(f"Endpoint order holds          : {check.endpoint_order_holds}")
    print(
        f"Segment min curvature margin  : "
        f"{check.segment_certificate.segment_min_curvature_margin:.6f}"
    )
    print(
        f"Segment max ||theta||_inf     : "
        f"{check.segment_certificate.segment_max_theta_infinity_norm:.6f}"
    )
    print(
        f"Segment curvature condition   : "
        f"{check.segment_certificate.curvature_condition_holds_on_segment}"
    )
    print(
        f"Segment mixed-block condition : "
        f"{check.segment_certificate.mixed_block_bound_holds_on_segment}"
    )
    print(
        f"Segment in admissible region  : "
        f"{check.segment_certificate.segment_in_region}"
    )
    print(f"Theorem hypothesis holds      : {check.theorem_hypothesis_holds}")

    print("\nDone.")


if __name__ == "__main__":
    main()
