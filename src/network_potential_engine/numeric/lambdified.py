from __future__ import annotations

from collections.abc import Callable

import numpy as np
import sympy as sp


def _flatten_symbol_args(symbols: sp.Matrix) -> list[sp.Symbol]:
    """
    Convert a SymPy column vector of symbols into a flat Python list.

    Parameters
    ----------
    symbols
        SymPy column vector of symbols.

    Returns
    -------
    list[sympy.Symbol]
        Flat list of symbols in column order.
    """
    if not isinstance(symbols, sp.MatrixBase):
        raise TypeError("symbols must be a SymPy Matrix.")
    if symbols.cols != 1:
        raise ValueError("symbols must be a column vector.")

    return [symbols[i, 0] for i in range(symbols.rows)]


def _coerce_vector(values: np.ndarray | list[float] | tuple[float, ...], name: str) -> np.ndarray:
    """Convert input values into a 1D NumPy array of floats."""
    arr = np.asarray(values, dtype=float)

    if arr.ndim == 0:
        raise ValueError(f"{name} must be a 1D array-like object, not a scalar.")

    return arr.reshape(-1)


def lambdify_scalar(
    expr: sp.Expr,
    w: sp.Matrix,
    theta: sp.Matrix,
) -> Callable[[np.ndarray | list[float], np.ndarray | list[float]], float]:
    """
    Lambdify a scalar SymPy expression in (w, theta).

    The returned function expects:
    - w_values: array-like of shape (n_w,)
    - theta_values: array-like of shape (n_theta,)

    and returns a Python float.

    Parameters
    ----------
    expr
        Scalar SymPy expression.
    w
        SymPy column vector of weight symbols.
    theta
        SymPy column vector of parameter symbols.

    Returns
    -------
    Callable
        Numerical function f(w_values, theta_values) -> float.
    """
    if not isinstance(expr, sp.Expr):
        raise TypeError("expr must be a SymPy expression.")

    w_symbols = _flatten_symbol_args(w)
    theta_symbols = _flatten_symbol_args(theta)
    all_symbols = w_symbols + theta_symbols

    raw_func = sp.lambdify(all_symbols, expr, modules="numpy")

    def wrapped(
        w_values: np.ndarray | list[float],
        theta_values: np.ndarray | list[float],
    ) -> float:
        w_arr = _coerce_vector(w_values, "w_values")
        theta_arr = _coerce_vector(theta_values, "theta_values")

        if w_arr.shape[0] != len(w_symbols):
            raise ValueError(f"Expected {len(w_symbols)} w values, got {w_arr.shape[0]}.")
        if theta_arr.shape[0] != len(theta_symbols):
            raise ValueError(
                f"Expected {len(theta_symbols)} theta values, got {theta_arr.shape[0]}."
            )

        args = [*w_arr.tolist(), *theta_arr.tolist()]
        value = raw_func(*args)
        return float(value)

    return wrapped


def lambdify_matrix(
    expr: sp.Matrix,
    w: sp.Matrix,
    theta: sp.Matrix,
) -> Callable[[np.ndarray | list[float], np.ndarray | list[float]], np.ndarray]:
    """
    Lambdify a SymPy matrix expression in (w, theta).

    The returned function expects:
    - w_values: array-like of shape (n_w,)
    - theta_values: array-like of shape (n_theta,)

    and returns:
    - a 1D NumPy array if expr is a column vector
    - otherwise a 2D NumPy array

    Parameters
    ----------
    expr
        SymPy matrix expression.
    w
        SymPy column vector of weight symbols.
    theta
        SymPy column vector of parameter symbols.

    Returns
    -------
    Callable
        Numerical function f(w_values, theta_values) -> np.ndarray.
    """
    if not isinstance(expr, sp.MatrixBase):
        raise TypeError("expr must be a SymPy Matrix.")

    w_symbols = _flatten_symbol_args(w)
    theta_symbols = _flatten_symbol_args(theta)
    all_symbols = w_symbols + theta_symbols

    raw_func = sp.lambdify(all_symbols, expr, modules="numpy")

    n_rows, n_cols = expr.shape

    def wrapped(
        w_values: np.ndarray | list[float],
        theta_values: np.ndarray | list[float],
    ) -> np.ndarray:
        w_arr = _coerce_vector(w_values, "w_values")
        theta_arr = _coerce_vector(theta_values, "theta_values")

        if w_arr.shape[0] != len(w_symbols):
            raise ValueError(f"Expected {len(w_symbols)} w values, got {w_arr.shape[0]}.")
        if theta_arr.shape[0] != len(theta_symbols):
            raise ValueError(
                f"Expected {len(theta_symbols)} theta values, got {theta_arr.shape[0]}."
            )

        args = [*w_arr.tolist(), *theta_arr.tolist()]
        value = raw_func(*args)
        arr = np.asarray(value, dtype=float)

        # Normalize shapes so SymPy column vectors become predictable 1D arrays.
        if n_cols == 1:
            return arr.reshape(n_rows)

        return arr.reshape(n_rows, n_cols)

    return wrapped
