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


def test_tdc_potential_is_polynomial_in_state_and_parameter_variables() -> None:
    w, theta = make_symbols(3, 3)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    vars_all = list(w) + list(theta) + [q, alpha, c]
    poly = sp.Poly(sp.expand(phi), *vars_all)

    assert poly is not None


def test_tdc_gradient_hessian_and_mixed_block_are_polynomial_expressions() -> None:
    w, theta = make_symbols(3, 3)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    grad = gradient_of_potential(phi, w)
    hess = hessian_of_potential(phi, w)
    mixed = mixed_derivative_from_potential(phi, w, theta)

    vars_all = list(w) + list(theta) + [q, alpha, c]

    for expr in list(grad) + list(hess) + list(mixed):
        assert sp.Poly(sp.expand(expr), *vars_all) is not None
