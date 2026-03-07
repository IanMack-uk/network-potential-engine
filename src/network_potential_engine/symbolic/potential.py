from __future__ import annotations

import sympy as sp


def bootstrap_potential(
    w: sp.Matrix,
    theta: sp.Matrix,
    quadratic_weight: sp.Expr | float = 1,
    coupling_weight: sp.Expr | float = sp.Rational(1, 2),
) -> sp.Expr:
    """
    Build a simple bootstrap potential Phi(w, theta).

    Current bootstrap assumption:
        len(w) == len(theta)

    Phi(w, theta)
      = sum_i theta_i * w_i
        - (quadratic_weight / 2) * sum_i w_i^2
        - (coupling_weight / 2) * sum_{i=0}^{n-2} (w_i - w_{i+1})^2

    Parameters
    ----------
    w
        Column vector of weight variables.
    theta
        Column vector of theta variables.
    quadratic_weight
        Coefficient on the diagonal quadratic term.
    coupling_weight
        Coefficient on the nearest-neighbour coupling term.

    Returns
    -------
    sympy.Expr
        Scalar symbolic expression for Phi(w, theta).
    """
    if not isinstance(w, sp.MatrixBase):
        raise TypeError("w must be a SymPy Matrix.")
    if not isinstance(theta, sp.MatrixBase):
        raise TypeError("theta must be a SymPy Matrix.")

    if w.cols != 1:
        raise ValueError("w must be a column vector.")
    if theta.cols != 1:
        raise ValueError("theta must be a column vector.")
    if w.rows != theta.rows:
        raise ValueError(
            "bootstrap_potential currently requires len(w) == len(theta)."
        )

    q = sp.sympify(quadratic_weight)
    c = sp.sympify(coupling_weight)
    n = w.rows

    linear_term = sum(theta[i, 0] * w[i, 0] for i in range(n))
    quadratic_term = sp.Rational(1, 2) * q * sum(w[i, 0] ** 2 for i in range(n))
    coupling_term = sp.Rational(1, 2) * c * sum(
        (w[i, 0] - w[i + 1, 0]) ** 2 for i in range(n - 1)
    )

    phi = linear_term - quadratic_term - coupling_term
    return sp.simplify(phi)
