import sympy as sp

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.equilibrium import (
    bootstrap_symbolic_equilibrium,
    equilibrium_residual,
    symbolic_equilibrium_from_coupling,
    symbolic_equilibrium_from_hessian,
)


def test_symbolic_equilibrium_has_column_shape() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)

    equilibrium = bootstrap_symbolic_equilibrium(phi, w, theta)

    assert isinstance(equilibrium, sp.MatrixBase)
    assert equilibrium.shape == (3, 1)


def test_symbolic_equilibrium_from_hessian_matches_coupling_version() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    hessian = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hessian)

    eq_from_hessian = symbolic_equilibrium_from_hessian(hessian, theta)
    eq_from_coupling = symbolic_equilibrium_from_coupling(coupling, theta)

    assert sp.simplify(eq_from_hessian - eq_from_coupling) == sp.zeros(3, 1)


def test_bootstrap_symbolic_equilibrium_has_zero_residual() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)

    equilibrium = bootstrap_symbolic_equilibrium(phi, w, theta)
    residual = equilibrium_residual(phi, w, theta, equilibrium)

    assert sp.simplify(residual) == sp.zeros(3, 1)
