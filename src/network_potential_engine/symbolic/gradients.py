from __future__ import annotations

import sympy as sp


def gradient_of_potential(phi: sp.Expr, w: sp.Matrix) -> sp.Matrix:
    """
    Compute the gradient F(w, theta) = ∇_w Phi(w, theta).

    Parameters
    ----------
    phi
        Scalar SymPy expression representing the potential.
    w
        Column vector of weight variables.

    Returns
    -------
    sympy.Matrix
        Column vector of partial derivatives of phi with respect to w.
    """
    if not isinstance(phi, sp.Expr):
        raise TypeError("phi must be a SymPy expression.")
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if w.cols != 1:
        raise ValueError("w must be a column vector.")

    grad = sp.Matrix([sp.diff(phi, w[i, 0]) for i in range(w.rows)])
    return sp.simplify(grad)
