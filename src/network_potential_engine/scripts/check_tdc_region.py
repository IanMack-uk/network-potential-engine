from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_region import in_tdc_region


def main() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = in_tdc_region(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC ADMISSIBLE REGION CHECK")
    print("=" * 72)

    print("\nTheta values:")
    print(check.theta_values)

    print(f"\nMinimum curvature margin m(theta): {check.min_curvature_margin:.6f}")
    print(f"Theta infinity norm ||theta||_inf: {check.theta_infinity_norm:.6f}")
    print(
        "Equilibrium infinity bound "
        "||w*(theta)||_inf <= ||theta||_inf / m(theta): "
        f"{check.equilibrium_infinity_bound:.6f}"
    )

    print(f"\nCurvature region condition      : {check.curvature_region_condition}")
    print(f"Mixed-block region condition    : {check.mixed_block_region_condition}")
    print(f"In theorem-ready admissible set : {check.in_region}")

    print("\nDone.")


if __name__ == "__main__":
    main()