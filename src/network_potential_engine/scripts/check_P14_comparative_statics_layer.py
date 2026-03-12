from __future__ import annotations

from collections.abc import Callable

from network_potential_engine.scripts.check_C1_tdc_equilibrium_response_identity import (
    run_all_checks as check_c1,
)
from network_potential_engine.scripts.check_D1_tdc_inverse_positivity import run_all_checks as check_d1
from network_potential_engine.scripts.check_D2_tdc_mixed_block_positivity import run_all_checks as check_d2
from network_potential_engine.scripts.check_D3_tdc_response_positivity import run_all_checks as check_d3
from network_potential_engine.scripts.check_S1_motif_cross_partials import run_all_checks as check_s1
from network_potential_engine.scripts.check_S2_row_dominance_tdc import run_all_checks as check_s2
from network_potential_engine.scripts.check_S3_mmatrix_tdc import run_all_checks as check_s3


def _run_substep(name: str, fn: Callable[[], None]) -> None:
    print("-" * 78)
    print(f"P14 substep: {name}")
    print("-" * 78)
    fn()
    print()


def main() -> None:
    print("P14 comparative statics layer wrapper")
    print(
        "This step runs the certified comparative statics chain: "
        "C1 -> S1 -> S2 -> S3 -> D1 -> D2 -> D3"
    )
    print()
    _run_substep("C1 — Equilibrium Response Identity (TDC)", check_c1)
    _run_substep("S1 — Structural Z-matrix Preconditions (TDC)", check_s1)
    _run_substep("S2 — Structural Diagonal Dominance Preconditions (TDC)", check_s2)
    _run_substep("S3 — Structural M-matrix Preconditions (TDC)", check_s3)
    _run_substep("D1 — Inverse Positivity (TDC)", check_d1)
    _run_substep("D2 — Mixed-block Positivity (TDC)", check_d2)
    _run_substep("D3 — Response Positivity (TDC)", check_d3)


if __name__ == "__main__":
    main()
