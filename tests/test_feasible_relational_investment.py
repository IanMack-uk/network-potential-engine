import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.constraints.feasible_relational_investment import (
    check_capacity_from_edge_vector,
    check_row_sum_capacity,
)
from network_potential_engine.graph.primitives import edge_index_from_edges, weight_vector_to_matrix


def test_check_row_sum_capacity_holds_when_within_limits() -> None:
    W = np.array(
        [
            [0.0, 1.0, 0.5],
            [0.0, 0.0, 2.0],
            [0.0, 0.0, 0.0],
        ]
    )
    r = np.array([2.0, 3.0, 0.0])

    result = check_row_sum_capacity(W, r)

    assert result.holds is True
    assert np.all(result.margins >= 0.0)


def test_check_row_sum_capacity_fails_when_exceeds_limits() -> None:
    W = np.array(
        [
            [0.0, 1.0, 0.5],
            [0.0, 0.0, 2.0],
            [0.0, 0.0, 0.0],
        ]
    )
    r = np.array([1.4, 3.0, 0.0])

    result = check_row_sum_capacity(W, r)

    assert result.holds is False
    assert result.margins[0] < 0.0


def test_edge_vector_capacity_check_matches_matrix_check() -> None:
    n_nodes = 3
    edges = {(0, 1), (0, 2), (1, 2)}
    idx = edge_index_from_edges(edges)

    # Edge weights aligned with the deterministic ordering used by edge_index_from_edges.
    w = np.array([1.0, 0.5, 2.0], dtype=float)
    W = weight_vector_to_matrix(w, idx, n_nodes=n_nodes)

    r = np.array([2.0, 2.0, 0.0], dtype=float)

    mat_result = check_row_sum_capacity(W, r)
    vec_result = check_capacity_from_edge_vector(w, idx, r, n_nodes)

    assert mat_result.holds == vec_result.holds
    assert np.allclose(mat_result.margins, vec_result.margins)


def test_edge_vector_capacity_check_rejects_wrong_length() -> None:
    n_nodes = 3
    edges = {(0, 1), (1, 2)}
    idx = edge_index_from_edges(edges)

    w = np.array([1.0, 2.0, 3.0], dtype=float)
    r = np.array([10.0, 10.0, 10.0], dtype=float)

    with pytest.raises(ValueError, match="length equal to number of edges"):
        check_capacity_from_edge_vector(w, idx, r, n_nodes)
