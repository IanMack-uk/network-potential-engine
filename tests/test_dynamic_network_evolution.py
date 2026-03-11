import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.dynamics.gradient_flow import euler_step


def phi_quadratic(w: np.ndarray, theta: np.ndarray) -> float:
    # Concave quadratic with maximiser at w = theta.
    # Φ(w,θ) = -1/2 ||w-θ||^2
    d = w - theta
    return float(-0.5 * np.dot(d, d))


def grad_phi_quadratic(w: np.ndarray, theta: np.ndarray) -> np.ndarray:
    # ∇_w Φ = -(w-θ) = θ-w
    return theta - w


def test_euler_step_fixed_point_is_stationary() -> None:
    theta = np.array([2.0, -1.0, 3.0])
    w_star = theta.copy()
    eta = 0.7

    w_next = euler_step(w_star, theta, grad_phi_quadratic, eta)
    assert np.allclose(w_next, w_star)


def test_euler_step_increases_phi_for_small_step() -> None:
    theta = np.array([2.0, -1.0, 3.0])
    w = np.array([0.0, 0.0, 0.0])

    eta = 0.5

    phi0 = phi_quadratic(w, theta)
    w1 = euler_step(w, theta, grad_phi_quadratic, eta)
    phi1 = phi_quadratic(w1, theta)

    assert phi1 >= phi0


def test_euler_step_rejects_shape_mismatch() -> None:
    w = np.array([1.0, 2.0])
    theta = np.array([1.0, 2.0, 3.0])

    with pytest.raises(ValueError, match="same shape"):
        euler_step(w, theta, grad_phi_quadratic, eta=0.1)


def test_euler_step_rejects_non_1d() -> None:
    w = np.zeros((2, 1))
    theta = np.zeros((2,))

    with pytest.raises(ValueError, match="w must be a 1D vector"):
        euler_step(w, theta, grad_phi_quadratic, eta=0.1)
