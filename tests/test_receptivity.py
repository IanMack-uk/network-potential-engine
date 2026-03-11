import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.diffusion.receptivity import receptivity_modulate


def test_receptivity_modulate_is_elementwise_product() -> None:
    rho = np.array([2.0, 0.5, -1.0])
    v = np.array([10.0, 20.0, 3.0])

    vt = receptivity_modulate(rho, v)
    assert np.allclose(vt, np.array([20.0, 10.0, -3.0]))


def test_receptivity_modulate_special_cases() -> None:
    v = np.array([1.0, 2.0])
    assert np.allclose(receptivity_modulate(np.ones_like(v), v), v)
    assert np.allclose(receptivity_modulate(np.zeros_like(v), v), np.zeros_like(v))


def test_receptivity_modulate_rejects_shape_mismatch() -> None:
    rho = np.array([1.0, 2.0])
    v = np.array([1.0, 2.0, 3.0])

    with pytest.raises(ValueError, match="same shape"):
        receptivity_modulate(rho, v)


def test_receptivity_modulate_rejects_non_1d() -> None:
    rho = np.zeros((2, 1))
    v = np.zeros((2,))

    with pytest.raises(ValueError, match="rho must be a 1D vector"):
        receptivity_modulate(rho, v)
