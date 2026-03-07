from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_region import (
    all_points_in_tdc_region,
    in_tdc_region,
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
    print("TDC REGION SCAN CHECK")
    print("=" * 72)

    for theta in theta_points:
        check = in_tdc_region(
            theta,
            base_quadratic_weight=1.0,
            theta_curvature_weight=0.2,
        )

        print("-" * 72)
        print(f"theta = {check.theta_values}")
        print(f"min curvature margin   = {check.min_curvature_margin:.6f}")
        print(f"theta infinity norm    = {check.theta_infinity_norm:.6f}")
        print(f"equilibrium inf bound  = {check.equilibrium_infinity_bound:.6f}")
        print(f"curvature condition    = {check.curvature_region_condition}")
        print(f"mixed-block condition  = {check.mixed_block_region_condition}")
        print(f"in region              = {check.in_region}")

    print("\nSummary:")
    print(
        "All sampled points in theorem-ready region: "
        f"{all_points_in_tdc_region(theta_points, 1.0, 0.2)}"
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
