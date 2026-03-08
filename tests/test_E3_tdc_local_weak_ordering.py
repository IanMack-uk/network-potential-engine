import numpy as np

from network_potential_engine.theorem.tdc_local_theorem import (
    check_tdc_local_theorem_hypothesis,
)
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
    import sympy as sp

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


def test_E3_tdc_local_weak_ordering_observed_for_representative_pair() -> None:
    theta_left = np.array([0.2, 0.1, 0.0], dtype=float)
    theta_right = np.array([0.3, 0.2, 0.1], dtype=float)

    check = check_tdc_local_theorem_hypothesis(
        theta_left,
        theta_right,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )
    assert check.theorem_hypothesis_holds is True

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
