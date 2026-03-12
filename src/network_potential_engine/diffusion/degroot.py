from __future__ import annotations

import numpy as np


def transition_matrix_from_adjacency(
    A: np.ndarray,
    *,
    add_self_loops_for_dangling: bool = True,
) -> np.ndarray:
    A_arr = np.asarray(A, dtype=float)
    if A_arr.ndim != 2 or A_arr.shape[0] != A_arr.shape[1]:
        raise ValueError("A must be a square 2D array")

    if np.any(A_arr < 0.0):
        raise ValueError("A must be entrywise nonnegative")

    n = int(A_arr.shape[0])
    row_sums = np.sum(A_arr, axis=1)

    if add_self_loops_for_dangling:
        dangling = row_sums == 0.0
        if np.any(dangling):
            A_arr = A_arr.copy()
            A_arr[dangling, dangling] = 1.0
            row_sums = np.sum(A_arr, axis=1)

    if np.any(row_sums == 0.0):
        raise ValueError("A has a zero row; cannot row-normalize")

    P = A_arr / row_sums[:, None]
    return np.asarray(P, dtype=float)


def degroot_step(P: np.ndarray, x: np.ndarray) -> np.ndarray:
    P_arr = np.asarray(P, dtype=float)
    x_arr = np.asarray(x, dtype=float)

    if P_arr.ndim != 2 or P_arr.shape[0] != P_arr.shape[1]:
        raise ValueError("P must be a square 2D array")

    if x_arr.ndim != 1:
        raise ValueError("x must be a 1D vector")

    if x_arr.shape[0] != P_arr.shape[0]:
        raise ValueError("x has incompatible dimension")

    return P_arr @ x_arr


def degroot_step_with_receptivity(P: np.ndarray, x: np.ndarray, rho: np.ndarray) -> np.ndarray:
    P_arr = np.asarray(P, dtype=float)
    x_arr = np.asarray(x, dtype=float)
    rho_arr = np.asarray(rho, dtype=float)

    if rho_arr.ndim != 1:
        raise ValueError("rho must be a 1D vector")
    if x_arr.ndim != 1:
        raise ValueError("x must be a 1D vector")
    if rho_arr.shape != x_arr.shape:
        raise ValueError("rho and x must have the same shape")

    x_next = degroot_step(P_arr, x_arr)
    return rho_arr * x_next


def degroot_simulate(P: np.ndarray, x0: np.ndarray, n_steps: int) -> np.ndarray:
    if n_steps < 0:
        raise ValueError("n_steps must be nonnegative")

    P_arr = np.asarray(P, dtype=float)
    x = np.asarray(x0, dtype=float)

    if x.ndim != 1:
        raise ValueError("x0 must be a 1D vector")

    if P_arr.ndim != 2 or P_arr.shape[0] != P_arr.shape[1]:
        raise ValueError("P must be a square 2D array")

    if x.shape[0] != P_arr.shape[0]:
        raise ValueError("x0 has incompatible dimension")

    xs = np.zeros((n_steps + 1, x.shape[0]), dtype=float)
    xs[0] = x

    for t in range(n_steps):
        x = P_arr @ x
        xs[t + 1] = x

    return xs


def degroot_simulate_with_receptivity(
    P: np.ndarray,
    x0: np.ndarray,
    rho: np.ndarray,
    n_steps: int,
) -> np.ndarray:
    if n_steps < 0:
        raise ValueError("n_steps must be nonnegative")

    P_arr = np.asarray(P, dtype=float)
    x = np.asarray(x0, dtype=float)
    rho_arr = np.asarray(rho, dtype=float)

    if rho_arr.ndim != 1:
        raise ValueError("rho must be a 1D vector")
    if x.ndim != 1:
        raise ValueError("x0 must be a 1D vector")
    if rho_arr.shape != x.shape:
        raise ValueError("rho and x0 must have the same shape")

    if P_arr.ndim != 2 or P_arr.shape[0] != P_arr.shape[1]:
        raise ValueError("P must be a square 2D array")

    if x.shape[0] != P_arr.shape[0]:
        raise ValueError("x0 has incompatible dimension")

    xs = np.zeros((n_steps + 1, x.shape[0]), dtype=float)
    xs[0] = x

    for t in range(n_steps):
        x = rho_arr * (P_arr @ x)
        xs[t + 1] = x

    return xs
