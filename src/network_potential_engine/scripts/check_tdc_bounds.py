from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_bounds import check_tdc_analytic_bounds


def main() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = check_tdc_analytic_bounds(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    print("=" * 72)
    print("TDC ANALYTIC BOUNDS")
    print("=" * 72)

    print("\nTheta values:")
    print(check.theta_values)

    print(f"\nMinimum curvature margin m(theta): {check.min_curvature_margin:.6f}")
    print(f"Inverse infinity bound 1/m(theta): {check.inverse_infinity_bound:.6f}")
    print(f"Theta infinity norm ||theta||_inf: {check.theta_infinity_norm:.6f}")

    print(
        "\nEquilibrium infinity bound "
        "||w*(theta)||_inf <= ||theta||_inf / m(theta):"
    )
    print(f"{check.equilibrium_infinity_bound:.6f}")

    print(
        "\nBound implies mixed-block positivity "
        "(alpha * ||w*(theta)||_inf <= 1):"
    )
    print(check.mixed_block_condition_bound_holds)

    print("\nDone.")


if __name__ == "__main__":
    main()
