import numpy as np
import pytest

from network_potential_engine.graph.weight_transforms import (
    adjacency_from_frequency,
    symmetrize_adjacency,
)


def test_adjacency_from_frequency_is_log1p_and_rejects_negative() -> None:
    freq = np.array([[0.0, 3.0], [7.0, 0.0]], dtype=float)
    A = adjacency_from_frequency(freq)
    assert np.allclose(A, np.log1p(freq))

    freq_bad = np.array([[0.0, -1.0], [0.0, 0.0]], dtype=float)
    with pytest.raises(ValueError, match="entrywise nonnegative"):
        adjacency_from_frequency(freq_bad)


def test_symmetrize_adjacency_is_average_with_transpose() -> None:
    A = np.array(
        [
            [0.0, 1.0, 2.0],
            [3.0, 0.0, 4.0],
            [5.0, 6.0, 0.0],
        ],
        dtype=float,
    )
    A_sym = symmetrize_adjacency(A)
    assert np.allclose(A_sym, 0.5 * (A + A.T))
    assert np.allclose(A_sym, A_sym.T)
