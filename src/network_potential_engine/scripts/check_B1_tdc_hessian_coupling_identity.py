from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def check_tdc_coupling_operator_is_negative_hessian() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1,
        theta_curvature_weight=sp.Rational(1, 5),
        coupling_weight=sp.Rational(1, 2),
    )

    hess = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hess)

    residual = sp.simplify(coupling + hess)
    assert residual == sp.zeros(*hess.shape)


def run_all_checks() -> None:
    print("Running B1 Hessian–Coupling identity checks (TDC model)")

    check_tdc_coupling_operator_is_negative_hessian()
    print("✓ C(w,θ) = −H(w,θ) verified (TDC instance)")

    print("B1 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
