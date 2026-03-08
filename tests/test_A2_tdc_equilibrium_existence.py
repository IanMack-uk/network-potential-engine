from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian


def _build_tdc_objects(n: int = 3) -> tuple[sp.Matrix, sp.Matrix, sp.Expr, sp.Matrix, sp.Matrix]:
    w, theta = make_symbols(n, n)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    F = gradient_of_potential(phi, w)
    H = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(H)

    return w, theta, phi, F, C


def test_A2_equilibrium_operator_has_tdc_form() -> None:
    w, theta, phi, F, C = _build_tdc_objects()
    residual = sp.simplify(F - (theta - C * w))
    assert residual == sp.zeros(*F.shape)


def test_A2_symbolic_equilibrium_branch_has_correct_shape() -> None:
    w, theta, phi, F, C = _build_tdc_objects()
    w_star = sp.simplify(C.inv() * theta)
    assert w_star.shape == (w.rows, 1)


def test_A2_equilibrium_satisfies_stationarity() -> None:
    w, theta, phi, F, C = _build_tdc_objects()
    w_star = sp.simplify(C.inv() * theta)

    substitutions = {w[i, 0]: w_star[i, 0] for i in range(w.rows)}
    residual = sp.simplify(F.subs(substitutions))

    assert residual == sp.zeros(*F.shape)


def test_A2_equilibrium_equation_matches_matrix_form() -> None:
    w, theta, phi, F, C = _build_tdc_objects()
    w_star = sp.simplify(C.inv() * theta)

    residual = sp.simplify(C * w_star - theta)
    assert residual == sp.zeros(*theta.shape)
