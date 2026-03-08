from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import (
    mixed_derivative_from_potential,
)


def _build_tdc_phi(n: int = 3) -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    w, theta = make_symbols(n, n)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )
    return w, theta, phi


def test_gradient_exists_for_tdc_potential() -> None:
    w, theta, phi = _build_tdc_phi()
    grad = gradient_of_potential(phi, w)

    assert isinstance(grad, sp.MatrixBase)
    assert grad.shape == (w.rows, 1)


def test_hessian_exists_for_tdc_potential() -> None:
    w, theta, phi = _build_tdc_phi()
    hess = hessian_of_potential(phi, w)

    assert isinstance(hess, sp.MatrixBase)
    assert hess.shape == (w.rows, w.rows)


def test_mixed_derivative_block_exists_for_tdc_potential() -> None:
    w, theta, phi = _build_tdc_phi()
    mixed = mixed_derivative_from_potential(phi, w, theta)

    assert isinstance(mixed, sp.MatrixBase)
    assert mixed.shape == (w.rows, theta.rows)