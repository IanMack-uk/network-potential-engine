from __future__ import annotations

from typing import Callable

from network_potential_engine.scripts.check_C1_tdc_equilibrium_response_identity import (
    run_all_checks as check_c1,
)
from network_potential_engine.scripts.check_S1_motif_cross_partials import run_all_checks as check_s1
from network_potential_engine.scripts.check_S2_row_dominance_tdc import run_all_checks as check_s2
from network_potential_engine.scripts.check_S3_mmatrix_tdc import run_all_checks as check_s3
from network_potential_engine.scripts.check_D1_tdc_inverse_positivity import (
    run_all_checks as check_d1,
)
from network_potential_engine.scripts.check_D2_tdc_mixed_block_positivity import (
    run_all_checks as check_d2,
)
from network_potential_engine.scripts.check_D3_tdc_response_positivity import (
    run_all_checks as check_d3,
)


def run_step(name: str, fn: Callable[[], None]) -> None:
    print("=" * 78)
    print(f"COMPARATIVE STATICS CHAIN CHECK: {name}")
    print("=" * 78)
    fn()
    print()


def main() -> None:
    run_step("C1 — Equilibrium Response Identity (TDC)", check_c1)
    run_step("S1 — Structural Z-matrix Preconditions (TDC)", check_s1)
    run_step("S2 — Structural Diagonal Dominance Preconditions (TDC)", check_s2)
    run_step("S3 — Structural M-matrix Preconditions (TDC)", check_s3)
    run_step("D1 — Inverse Positivity (TDC)", check_d1)
    run_step("D2 — Mixed-block Positivity (TDC)", check_d2)
    run_step("D3 — Response Positivity (TDC)", check_d3)
    print("=" * 78)
    print("COMPARATIVE STATICS CHAIN CHECK: PASS")
    print("=" * 78)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("=" * 78)
        print("COMPARATIVE STATICS CHAIN CHECK: FAIL")
        print("=" * 78)
        raise
