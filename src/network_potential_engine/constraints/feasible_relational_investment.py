from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence, Tuple

import numpy as np

Edge = Tuple[int, int]


@dataclass(frozen=True)
class CapacityCheck:
    margins: np.ndarray
    holds: bool


def row_sum_capacity_margins(
    W: np.ndarray | Sequence[Sequence[float]],
    r: np.ndarray | Sequence[float],
) -> np.ndarray:
    W_arr = np.asarray(W, dtype=float)
    if W_arr.ndim != 2 or W_arr.shape[0] != W_arr.shape[1]:
        raise ValueError("W must be a square 2D array")

    r_arr = np.asarray(r, dtype=float).reshape(-1)
    if r_arr.shape[0] != W_arr.shape[0]:
        raise ValueError("r must have length equal to number of nodes")

    row_sums = np.sum(W_arr, axis=1)
    return r_arr - row_sums


def check_row_sum_capacity(
    W: np.ndarray | Sequence[Sequence[float]],
    r: np.ndarray | Sequence[float],
    *,
    atol: float = 0.0,
) -> CapacityCheck:
    if atol < 0:
        raise ValueError("atol must be nonnegative")

    margins = row_sum_capacity_margins(W, r)
    holds = bool(np.all(margins >= -float(atol)))
    return CapacityCheck(margins=margins, holds=holds)


def check_capacity_from_edge_vector(
    w: np.ndarray | Sequence[float],
    edge_index: Mapping[Edge, int],
    r: np.ndarray | Sequence[float],
    n_nodes: int,
    *,
    atol: float = 0.0,
) -> CapacityCheck:
    if n_nodes <= 0:
        raise ValueError("n_nodes must be positive")
    if atol < 0:
        raise ValueError("atol must be nonnegative")

    w_arr = np.asarray(w, dtype=float).reshape(-1)
    if w_arr.shape[0] != len(edge_index):
        raise ValueError("w must have length equal to number of edges")

    r_arr = np.asarray(r, dtype=float).reshape(-1)
    if r_arr.shape[0] != n_nodes:
        raise ValueError("r must have length equal to n_nodes")

    row_sums = np.zeros((n_nodes,), dtype=float)
    for (i, _j), k in edge_index.items():
        if not (0 <= i < n_nodes):
            raise ValueError("edge_index contains node index outside [0, n_nodes)")
        if not (0 <= k < w_arr.shape[0]):
            raise ValueError("edge_index contains invalid index")
        row_sums[i] += w_arr[k]

    margins = r_arr - row_sums
    holds = bool(np.all(margins >= -float(atol)))
    return CapacityCheck(margins=margins, holds=holds)
