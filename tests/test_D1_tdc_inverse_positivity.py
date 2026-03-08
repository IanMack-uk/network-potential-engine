from __future__ import annotations

import numpy as np
import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def _tdc_coupling_matrix_numeric(
    theta_values: np.ndarray,
    *,
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    coupling_weight: float,
) -> np.ndarray:
    n = int(theta_values.shape[0])
    w, theta = make_symbols(n, n)
    q, alpha, c = sp.symbols("q alpha c", real=True)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    hess = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hess)

    theta_syms = [theta[i, 0] for i in range(theta.rows)]

    coupling_fn = sp.lambdify(
        [*theta_syms, q, alpha, c],
        coupling,
        "numpy",
    )

    coupling_numeric = np.asarray(
        coupling_fn(
            *list(theta_values),
            float(base_quadratic_weight),
            float(theta_curvature_weight),
            float(coupling_weight),
        ),
        dtype=float,
    )

    return coupling_numeric


def test_D1_tdc_inverse_positivity_holds_for_representative_theta() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    coupling = _tdc_coupling_matrix_numeric(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )

    inv_coupling = np.linalg.inv(coupling)

    tol = 1e-12
    assert float(np.min(inv_coupling)) >= -tol
