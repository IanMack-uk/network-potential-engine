from __future__ import annotations

from collections.abc import Callable

import numpy as np


def euler_step(
    w: np.ndarray,
    theta: np.ndarray,
    grad_phi: Callable[[np.ndarray, np.ndarray], np.ndarray],
    eta: float,
) -> np.ndarray:
    if w.ndim != 1:
        raise ValueError("w must be a 1D vector")
    if theta.ndim != 1:
        raise ValueError("theta must be a 1D vector")
    if w.shape != theta.shape:
        raise ValueError("w and theta must have the same shape")

    g = grad_phi(w, theta)
    if not isinstance(g, np.ndarray):
        raise TypeError("grad_phi must return a numpy array")
    if g.shape != w.shape:
        raise ValueError("grad_phi must return an array of the same shape as w")

    return w + float(eta) * g
