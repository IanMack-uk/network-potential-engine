from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

import numpy as np

Edge = Tuple[int, int]


@dataclass(frozen=True)
class Graph:
    """Lightweight graph container for Step 1(1) representation.

    Nodes are represented implicitly as integer labels in {0, ..., n_nodes-1}.
    Edges are represented as ordered pairs (i, j) using the same integer labels.
    """

    n_nodes: int
    edges: FrozenSet[Edge]
    directed: bool = True

    def __post_init__(self) -> None:
        if self.n_nodes <= 0:
            raise ValueError("n_nodes must be positive")
        for (i, j) in self.edges:
            if not (0 <= i < self.n_nodes) or not (0 <= j < self.n_nodes):
                raise ValueError("edge contains node index outside [0, n_nodes)")
        if not self.directed:
            missing = [(j, i) for (i, j) in self.edges if (j, i) not in self.edges]
            if missing:
                raise ValueError(
                    "undirected graphs require symmetric edge set: missing reverse edges for "
                    + str(missing[:10])
                    + ("..." if len(missing) > 10 else "")
                )


def edge_index_from_edges(edges: Iterable[Edge]) -> Dict[Edge, int]:
    """Create a deterministic edge->index mapping.

    The mapping is defined by sorting edges lexicographically.
    """

    edge_list = sorted(set(edges))
    return {e: k for k, e in enumerate(edge_list)}


def support_mask(edges: Iterable[Edge], n_nodes: int) -> np.ndarray:
    """Return a boolean support mask M where M[i,j] is True iff (i,j) is an edge."""

    if n_nodes <= 0:
        raise ValueError("n_nodes must be positive")

    mask = np.zeros((n_nodes, n_nodes), dtype=bool)
    for (i, j) in set(edges):
        if not (0 <= i < n_nodes) or not (0 <= j < n_nodes):
            raise ValueError("edge contains node index outside [0, n_nodes)")
        mask[i, j] = True
    return mask


def weight_vector_to_matrix(
    w: Sequence[float], edge_index: Mapping[Edge, int], n_nodes: int
) -> np.ndarray:
    """Convert an edge-indexed weight vector into a matrix W with zero off-support entries."""

    if n_nodes <= 0:
        raise ValueError("n_nodes must be positive")

    w_arr = np.asarray(w, dtype=float)
    if w_arr.ndim != 1:
        raise ValueError("w must be a 1D sequence")

    n_edges = len(edge_index)
    if w_arr.shape[0] != n_edges:
        raise ValueError(f"w has length {w_arr.shape[0]} but edge_index has {n_edges} edges")

    W = np.zeros((n_nodes, n_nodes), dtype=float)
    for (i, j), k in edge_index.items():
        if not (0 <= i < n_nodes) or not (0 <= j < n_nodes):
            raise ValueError("edge_index contains node index outside [0, n_nodes)")
        if not (0 <= k < n_edges):
            raise ValueError("edge_index contains invalid index")
        W[i, j] = float(w_arr[k])
    return W


def weight_matrix_to_vector(
    W: np.ndarray, edge_index: Mapping[Edge, int], *, tol: float = 0.0
) -> np.ndarray:
    """Convert a matrix representation to an edge-indexed vector.

    Entries not in edge_index must be zero (within tol), enforcing the support convention.
    """

    W_arr = np.asarray(W, dtype=float)
    if W_arr.ndim != 2 or W_arr.shape[0] != W_arr.shape[1]:
        raise ValueError("W must be a square 2D array")

    n_nodes = W_arr.shape[0]
    n_edges = len(edge_index)
    w = np.zeros((n_edges,), dtype=float)

    supported = np.zeros_like(W_arr, dtype=bool)
    for (i, j), k in edge_index.items():
        if not (0 <= i < n_nodes) or not (0 <= j < n_nodes):
            raise ValueError("edge_index contains node index outside W dimensions")
        if not (0 <= k < n_edges):
            raise ValueError("edge_index contains invalid index")
        w[k] = W_arr[i, j]
        supported[i, j] = True

    if tol < 0:
        raise ValueError("tol must be nonnegative")

    if tol == 0.0:
        off_support_nonzero = np.any(W_arr[~supported] != 0.0)
    else:
        off_support_nonzero = np.any(np.abs(W_arr[~supported]) > tol)

    if off_support_nonzero:
        raise ValueError("W has nonzero entries off the declared edge support")

    return w
