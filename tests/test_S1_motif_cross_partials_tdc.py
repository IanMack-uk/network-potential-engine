import sympy as sp

from network_potential_engine.symbolic.motif_analysis import (
    build_cross_partial_report_for_groups,
    decompose_tdc_into_admissible_grammar_terms,
    decompose_tdc_into_pilot_groups,
)
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def test_s1_tdc_pilot_groups_exist_with_expected_classes() -> None:
    w, theta = make_symbols(5, 5)
    groups = decompose_tdc_into_pilot_groups(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    ids = [g.group_id for g in groups]
    classes = [g.group_class for g in groups]

    assert ids == ["linear", "diagonal_curvature", "coupling"]
    assert classes == ["linear", "diagonal", "interaction"]


def test_s1_tdc_aggregated_coupling_is_zmatrix_and_tridiagonal_off_diagonals() -> None:
    w, theta = make_symbols(5, 5)

    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=c,
    )

    hess = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hess)

    n = coupling.rows
    assert coupling.cols == n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            entry = sp.simplify(coupling[i, j])

            if abs(i - j) == 1:
                assert entry == -c
            else:
                assert entry == 0


def test_s1_tdc_report_aggregated_zmatrix_flag_is_true() -> None:
    w, theta = make_symbols(5, 5)

    groups = decompose_tdc_into_admissible_grammar_terms(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    report = build_cross_partial_report_for_groups(
        model="tdc",
        groups=groups,
        w=w,
        theta=theta,
    )

    assert report.aggregated_is_zmatrix is True
