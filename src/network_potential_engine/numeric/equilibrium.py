from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
from scipy.optimize import root


@dataclass
class EquilibriumResult:
    """
    Result of solving F(w, theta) = 0 for w.

    Attributes
    ----------
    w_star
        Numerical equilibrium candidate.
    success
        Whether the solver reported success.
    message
        Solver status message.
    residual_norm
        Euclidean norm of F(w_star, theta).
    """
    w_star: np.ndarray
    success: bool
    message: str
    residual_norm: float


def solve_equilibrium(
    gradient_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    theta_values: np.ndarray | list[float],
    w0: np.ndarray | list[float],
    residual_tol: float = 1e-10,
) -> EquilibriumResult:
    """
    Solve the equilibrium condition F(w, theta) = 0 for w at fixed theta.

    Parameters
    ----------
    gradient_fn
        Numerical function returning F(w, theta) as a 1D NumPy array.
    theta_values
        Fixed theta parameter values.
    w0
        Initial guess for the equilibrium solver.

    Returns
    -------
    EquilibriumResult
        Structured result containing the equilibrium candidate and diagnostics.
    """
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)
    w0_arr = np.asarray(w0, dtype=float).reshape(-1)

    def objective(w_values: np.ndarray) -> np.ndarray:
        value = np.asarray(gradient_fn(w_values, theta_arr), dtype=float).reshape(-1)
        return value

    sol = root(objective, w0_arr)
    residual = objective(sol.x)

    residual_norm = float(np.linalg.norm(residual))
    success = bool(sol.success) or residual_norm <= float(residual_tol)

    return EquilibriumResult(
        w_star=np.asarray(sol.x, dtype=float).reshape(-1),
        success=success,
        message=str(sol.message),
        residual_norm=residual_norm,
    )
