from __future__ import annotations

import numpy as np


def effective_energy_vector(
    s: np.ndarray,
    v: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
) -> np.ndarray:
    if s.ndim != 1:
        raise ValueError("s must be a 1D vector")
    if v.ndim != 1:
        raise ValueError("v must be a 1D vector")
    if rho.ndim != 1:
        raise ValueError("rho must be a 1D vector")
    if s.shape != v.shape or s.shape != rho.shape:
        raise ValueError("s, v, and rho must have the same shape")

    v_tilde = rho * v
    return float(beta0) * s + float(beta1) * v_tilde
