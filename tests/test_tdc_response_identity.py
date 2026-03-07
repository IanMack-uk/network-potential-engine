import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_block
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.tdc_equilibrium import (
    tdc_symbolic_equilibrium,
)


def test_tdc_response_identity_matches_jacobian_of_symbolic_equilibrium() -> None:
    w, theta = make_symbols(3, 3)

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

    # Symbolic equilibrium map w*(theta)
    equilibrium = tdc_symbolic_equilibrium(phi, w, theta)

    # Left-hand side: D_theta w*(theta)
    lhs = equilibrium.jacobian(list(theta))

    # Right-hand side: C(theta)^(-1) H_{w,theta}(w*(theta), theta)
    hessian = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hessian)

    grad = gradient_of_potential(phi, w)
    mixed_block = mixed_derivative_block(grad, theta)

    substitutions = {w[i, 0]: equilibrium[i, 0] for i in range(w.rows)}
    mixed_at_equilibrium = sp.simplify(mixed_block.subs(substitutions))

    rhs = sp.simplify(coupling.inv() * mixed_at_equilibrium)

    assert sp.simplify(lhs - rhs) == sp.zeros(3, 3)


def test_tdc_response_identity_matrix_has_correct_shape() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    equilibrium = tdc_symbolic_equilibrium(phi, w, theta)
    jacobian = equilibrium.jacobian(list(theta))

    assert isinstance(jacobian, sp.MatrixBase)
    assert jacobian.shape == (3, 3)