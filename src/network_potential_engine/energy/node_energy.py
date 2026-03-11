from __future__ import annotations

import numpy as np


def energy_vector(
    s: np.ndarray,
    v: np.ndarray,
    beta0: float,
    beta1: float,
) -> np.ndarray:
    if s.ndim != 1:
        raise ValueError("s must be a 1D vector")
    if v.ndim != 1:
        raise ValueError("v must be a 1D vector")
    if s.shape != v.shape:
        raise ValueError("s and v must have the same shape")

    return float(beta0) * s + float(beta1) * v
