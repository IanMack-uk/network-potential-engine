from __future__ import annotations

import numpy as np


def _as_square_matrix(matrix: np.ndarray | list[list[float]], name: str) -> np.ndarray:
    """
    Convert input into a 2D square NumPy array of floats.
    """
    arr = np.asarray(matrix, dtype=float)

    if arr.ndim != 2:
        raise ValueError(f"{name} must be a 2D array.")
    if arr.shape[0] != arr.shape[1]:
        raise ValueError(f"{name} must be square.")

    return arr


def is_symmetric(
    matrix: np.ndarray | list[list[float]],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether a matrix is symmetric up to a numerical tolerance.

    Parameters
    ----------
    matrix
        Matrix to test.
    tol
        Absolute tolerance for symmetry.

    Returns
    -------
    bool
        True if matrix is symmetric within tolerance.
    """
    arr = _as_square_matrix(matrix, "matrix")
    return bool(np.allclose(arr, arr.T, atol=tol, rtol=0.0))


def diagonal_dominance_margins(
    matrix: np.ndarray | list[list[float]],
) -> np.ndarray:
    """
    Compute row-wise diagonal dominance margins.

    For each row i, returns
        |a_ii| - sum_{j != i} |a_ij|.

    Positive margins mean strict diagonal dominance on that row.

    Parameters
    ----------
    matrix
        Square matrix.

    Returns
    -------
    np.ndarray
        1D array of row-wise dominance margins.
    """
    arr = _as_square_matrix(matrix, "matrix")

    diagonal_abs = np.abs(np.diag(arr))
    off_diag_abs_sum = np.sum(np.abs(arr), axis=1) - diagonal_abs

    return diagonal_abs - off_diag_abs_sum


def is_strictly_diagonally_dominant(
    matrix: np.ndarray | list[list[float]],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether a matrix is strictly diagonally dominant by rows.

    Parameters
    ----------
    matrix
        Square matrix.
    tol
        Tolerance used to require a positive margin.

    Returns
    -------
    bool
        True if every row has dominance margin > tol.
    """
    margins = diagonal_dominance_margins(matrix)
    return bool(np.all(margins > tol))


def has_nonpositive_off_diagonals(
    matrix: np.ndarray | list[list[float]],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether all off-diagonal entries are nonpositive up to tolerance.

    Parameters
    ----------
    matrix
        Square matrix.
    tol
        Entries <= tol are treated as nonpositive.

    Returns
    -------
    bool
        True if all off-diagonal entries are <= tol.
    """
    arr = _as_square_matrix(matrix, "matrix")
    off_diag_mask = ~np.eye(arr.shape[0], dtype=bool)
    off_diag_entries = arr[off_diag_mask]

    return bool(np.all(off_diag_entries <= tol))


def has_nonnegative_off_diagonals(
    matrix: np.ndarray | list[list[float]],
    tol: float = 1e-10,
) -> bool:
    """
    Check whether all off-diagonal entries are nonnegative up to tolerance.

    Parameters
    ----------
    matrix
        Square matrix.
    tol
        Entries >= -tol are treated as nonnegative.

    Returns
    -------
    bool
        True if all off-diagonal entries are >= -tol.
    """
    arr = _as_square_matrix(matrix, "matrix")
    off_diag_mask = ~np.eye(arr.shape[0], dtype=bool)
    off_diag_entries = arr[off_diag_mask]

    return bool(np.all(off_diag_entries >= -tol))
