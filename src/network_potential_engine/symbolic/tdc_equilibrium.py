from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.gradient import gradient_of_potential


def tdc_symbolic_equilibrium(
    phi: sp.Expr,
    w: sp.Matrix,
    theta: sp.Matrix,
) -> sp.Matrix:
    """
    Compute the symbolic equilibrium map for the TDC model:

        w*(theta) = C(theta)^(-1) theta,

    where C(theta) = -H(theta) and H(theta) is the raw Hessian.

    Parameters
    ----------
    phi
        Scalar symbolic potential expression.
    w
        Symbolic column vector of weight variables.
    theta
        Symbolic column vector of theta variables.

    Returns
    -------
    sympy.Matrix
        Symbolic column vector for the equilibrium map.
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
    if w.rows != theta.rows:
        raise ValueError("w and theta must have the same number of rows.")

    hessian = hessian_of_potential(phi, w)
    coupling = coupling_operator_from_hessian(hessian)

    equilibrium = coupling.inv() * theta
    return sp.simplify(equilibrium)


def tdc_equilibrium_residual(
    phi: sp.Expr,
    w: sp.Matrix,
    theta: sp.Matrix,
    equilibrium: sp.Matrix,
) -> sp.Matrix:
    """
    Evaluate the symbolic equilibrium residual

        F(w*(theta), theta)

    by substituting the candidate equilibrium into the gradient.

    Parameters
    ----------
    phi
        Scalar symbolic potential expression.
    w
        Symbolic column vector of weight variables.
    theta
        Symbolic column vector of theta variables.
    equilibrium
        Symbolic candidate equilibrium vector.

    Returns
    -------
    sympy.Matrix
        Symbolic residual vector.
    """
    if not isinstance(phi, sp.Expr):
        raise TypeError("phi must be a SymPy expression.")
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if not isinstance(theta, sp.MatrixBase):
        raise TypeError("theta must be a SymPy Matrix.")
    if not isinstance(equilibrium, sp.MatrixBase):
        raise TypeError("equilibrium must be a SymPy Matrix.")

    if w.cols != 1:
        raise ValueError("w must be a column vector.")
    if theta.cols != 1:
        raise ValueError("theta must be a column vector.")
    if equilibrium.cols != 1:
        raise ValueError("equilibrium must be a column vector.")
    if equilibrium.rows != w.rows:
        raise ValueError("equilibrium and w must have the same number of rows.")

    grad = gradient_of_potential(phi, w)
    substitutions = {w[i, 0]: equilibrium[i, 0] for i in range(w.rows)}
    residual = grad.subs(substitutions)

    return sp.simplify(residual)
