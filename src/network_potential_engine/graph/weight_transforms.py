from __future__ import annotations

import numpy as np


def adjacency_from_frequency(freq: np.ndarray) -> np.ndarray:
    freq_arr = np.asarray(freq, dtype=float)
    if freq_arr.ndim != 2 or freq_arr.shape[0] != freq_arr.shape[1]:
        raise ValueError("freq must be a square 2D array")
    if np.any(freq_arr < 0.0):
        raise ValueError("freq must be entrywise nonnegative")
    return np.log1p(freq_arr)


def symmetrize_adjacency(A: np.ndarray) -> np.ndarray:
    A_arr = np.asarray(A, dtype=float)
    if A_arr.ndim != 2 or A_arr.shape[0] != A_arr.shape[1]:
        raise ValueError("A must be a square 2D array")
    return 0.5 * (A_arr + A_arr.T)
