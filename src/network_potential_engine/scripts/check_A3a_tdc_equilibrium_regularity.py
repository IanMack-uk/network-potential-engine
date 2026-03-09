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
from network_potential_engine.symbolic.operators import (
    coupling_operator_from_hessian,
    response_operator,
)


def build_tdc_objects(n: int = 3) -> tuple[sp.Matrix, sp.Matrix, sp.Expr, sp.Matrix, sp.Matrix, sp.Matrix]:
    """
    Construct the symbolic TDC objects needed for A3.
    Returns (w, theta, phi, F, C, H_wtheta).
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
    F = gradient_of_potential(phi, w)
    H = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(H)
    H_wtheta = mixed_derivative_from_potential(phi, w, theta)

    return w, theta, phi, F, C, H_wtheta


def check_equilibrium_branch_is_symbolically_constructible() -> None:
    """
    Verify that the symbolic equilibrium branch
        w*(theta) = C(theta)^(-1) theta
    can be constructed.
    """
    w, theta, phi, F, C, H_wtheta = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    assert w_star.shape == (w.rows, 1), (
        f"Equilibrium branch has incorrect shape: {w_star.shape}"
    )


def check_equilibrium_branch_is_differentiable() -> None:
    """
    Verify that D_theta w*(theta) can be constructed symbolically.
    """
    w, theta, phi, F, C, H_wtheta = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    jac = sp.simplify(w_star.jacobian(list(theta)))

    assert jac.shape == (w.rows, theta.rows), (
        f"Jacobian of equilibrium branch has incorrect shape: {jac.shape}"
    )


def check_response_identity_at_equilibrium() -> None:
    """
    Verify the A3/TDC response identity
        D_theta w*(theta) = C(theta)^(-1) H_wtheta(w*(theta), theta).
    """
    w, theta, phi, F, C, H_wtheta = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    jac = sp.simplify(w_star.jacobian(list(theta)))

    substitutions = {w[i, 0]: w_star[i, 0] for i in range(w.rows)}
    H_wtheta_at_equilibrium = sp.simplify(H_wtheta.subs(substitutions))

    response = response_operator(C, H_wtheta_at_equilibrium)

    residual = sp.simplify(jac - response)
    assert residual == sp.zeros(*jac.shape), (
        "A3a response identity failed: D_theta w*(theta) != C(theta)^(-1) H_wtheta(w*(theta), theta)."
    )


def check_equilibrium_branch_remains_stationary_after_differentiation_setup() -> None:
    """
    Reconfirm the A2 stationarity condition while setting up A3:
        F(w*(theta), theta) = 0.
    """
    w, theta, phi, F, C, H_wtheta = build_tdc_objects()

    w_star = sp.simplify(C.inv() * theta)
    substitutions = {w[i, 0]: w_star[i, 0] for i in range(w.rows)}

    residual = sp.simplify(F.subs(substitutions))
    assert residual == sp.zeros(*F.shape), (
        "Equilibrium branch does not satisfy stationarity."
    )


def run_all_checks() -> None:
    print("Running A3a equilibrium regularity checks (TDC model)")

    check_equilibrium_branch_is_symbolically_constructible()
    print("✓ symbolic equilibrium branch constructed")

    check_equilibrium_branch_is_differentiable()
    print("✓ equilibrium branch differentiability verified symbolically")

    check_equilibrium_branch_remains_stationary_after_differentiation_setup()
    print("✓ stationarity of equilibrium branch reconfirmed")

    check_response_identity_at_equilibrium()
    print("✓ Dθw*(θ) = C(θ)^(-1) H_wθ(w*(θ), θ) verified")

    print("A3a checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
