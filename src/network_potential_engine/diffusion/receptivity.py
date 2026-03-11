from __future__ import annotations

import numpy as np


def receptivity_modulate(rho: np.ndarray, v: np.ndarray) -> np.ndarray:
    if rho.ndim != 1:
        raise ValueError("rho must be a 1D vector")
    if v.ndim != 1:
        raise ValueError("v must be a 1D vector")
    if rho.shape != v.shape:
        raise ValueError("rho and v must have the same shape")

    return rho * v
