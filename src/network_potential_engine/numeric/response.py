from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class ResponseResult:
    """
    Numerical comparative-statics response data at a fixed equilibrium.

    Attributes
    ----------
    response_matrix
        The response matrix R = C^{-1} H_{w,theta}.
    hessian_matrix
        The raw Hessian H evaluated at (w_star, theta).
    coupling_matrix
        The coupling operator C = -H evaluated at (w_star, theta).
    mixed_block
        The mixed derivative block H_{w,theta} evaluated at (w_star, theta).
    """
    response_matrix: np.ndarray
    hessian_matrix: np.ndarray
    coupling_matrix: np.ndarray
    mixed_block: np.ndarray


def compute_response(
    hessian_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    mixed_block_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    w_star: np.ndarray | list[float],
    theta_values: np.ndarray | list[float],
) -> ResponseResult:
    """
    Compute the response matrix

        R = C^{-1} H_{w,theta}

    at a fixed equilibrium point (w_star, theta), where C = -H.

    Parameters
    ----------
    hessian_fn
        Numerical function returning the Hessian H(w, theta).
    mixed_block_fn
        Numerical function returning H_{w,theta}(w, theta).
    w_star
        Equilibrium point at which to evaluate the response.
    theta_values
        Fixed parameter values.

    Returns
    -------
    ResponseResult
        Structured response data.
    """
    w_arr = np.asarray(w_star, dtype=float).reshape(-1)
    theta_arr = np.asarray(theta_values, dtype=float).reshape(-1)

    hessian = np.asarray(hessian_fn(w_arr, theta_arr), dtype=float)
    mixed_block = np.asarray(mixed_block_fn(w_arr, theta_arr), dtype=float)

    if hessian.ndim != 2:
        raise ValueError("hessian_fn must return a 2D array.")
    if mixed_block.ndim != 2:
        raise ValueError("mixed_block_fn must return a 2D array.")
    if hessian.shape[0] != hessian.shape[1]:
        raise ValueError("Hessian matrix must be square.")
    if hessian.shape[0] != mixed_block.shape[0]:
        raise ValueError("Hessian and mixed block must have compatible shapes.")

    coupling = -hessian

    # Solve C X = H_{w,theta} for X rather than forming inv(C) explicitly.
    response = np.linalg.solve(coupling, mixed_block)

    return ResponseResult(
        response_matrix=response,
        hessian_matrix=hessian,
        coupling_matrix=coupling,
        mixed_block=mixed_block,
    )
