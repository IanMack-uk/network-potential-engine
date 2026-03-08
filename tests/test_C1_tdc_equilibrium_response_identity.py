from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_from_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian, response_operator
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def _build_tdc_objects(
    n: int = 3,
) -> tuple[sp.Matrix, sp.Matrix, sp.Expr, sp.Matrix, sp.Matrix, sp.Matrix]:
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
    H_wtheta = mixed_derivative_from_potential(phi, w, theta)

    return w, theta, phi, F, C, H_wtheta


def test_C1_response_identity_holds_at_equilibrium() -> None:
    w, theta, phi, F, C, H_wtheta = _build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    jac = sp.simplify(w_star.jacobian(list(theta)))

    substitutions = {w[i, 0]: w_star[i, 0] for i in range(w.rows)}
    H_wtheta_at_equilibrium = sp.simplify(H_wtheta.subs(substitutions))

    response = response_operator(C, H_wtheta_at_equilibrium)
    residual = sp.simplify(jac - response)

    assert residual == sp.zeros(*jac.shape)
