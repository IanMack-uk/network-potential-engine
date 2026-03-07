from __future__ import annotations

import sympy as sp


def hessian_of_potential(phi: sp.Expr, w: sp.Matrix) -> sp.Matrix:
    """
    Compute the raw Hessian H(w, theta) = ∇²_{ww} Phi(w, theta).

    Parameters
    ----------
    phi
        Scalar SymPy expression representing the potential.
    w
        Column vector of weight variables.

    Returns
    -------
    sympy.Matrix
        Hessian matrix of phi with respect to w.
    """
    if not isinstance(phi, sp.Expr):
        raise TypeError("phi must be a SymPy expression.")
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if w.cols != 1:
        raise ValueError("w must be a column vector.")

    hess = sp.hessian(phi, list(w))
    return sp.simplify(hess)


def jacobian_of_gradient(grad: sp.Matrix, w: sp.Matrix) -> sp.Matrix:
    """
    Compute the Jacobian of the gradient vector with respect to w.

    If grad = ∇_w Phi, this should agree with the Hessian of Phi.

    Parameters
    ----------
    grad
        Column vector gradient.
    w
        Column vector of weight variables.

    Returns
    -------
    sympy.Matrix
        Jacobian of grad with respect to w.
    """
    if not isinstance(grad, sp.MatrixBase):
        raise TypeError("grad must be a SymPy Matrix.")
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if grad.cols != 1:
        raise ValueError("grad must be a column vector.")
    if w.cols != 1:
        raise ValueError("w must be a column vector.")

    jac = grad.jacobian(list(w))
    return sp.simplify(jac)
