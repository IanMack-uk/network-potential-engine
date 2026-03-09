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


def build_tdc_objects(n: int = 3) -> tuple[sp.Matrix, sp.Matrix, sp.Expr, sp.Matrix, sp.Matrix]:
    """
    Construct the symbolic TDC objects needed for A3.

    Returns
    -------
    tuple
        (w, theta, phi, H, C)
    """
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


def check_hessian_equals_negative_coupling() -> None:
    """
    Verify the canonical identity H = -C.
    This is the structural gateway to nondegeneracy in the TDC model.
    """
    w, theta, phi, H, C = build_tdc_objects()
    residual = sp.simplify(H + C)
    assert residual == sp.zeros(*H.shape), "Hessian/coupling sign identity failed."


def check_coupling_quadratic_form_decomposition() -> None:
    """
    Verify the exact TDC quadratic-form identity

        x^T C x
        =
        sum_i (q + alpha*theta_i) x_i^2
        + c * sum_i (x_i - x_{i+1})^2

    for n = 3.

    This is the key algebraic support for positive definiteness of C
    and hence negative definiteness of H = -C.
    """
    w, theta, phi, H, C = build_tdc_objects(n=3)

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

    assert sp.simplify(lhs - rhs) == 0, (
        "Coupling quadratic-form decomposition failed."
    )


def check_negative_definiteness_on_admissible_numeric_sample() -> None:
    """
    Support strict local maximum / stability by checking that the Hessian
    is negative definite on a representative admissible numeric sample.

    This is not the proof itself, but it is strong computational support
    for the TDC instance of A3.
    """
    w, theta, phi, H, C = build_tdc_objects(n=3)

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

    # C should be positive definite, so H = -C negative definite
    c_eigs = [_real_float(ev) for ev in C_num.eigenvals().keys()]
    h_eigs = [_real_float(ev) for ev in H_num.eigenvals().keys()]

    assert all(ev > 0.0 for ev in c_eigs), (
        f"Coupling operator is not positive definite on admissible sample: {c_eigs}"
    )
    assert all(ev < 0.0 for ev in h_eigs), (
        f"Hessian is not negative definite on admissible sample: {h_eigs}"
    )


def check_local_uniqueness_support_via_hessian_nonsingularity() -> None:
    """
    Support local uniqueness by checking that the Hessian is nonsingular
    on a representative admissible numeric sample.
    """
    w, theta, phi, H, C = build_tdc_objects(n=3)

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

    assert det_H != 0, "Hessian is singular on admissible numeric sample."
    assert det_C != 0, "Coupling operator is singular on admissible numeric sample."


def run_all_checks() -> None:
    print("Running A3b interior nondegeneracy checks (TDC model)")

    check_hessian_equals_negative_coupling()
    print("✓ H = -C verified")

    check_coupling_quadratic_form_decomposition()
    print("✓ coupling quadratic-form decomposition verified")

    check_negative_definiteness_on_admissible_numeric_sample()
    print("✓ negative definiteness / local stability supported on admissible sample")

    check_local_uniqueness_support_via_hessian_nonsingularity()
    print("✓ nonsingularity / local uniqueness supported on admissible sample")

    print("A3b checks completed successfully")


if __name__ == "__main__":
    run_all_checks()