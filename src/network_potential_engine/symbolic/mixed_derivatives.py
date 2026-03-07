from __future__ import annotations

import sympy as sp


def mixed_derivative_block(grad: sp.Matrix, theta: sp.Matrix) -> sp.Matrix:
    """
    Compute the mixed derivative block H_{w,theta} = D_theta(∇_w Phi).

    If grad = ∇_w Phi(w, theta), this returns the matrix whose (i, j)-entry is
        ∂² Phi / (∂w_i ∂theta_j).

    Parameters
    ----------
    grad
        Column vector gradient ∇_w Phi.
    theta
        Column vector of theta variables.

    Returns
    -------
    sympy.Matrix
        Matrix of shape (len(w), len(theta)).
    """
    if not isinstance(grad, sp.MatrixBase):
        raise TypeError("grad must be a SymPy Matrix.")
    if not isinstance(theta, sp.MatrixBase):
        raise TypeError("theta must be a SymPy Matrix.")
    if grad.cols != 1:
        raise ValueError("grad must be a column vector.")
    if theta.cols != 1:
        raise ValueError("theta must be a column vector.")

    mixed = grad.jacobian(list(theta))
    return sp.simplify(mixed)


def mixed_derivative_from_potential(
    phi: sp.Expr, w: sp.Matrix, theta: sp.Matrix
) -> sp.Matrix:
    """
    Convenience wrapper to compute H_{w,theta} directly from Phi.

    Parameters
    ----------
    phi
        Scalar SymPy expression.
    w
        Column vector of weight variables.
    theta
        Column vector of theta variables.

    Returns
    -------
    sympy.Matrix
        Mixed derivative block D_theta(∇_w Phi).
    """
    if not isinstance(phi, sp.Expr):
        raise TypeError("phi must be a SymPy expression.")
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if not isinstance(theta, sp.MatrixBase):
        raise TypeError("theta must be a SymPy Matrix.")
    if w.cols != 1:
        raise ValueError("w must be a column vector.")
    if theta.cols != 1:
        raise ValueError("theta must be a column vector.")

    grad = sp.Matrix([sp.diff(phi, w[i, 0]) for i in range(w.rows)])
    mixed = grad.jacobian(list(theta))
    return sp.simplify(mixed)
