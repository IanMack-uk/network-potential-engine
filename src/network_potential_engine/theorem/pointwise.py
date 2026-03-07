from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from network_potential_engine.numeric.equilibrium import EquilibriumResult, solve_equilibrium
from network_potential_engine.numeric.linear_algebra import (
    diagonal_dominance_margins,
    has_nonpositive_off_diagonals,
    is_strictly_diagonally_dominant,
    is_symmetric,
)
from network_potential_engine.numeric.response import ResponseResult, compute_response


@dataclass
class PointwiseTheoremCheck:
    """
    Structured result for a pointwise theorem-style check at fixed theta.
    """

    equilibrium: EquilibriumResult
    response: ResponseResult
    c_diagonal_dominance_margins: np.ndarray
    c_min_diagonal_dominance_margin: float
    is_c_symmetric: bool
    is_c_strictly_diagonally_dominant: bool
    has_c_nonpositive_off_diagonals: bool
    response_is_entrywise_nonnegative: bool


def is_entrywise_nonnegative(
    matrix: np.ndarray | list[list[float]],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether every entry of a matrix is nonnegative up to tolerance.
    """
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim != 2:
        raise ValueError("matrix must be a 2D array.")

    return bool(np.all(arr >= -tol))


def check_pointwise_conditions(
    gradient_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    hessian_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    mixed_block_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    theta_values: np.ndarray | list[float],
    w0: np.ndarray | list[float],
    residual_tol: float = 1e-10,
    sign_tol: float = 1e-10,
) -> PointwiseTheoremCheck:
    """
    Perform a basic pointwise theorem-style check at fixed theta.
    """
    equilibrium = solve_equilibrium(
        gradient_fn=gradient_fn,
        theta_values=theta_values,
        w0=w0,
        residual_tol=residual_tol,
    )

    response = compute_response(
        hessian_fn=hessian_fn,
        mixed_block_fn=mixed_block_fn,
        w_star=equilibrium.w_star,
        theta_values=theta_values,
    )

    coupling = response.coupling_matrix
    response_matrix = response.response_matrix
    margins = diagonal_dominance_margins(coupling)

    return PointwiseTheoremCheck(
        equilibrium=equilibrium,
        response=response,
        c_diagonal_dominance_margins=margins,
        c_min_diagonal_dominance_margin=float(np.min(margins)),
        is_c_symmetric=is_symmetric(coupling, tol=sign_tol),
        is_c_strictly_diagonally_dominant=is_strictly_diagonally_dominant(
            coupling, tol=sign_tol
        ),
        has_c_nonpositive_off_diagonals=has_nonpositive_off_diagonals(
            coupling, tol=sign_tol
        ),
        response_is_entrywise_nonnegative=is_entrywise_nonnegative(
            response_matrix, tol=sign_tol
        ),
    )
