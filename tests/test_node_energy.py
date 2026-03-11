import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.energy.node_energy import energy_vector


def test_energy_vector_returns_beta0_s_plus_beta1_v() -> None:
    s = np.array([1.0, 2.0, 3.0])
    v = np.array([10.0, 20.0, 30.0])

    E = energy_vector(s, v, beta0=2.0, beta1=0.5)
    assert np.allclose(E, np.array([2.0 * 1.0 + 0.5 * 10.0, 2.0 * 2.0 + 0.5 * 20.0, 2.0 * 3.0 + 0.5 * 30.0]))


def test_energy_vector_special_cases() -> None:
    s = np.array([1.0, 2.0])
    v = np.array([5.0, 7.0])

    assert np.allclose(energy_vector(s, v, beta0=1.0, beta1=0.0), s)
    assert np.allclose(energy_vector(s, v, beta0=0.0, beta1=1.0), v)


def test_energy_vector_rejects_shape_mismatch() -> None:
    s = np.array([1.0, 2.0])
    v = np.array([1.0, 2.0, 3.0])

    with pytest.raises(ValueError, match="same shape"):
        energy_vector(s, v, beta0=1.0, beta1=1.0)


def test_energy_vector_rejects_non_1d_inputs() -> None:
    s = np.zeros((2, 1))
    v = np.zeros((2,))

    with pytest.raises(ValueError, match="s must be a 1D vector"):
        energy_vector(s, v, beta0=1.0, beta1=1.0)
