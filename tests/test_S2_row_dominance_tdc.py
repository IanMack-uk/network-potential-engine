import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential


def _make_symbols(*, n: int) -> tuple[sp.Matrix, sp.Matrix]:
    w = sp.Matrix([sp.Symbol(f"w{i}", real=True) for i in range(n)])
    theta = sp.Matrix([sp.Symbol(f"theta{i}", positive=True) for i in range(n)])
    return w, theta


def _row_offdiag_abs_sum(C: sp.Matrix, i: int) -> sp.Expr:
    n = C.rows
    return sp.simplify(sum(sp.Abs(C[i, j]) for j in range(n) if j != i))


def test_s2_tdc_offdiagonals_are_tridiagonal_and_equal_minus_c() -> None:
    n = 5
    w, theta = _make_symbols(n=n)

    q = sp.Integer(1)
    alpha = sp.Rational(1, 5)
    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    hess = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(hess)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            entry = sp.simplify(C[i, j])

            if abs(i - j) == 1:
                assert entry == -c
            else:
                assert entry == 0


def test_s2_tdc_row_margins_simplify_to_expected_formula() -> None:
    n = 5
    w, theta = _make_symbols(n=n)

    q = sp.Integer(1)
    alpha = sp.Rational(1, 5)
    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    hess = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(hess)

    for i in range(n):
        diag = sp.simplify(C[i, i])
        offdiag_sum = _row_offdiag_abs_sum(C, i)
        margin = sp.simplify(diag - offdiag_sum)

        expected = sp.simplify(q + alpha * theta[i, 0])
        assert sp.simplify(margin - expected) == 0

        assert margin.is_positive is True
