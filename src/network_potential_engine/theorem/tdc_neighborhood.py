from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from network_potential_engine.theorem.local_scan import LocalScanRecord
from network_potential_engine.theorem.tdc_conditions import check_tdc_conditions


@dataclass
class TDCNeighborhoodSummary:
    """
    Summary of sufficient-condition margins across a sampled neighborhood.
    """

    min_curvature_margin: float
    min_mixed_block_margin: float
    curvature_condition_holds_everywhere: bool
    mixed_block_condition_holds_everywhere: bool
    all_conditions_hold_everywhere: bool


def summarize_tdc_conditions_on_scan(
    records: list[LocalScanRecord],
    base_quadratic_weight: float,
    theta_curvature_weight: float,
) -> TDCNeighborhoodSummary:
    """
    Summarize the TDC sufficient-condition margins across a scan.
    """
    if not records:
        raise ValueError("records must not be empty.")

    checks = [
        check_tdc_conditions(
            theta_values=record.theta,
            w_star=record.pointwise.equilibrium.w_star,
            base_quadratic_weight=base_quadratic_weight,
            theta_curvature_weight=theta_curvature_weight,
        )
        for record in records
    ]

    min_curvature_margin = float(
        min(np.min(check.curvature_margins) for check in checks)
    )
    min_mixed_block_margin = float(
        min(np.min(check.mixed_block_margins) for check in checks)
    )

    curvature_ok = all(check.curvature_condition_holds for check in checks)
    mixed_ok = all(check.mixed_block_condition_holds for check in checks)

    return TDCNeighborhoodSummary(
        min_curvature_margin=min_curvature_margin,
        min_mixed_block_margin=min_mixed_block_margin,
        curvature_condition_holds_everywhere=curvature_ok,
        mixed_block_condition_holds_everywhere=mixed_ok,
        all_conditions_hold_everywhere=(curvature_ok and mixed_ok),
    )
