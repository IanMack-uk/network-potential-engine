from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian


def _real_float(ev: sp.Expr, *, imag_tol: float = 1e-12) -> float:
    ev_eval = ev.evalf(chop=True)
    if ev_eval.is_real is True:
        return float(ev_eval)
    ev_complex = complex(ev_eval)
    if abs(ev_complex.imag) > imag_tol:
        raise TypeError(f"Invalid comparison of non-real eigenvalue {ev_eval}")
    return float(ev_complex.real)


def _build_tdc_objects(n: int = 3):
    w, theta = make_symbols(n, n)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    H = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(H)
    return w, theta, phi, H, C


def test_A3_hessian_equals_negative_coupling() -> None:
    w, theta, phi, H, C = _build_tdc_objects()
    residual = sp.simplify(H + C)
    assert residual == sp.zeros(*H.shape)


def test_A3_coupling_quadratic_form_decomposition() -> None:
    w, theta, phi, H, C = _build_tdc_objects(n=3)

    q, alpha, c = sp.symbols("q alpha c", real=True)
    x0, x1, x2 = sp.symbols("x0 x1 x2", real=True)
    x = sp.Matrix([x0, x1, x2])

    lhs = sp.simplify((x.T * C * x)[0, 0])
    rhs = sp.simplify(
        (q + alpha * theta[0, 0]) * x0**2
        + (q + alpha * theta[1, 0]) * x1**2
        + (q + alpha * theta[2, 0]) * x2**2
        + c * (x0 - x1) ** 2
        + c * (x1 - x2) ** 2
    )

    assert sp.simplify(lhs - rhs) == 0


def test_A3_negative_definiteness_on_admissible_numeric_sample() -> None:
    w, theta, phi, H, C = _build_tdc_objects(n=3)

    q, alpha, c = sp.symbols("q alpha c", real=True)

    subs = {
        theta[0, 0]: 1,
        theta[1, 0]: 2,
        theta[2, 0]: 3,
        q: 2,
        alpha: sp.Rational(1, 5),
        c: sp.Rational(1, 2),
    }

    H_num = sp.Matrix(H.subs(subs))
    C_num = sp.Matrix(C.subs(subs))

    c_eigs = [_real_float(ev) for ev in C_num.eigenvals().keys()]
    h_eigs = [_real_float(ev) for ev in H_num.eigenvals().keys()]

    assert all(ev > 0.0 for ev in c_eigs)
    assert all(ev < 0.0 for ev in h_eigs)


def test_A3_local_uniqueness_support_via_nonsingularity() -> None:
    w, theta, phi, H, C = _build_tdc_objects(n=3)

    q, alpha, c = sp.symbols("q alpha c", real=True)

    subs = {
        theta[0, 0]: 1,
        theta[1, 0]: 2,
        theta[2, 0]: 3,
        q: 2,
        alpha: sp.Rational(1, 5),
        c: sp.Rational(1, 2),
    }

    det_H = sp.simplify(H.subs(subs).det())
    det_C = sp.simplify(C.subs(subs).det())

    assert det_H != 0
    assert det_C != 0
