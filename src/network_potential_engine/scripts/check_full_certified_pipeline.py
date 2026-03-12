from __future__ import annotations

from collections.abc import Callable

from network_potential_engine.scripts.check_A1_tdc_well_posedness import run_all_checks as check_a1
from network_potential_engine.scripts.check_A2_tdc_equilibrium_existence import run_all_checks as check_a2
from network_potential_engine.scripts.check_A3a_tdc_equilibrium_regularity import run_all_checks as check_a3a
from network_potential_engine.scripts.check_A3b_tdc_interior_nondegeneracy import run_all_checks as check_a3b
from network_potential_engine.scripts.check_B1_tdc_hessian_coupling_identity import run_all_checks as check_b1
from network_potential_engine.scripts.check_B2_tdc_tridiagonal_coupling_structure import (
    run_all_checks as check_b2,
)
from network_potential_engine.scripts.check_P1_graph_layer_primitives import main as check_p1
from network_potential_engine.scripts.check_P2_node_attributes import main as check_p2
from network_potential_engine.scripts.check_P3_node_source_value import main as check_p3
from network_potential_engine.scripts.check_P4_feasible_relational_investment import main as check_p4
from network_potential_engine.scripts.check_P5_network_potential_functional import main as check_p5
from network_potential_engine.scripts.check_P6_equilibrium_network import main as check_p6
from network_potential_engine.scripts.check_P7_equilibrium_characterisation import main as check_p7
from network_potential_engine.scripts.check_P8_coupling_operator import main as check_p8
from network_potential_engine.scripts.check_P9_green_operator import main as check_p9
from network_potential_engine.scripts.check_P10_propagation_mapping import main as check_p10
from network_potential_engine.scripts.check_P11_node_energy_definition import main as check_p11
from network_potential_engine.scripts.check_P12_diffusion_receptivity import main as check_p12
from network_potential_engine.scripts.check_P13_effective_node_energy import main as check_p13
from network_potential_engine.scripts.check_P14_comparative_statics_layer import main as check_p14
from network_potential_engine.scripts.check_ordering_chain import main as check_ordering
from network_potential_engine.scripts.check_P15_dynamic_network_evolution import main as check_p15
from network_potential_engine.scripts.check_P16_endogenous_topology import main as check_p16
from network_potential_engine.scripts.check_P17_universality_layer import main as check_p17
from network_potential_engine.theorem.runner import run_check


def run_step(name: str, fn: Callable[[], object]) -> None:
    print("=" * 78)
    print(f"FULL PIPELINE CHECK: {name}")
    print("=" * 78)
    report = run_check(name, fn)
    if not report.passed:
        if report.error is not None:
            raise report.error
        raise RuntimeError(f"{report.error_type}: {report.error_message}")
    print()


def main() -> None:
    run_step("A1 — Well-posedness (TDC)", check_a1)
    run_step("A2 — Equilibrium existence (TDC)", check_a2)
    run_step("A3a — Equilibrium regularity (TDC)", check_a3a)
    run_step("A3b — Interior nondegeneracy (TDC)", check_a3b)

    run_step("P1 / Step 1(1) — Network Representation", check_p1)
    run_step("P2 / Step 2(9) — Node Attributes", check_p2)
    run_step("P3 / Step 3(10) — Node Source Value", check_p3)
    run_step("P4 / Step 4(2) — Feasible Relational Investment", check_p4)
    run_step("P5 / Step 5(3) — Network Potential Functional", check_p5)
    run_step("P6 / Step 6(4) — Equilibrium Network", check_p6)
    run_step("P7 / Step 7(5) — Equilibrium Characterisation", check_p7)
    run_step("P8 / Step 8(6) — Coupling Operator", check_p8)
    run_step("P8 :: B1 — Hessian–Coupling identity (TDC)", check_b1)
    run_step("P8 :: B2 — Tridiagonal coupling structure (TDC)", check_b2)
    run_step("P9 / Step 9(7) — Green Operator", check_p9)
    run_step("P10 / Step 10(11) — Propagation Mapping", check_p10)
    run_step("P11 / Step 11(12) — Node Energy Definition", check_p11)
    run_step("P12 / Step 12(13) — Diffusion / Receptivity", check_p12)
    run_step("P13 / Step 13(14) — Effective Node Energy", check_p13)
    run_step("P14 / Step 14(8) — Comparative Statics Layer", check_p14)
    run_step("P14 :: Ordering layer — E1 -> E2 -> E3", check_ordering)
    run_step("P15 / Step 15(15) — Dynamic Network Evolution", check_p15)
    run_step("P16 / Step 16(16) — Endogenous Topology", check_p16)
    run_step("P17 / Step 17(17) — Universality Layer", check_p17)

    print("=" * 78)
    print("FULL PIPELINE CHECK: PASS")
    print("=" * 78)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("=" * 78)
        print("FULL PIPELINE CHECK: FAIL")
        print("=" * 78)
        raise
