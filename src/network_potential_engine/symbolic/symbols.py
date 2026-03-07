from __future__ import annotations

import sympy as sp


def make_symbols(n_w: int, n_theta: int) -> tuple[sp.Matrix, sp.Matrix]:
    """
    Create symbolic column vectors for weights w and parameters theta.

    Parameters
    ----------
    n_w
        Number of weight variables.
    n_theta
        Number of theta variables.

    Returns
    -------
    tuple[sympy.Matrix, sympy.Matrix]
        A pair (w, theta), each a SymPy column vector.
    """
    if n_w <= 0:
        raise ValueError("n_w must be positive.")
    if n_theta <= 0:
        raise ValueError("n_theta must be positive.")

    w = sp.Matrix(sp.symbols(f"w0:{n_w}", real=True))
    theta = sp.Matrix(sp.symbols(f"theta0:{n_theta}", real=True))

    return w, theta
