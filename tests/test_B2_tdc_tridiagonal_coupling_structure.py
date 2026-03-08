import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def test_tdc_coupling_operator_is_tridiagonal() -> None:
    w, theta = make_symbols(5, 5)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    hess = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hess)

    n = coupling.rows
    assert coupling.cols == n

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1:
                assert sp.simplify(coupling[i, j]) == 0
