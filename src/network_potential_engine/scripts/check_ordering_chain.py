from __future__ import annotations

from typing import Callable

from network_potential_engine.scripts.check_E1_tdc_region import run_all_checks as check_e1
from network_potential_engine.scripts.check_E2_tdc_segment_certificate import (
    run_all_checks as check_e2,
)
from network_potential_engine.scripts.check_E3_tdc_local_weak_ordering import (
    run_all_checks as check_e3,
)


def run_step(name: str, fn: Callable[[], None]) -> None:
    print("=" * 78)
    print(f"ORDERING CHAIN CHECK: {name}")
    print("=" * 78)
    fn()
    print()


def main() -> None:
    run_step("E1 — Explicit Admissible Region (TDC)", check_e1)
    run_step("E2 — Segment Certificate (TDC)", check_e2)
    run_step("E3 — Local Weak Ordering (TDC)", check_e3)
    print("=" * 78)
    print("ORDERING CHAIN CHECK: PASS")
    print("=" * 78)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("=" * 78)
        print("ORDERING CHAIN CHECK: FAIL")
        print("=" * 78)
        raise
