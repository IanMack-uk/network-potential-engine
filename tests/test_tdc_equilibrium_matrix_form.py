import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.tdc_equilibrium import (
    tdc_equilibrium_residual,
    tdc_symbolic_equilibrium,
)


def test_tdc_symbolic_equilibrium_has_column_shape() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    equilibrium = tdc_symbolic_equilibrium(phi, w, theta)

    assert isinstance(equilibrium, sp.MatrixBase)
    assert equilibrium.shape == (3, 1)


def test_tdc_symbolic_equilibrium_equals_c_inverse_theta() -> None:
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

    hessian = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hessian)

    equilibrium = tdc_symbolic_equilibrium(phi, w, theta)
    expected = sp.simplify(coupling.inv() * theta)

    assert sp.simplify(equilibrium - expected) == sp.zeros(3, 1)


def test_tdc_symbolic_equilibrium_has_zero_residual() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    equilibrium = tdc_symbolic_equilibrium(phi, w, theta)
    residual = tdc_equilibrium_residual(phi, w, theta, equilibrium)

    assert sp.simplify(residual) == sp.zeros(3, 1)
