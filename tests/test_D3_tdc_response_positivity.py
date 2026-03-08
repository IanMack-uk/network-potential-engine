from __future__ import annotations

import numpy as np
import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.mixed_derivatives import mixed_derivative_from_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential
from network_potential_engine.symbolic.symbols import make_symbols


def _tdc_coupling_and_mixed_block_numeric(
    theta_values: np.ndarray,
    *,
    base_quadratic_weight: float,
    theta_curvature_weight: float,
    coupling_weight: float,
) -> tuple[np.ndarray, np.ndarray]:
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
    mixed = mixed_derivative_from_potential(phi, w, theta)

    theta_syms = [theta[i, 0] for i in range(theta.rows)]
    w_syms = [w[i, 0] for i in range(w.rows)]

    coupling_fn = sp.lambdify([
        *theta_syms,
        q,
        alpha,
        c,
    ], coupling, "numpy")

    mixed_fn = sp.lambdify([
        *w_syms,
        *theta_syms,
        q,
        alpha,
        c,
    ], mixed, "numpy")

    coupling_numeric = np.asarray(
        coupling_fn(
            *list(theta_values),
            float(base_quadratic_weight),
            float(theta_curvature_weight),
            float(coupling_weight),
        ),
        dtype=float,
    )

    w_star = np.linalg.solve(coupling_numeric, theta_values)

    mixed_numeric = np.asarray(
        mixed_fn(
            *list(w_star),
            *list(theta_values),
            float(base_quadratic_weight),
            float(theta_curvature_weight),
            float(coupling_weight),
        ),
        dtype=float,
    )

    return coupling_numeric, mixed_numeric


def test_D3_tdc_response_is_entrywise_nonnegative_for_representative_theta() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)

    coupling, mixed = _tdc_coupling_and_mixed_block_numeric(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )

    response = np.linalg.solve(coupling, mixed)

    tol = 1e-12
    assert float(np.min(response)) >= -tol
