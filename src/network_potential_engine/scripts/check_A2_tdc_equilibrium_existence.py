from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian


def build_tdc_objects(n: int = 3):
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


def check_equilibrium_operator_identity():
    w, theta, phi, F, C = build_tdc_objects()

    residual = sp.simplify(F - (theta - C * w))
    assert residual == sp.zeros(*F.shape)


def check_equilibrium_branch():
    w, theta, phi, F, C = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    assert w_star.shape == (w.rows, 1)


def check_stationarity_condition():
    w, theta, phi, F, C = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)

    substitutions = {w[i, 0]: w_star[i, 0] for i in range(w.rows)}

    residual = sp.simplify(F.subs(substitutions))
    assert residual == sp.zeros(*F.shape)


def check_matrix_equilibrium_equation():
    w, theta, phi, F, C = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)

    residual = sp.simplify(C * w_star - theta)
    assert residual == sp.zeros(*theta.shape)


def run_all_checks():
    print("Running A2 equilibrium checks (TDC model)")

    check_equilibrium_operator_identity()
    print("✓ F = θ − C(θ)w verified")

    check_equilibrium_branch()
    print("✓ symbolic equilibrium branch constructed")

    check_stationarity_condition()
    print("✓ F(w*,θ) = 0 verified")

    check_matrix_equilibrium_equation()
    print("✓ C(θ)w*(θ) = θ verified")

    print("A2 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
