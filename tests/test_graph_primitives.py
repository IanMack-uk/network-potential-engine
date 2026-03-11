import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.graph.primitives import (
    edge_index_from_edges,
    support_mask,
    weight_matrix_to_vector,
    weight_vector_to_matrix,
)


def test_support_mask_marks_edges_true_and_others_false() -> None:
    edges = {(0, 1), (2, 0)}
    mask = support_mask(edges, n_nodes=3)

    assert mask.shape == (3, 3)
    assert mask.dtype == bool

    assert bool(mask[0, 1]) is True
    assert bool(mask[2, 0]) is True

    assert bool(mask[0, 0]) is False
    assert bool(mask[1, 0]) is False
    assert bool(mask[1, 2]) is False


def test_vector_matrix_roundtrip_is_identity_on_support() -> None:
    edges = {(0, 1), (1, 2)}
    idx = edge_index_from_edges(edges)
    w = np.array([2.0, 3.0])

    W = weight_vector_to_matrix(w, idx, n_nodes=3)
    w2 = weight_matrix_to_vector(W, idx)

    assert np.allclose(w, w2)


def test_weight_matrix_to_vector_rejects_off_support_nonzero() -> None:
    edges = {(0, 1), (1, 2)}
    idx = edge_index_from_edges(edges)

    W = np.zeros((3, 3), dtype=float)
    W[0, 1] = 2.0
    W[1, 2] = 3.0

    # Off-support nonzero entry
    W[2, 2] = 1.0

    with pytest.raises(ValueError, match="off the declared edge support"):
        weight_matrix_to_vector(W, idx)
