from __future__ import annotations

import numpy as np

from network_potential_engine.numeric.green_operator import GreenOperator, certify_green_operator


def laplacian_from_adjacency(A: np.ndarray) -> np.ndarray:
    A_arr = np.asarray(A, dtype=float)
    if A_arr.ndim != 2 or A_arr.shape[0] != A_arr.shape[1]:
        raise ValueError("A must be a square 2D array")
    if np.any(A_arr < 0.0):
        raise ValueError("A must be entrywise nonnegative")

    degrees = np.sum(A_arr, axis=1)
    D = np.diag(degrees)
    return D - A_arr


def coupling_from_laplacian(L: np.ndarray, tau: float) -> np.ndarray:
    if tau <= 0.0:
        raise ValueError("tau must be positive")

    L_arr = np.asarray(L, dtype=float)
    if L_arr.ndim != 2 or L_arr.shape[0] != L_arr.shape[1]:
        raise ValueError("L must be a square 2D array")

    n = int(L_arr.shape[0])
    return np.eye(n, dtype=float) + float(tau) * L_arr


def K_from_graph(A: np.ndarray, tau: float) -> GreenOperator:
    L = laplacian_from_adjacency(A)
    C = coupling_from_laplacian(L, tau=tau)
    return certify_green_operator(C)


def propagated_value_total(K: GreenOperator, s: np.ndarray) -> np.ndarray:
    return K.apply(np.asarray(s, dtype=float))


def propagated_value_from_others(K: GreenOperator, s: np.ndarray) -> np.ndarray:
    s_arr = np.asarray(s, dtype=float)
    v_total = K.apply(s_arr)
    K_diag = np.diag(K.matrix())
    return v_total - K_diag * s_arr


def propagated_value_outgoing_total(K: GreenOperator, s: np.ndarray) -> np.ndarray:
    """Compute outgoing (impact) value v_out = G^T s.

    Interprets (G^T s)_i as the total amount of value originating at node i that reaches
    the rest of the network through the propagation operator.
    """

    s_arr = np.asarray(s, dtype=float)

    C = np.asarray(K.coupling_matrix, dtype=float)
    if C.ndim == 2 and np.allclose(C, C.T, atol=1e-12, rtol=0.0):
        # Symmetric coupling => symmetric Green operator.
        return K.apply(s_arr)

    Gt = K.matrix().T
    return np.asarray(Gt @ s_arr, dtype=float)


def propagated_value_outgoing_to_others(K: GreenOperator, s: np.ndarray) -> np.ndarray:
    """Outgoing value excluding the self contribution.

    Defined by v_out_to_others = G^T s - diag(G) * s.
    """

    s_arr = np.asarray(s, dtype=float)
    v_out_total = propagated_value_outgoing_total(K, s_arr)
    G_diag = np.diag(K.matrix())
    return v_out_total - G_diag * s_arr
