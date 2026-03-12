import numpy as np
import pytest

from network_potential_engine.diffusion.node_propagation import (
    K_from_graph,
    coupling_from_laplacian,
    laplacian_from_adjacency,
    propagated_value_from_others,
    propagated_value_outgoing_to_others,
    propagated_value_outgoing_total,
    propagated_value_total,
)
from network_potential_engine.numeric.green_operator import GreenOperator


def test_laplacian_from_adjacency_basic_properties() -> None:
    A = np.array(
        [
            [0.0, 1.0],
            [1.0, 0.0],
        ],
        dtype=float,
    )
    L = laplacian_from_adjacency(A)
    assert np.allclose(L, np.array([[1.0, -1.0], [-1.0, 1.0]]))
    assert np.allclose(np.sum(L, axis=1), np.zeros((2,), dtype=float))


def test_coupling_from_laplacian_rejects_nonpositive_tau() -> None:
    L = np.eye(2, dtype=float)
    with pytest.raises(ValueError, match="tau must be positive"):
        coupling_from_laplacian(L, tau=0.0)


def test_K_from_graph_and_propagated_values_shapes_and_self_exclusion() -> None:
    A = np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=float,
    )
    tau = 1.0
    K = K_from_graph(A, tau=tau)

    s = np.array([1.0, 2.0, 3.0], dtype=float)
    v_total = propagated_value_total(K, s)
    v_others = propagated_value_from_others(K, s)

    assert v_total.shape == (3,)
    assert v_others.shape == (3,)

    # By definition v_others = v_total - diag(K) * s
    K_diag = np.diag(K.matrix())
    assert np.allclose(v_others, v_total - K_diag * s)


def test_outgoing_equals_incoming_in_symmetric_kernel_regime() -> None:
    A = np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=float,
    )
    K = K_from_graph(A, tau=1.0)
    s = np.array([1.0, 2.0, 3.0], dtype=float)

    v_in = propagated_value_total(K, s)
    v_out = propagated_value_outgoing_total(K, s)
    assert np.allclose(v_in, v_out)

    v_in_others = propagated_value_from_others(K, s)
    v_out_others = propagated_value_outgoing_to_others(K, s)
    assert np.allclose(v_in_others, v_out_others)


def test_outgoing_differs_from_incoming_for_nonsymmetric_operator() -> None:
    # Construct a simple nonsymmetric coupling matrix.
    C = np.array(
        [
            [2.0, -1.0, 0.0],
            [0.0, 2.0, -1.0],
            [0.0, 0.0, 2.0],
        ],
        dtype=float,
    )
    K = GreenOperator(coupling_matrix=C)
    s = np.array([1.0, 2.0, 3.0], dtype=float)

    v_in = propagated_value_total(K, s)
    v_out = propagated_value_outgoing_total(K, s)

    # In general, G^T s != G s when G is not symmetric.
    assert not np.allclose(v_in, v_out)
