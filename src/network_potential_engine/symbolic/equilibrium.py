from __future__ import annotations

import sympy as sp

from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian


def symbolic_equilibrium_from_coupling(
    coupling_operator: sp.Matrix,
    theta: sp.Matrix,
) -> sp.Matrix:
    """
    Compute the symbolic equilibrium map

        w*(theta) = C^{-1} theta

    for a given coupling operator C.

    Parameters
    ----------
    coupling_operator
        Symbolic square matrix C.
    theta
        Symbolic column vector of theta variables.

    Returns
    -------
    sympy.Matrix
        Symbolic column vector for the equilibrium map.
    """
    if not isinstance(coupling_operator, sp.MatrixBase):
        raise TypeError("coupling_operator must be a SymPy Matrix.")
    if not isinstance(theta, sp.MatrixBase):
        raise TypeError("theta must be a SymPy Matrix.")

    if coupling_operator.rows != coupling_operator.cols:
        raise ValueError("coupling_operator must be square.")
    if theta.cols != 1:
        raise ValueError("theta must be a column vector.")
    if coupling_operator.rows != theta.rows:
        raise ValueError(
            "coupling_operator and theta must have compatible shapes."
        )

    equilibrium = coupling_operator.inv() * theta
    return sp.simplify(equilibrium)


def symbolic_equilibrium_from_hessian(
    hessian: sp.Matrix,
    theta: sp.Matrix,
) -> sp.Matrix:
    """
    Compute the symbolic equilibrium map

        w*(theta) = C^{-1} theta, where C = -H

    from the raw Hessian H.

    Parameters
    ----------
    hessian
        Raw symbolic Hessian matrix H.
    theta
        Symbolic column vector of theta variables.

    Returns
    -------
    sympy.Matrix
        Symbolic column vector for the equilibrium map.
    """
    if not isinstance(hessian, sp.MatrixBase):
        raise TypeError("hessian must be a SymPy Matrix.")

    coupling_operator = coupling_operator_from_hessian(hessian)
    return symbolic_equilibrium_from_coupling(coupling_operator, theta)


def bootstrap_symbolic_equilibrium(
    phi: sp.Expr,
    w: sp.Matrix,
    theta: sp.Matrix,
) -> sp.Matrix:
    """
    Compute the symbolic equilibrium map for the bootstrap model.

    For the current bootstrap model, the equilibrium equation has the form

        F(w, theta) = theta - C w = 0,

    so the equilibrium is

        w*(theta) = C^{-1} theta,

    where C = -H and H = ∇²_{ww} Phi.

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

    hessian = hessian_of_potential(phi, w)
    return symbolic_equilibrium_from_hessian(hessian, theta)


def equilibrium_residual(
    phi: sp.Expr,
    w: sp.Matrix,
    theta: sp.Matrix,
    equilibrium: sp.Matrix,
) -> sp.Matrix:
    """
    Evaluate the symbolic equilibrium residual

        F(w*(theta), theta)

    by substituting the symbolic equilibrium into the gradient.

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
        Symbolic residual vector after substitution.
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
