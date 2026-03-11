import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.energy.effective_energy import effective_energy_vector


def test_effective_energy_vector_composition() -> None:
    s = np.array([1.0, 2.0, 3.0])
    v = np.array([10.0, 20.0, 30.0])
    rho = np.array([2.0, 0.5, 0.0])

    beta0 = 2.0
    beta1 = 0.5

    E = effective_energy_vector(s, v, rho, beta0=beta0, beta1=beta1)
    assert np.allclose(E, beta0 * s + beta1 * (rho * v))


def test_effective_energy_vector_special_cases() -> None:
    s = np.array([1.0, 2.0])
    v = np.array([5.0, 7.0])
    rho = np.ones_like(v)

    assert np.allclose(effective_energy_vector(s, v, rho, beta0=1.0, beta1=0.0), s)
    assert np.allclose(effective_energy_vector(s, v, rho, beta0=0.0, beta1=1.0), v)


def test_effective_energy_vector_rejects_shape_mismatch() -> None:
    s = np.array([1.0, 2.0])
    v = np.array([1.0, 2.0])
    rho = np.array([1.0, 2.0, 3.0])

    with pytest.raises(ValueError, match="must have the same shape"):
        effective_energy_vector(s, v, rho, beta0=1.0, beta1=1.0)


def test_effective_energy_vector_rejects_non_1d_inputs() -> None:
    s = np.zeros((2, 1))
    v = np.zeros((2,))
    rho = np.zeros((2,))

    with pytest.raises(ValueError, match="s must be a 1D vector"):
        effective_energy_vector(s, v, rho, beta0=1.0, beta1=1.0)
