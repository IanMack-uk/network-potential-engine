from __future__ import annotations

import numpy as np
import sympy as sp

from network_potential_engine.theorem.tdc_local_theorem import is_coordinatewise_ordered
from network_potential_engine.theorem.tdc_segment import check_tdc_segment_in_region
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
    coupling_fn = sp.lambdify([
        *theta_syms,
        q,
        alpha,
        c,
    ], coupling, "numpy")

    return np.asarray(
        coupling_fn(
            *list(theta_values),
            float(base_quadratic_weight),
            float(theta_curvature_weight),
            float(coupling_weight),
        ),
        dtype=float,
    )


def run_all_checks() -> None:
    theta_left = np.array([0.2, 0.1, 0.0], dtype=float)
    theta_right = np.array([0.3, 0.2, 0.1], dtype=float)

    assert is_coordinatewise_ordered(theta_left, theta_right)

    seg = check_tdc_segment_in_region(
        theta_left,
        theta_right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )
    assert seg.segment_in_region is True

    coupling_left = _tdc_coupling_matrix_numeric(
        theta_left,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    coupling_right = _tdc_coupling_matrix_numeric(
        theta_right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )

    w_left = np.linalg.solve(coupling_left, theta_left)
    w_right = np.linalg.solve(coupling_right, theta_right)

    tol = 1e-10
    assert bool(np.all(w_right - w_left >= -tol))

    print("Running E3 local weak ordering checks (TDC model)")
    print("✓ endpoint order holds")
    print("✓ segment certificate holds")
    print("✓ observed equilibrium ordering holds for the representative pair")
    print("E3 checks completed successfully")


if __name__ == "__main__":
    run_all_checks()
