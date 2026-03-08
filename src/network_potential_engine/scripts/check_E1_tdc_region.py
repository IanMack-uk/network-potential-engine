from __future__ import annotations

import numpy as np

from network_potential_engine.theorem.tdc_region import in_tdc_region


def run_all_checks() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    check = in_tdc_region(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.in_region is True

    print("Running E1 admissible-region checks (TDC model)")
    print("✓ θ is in the TDC admissible region ℛ")
    print("E1 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
