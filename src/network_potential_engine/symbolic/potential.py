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


def theta_dependent_curvature_potential(
    w: sp.Matrix,
    theta: sp.Matrix,
    base_quadratic_weight: sp.Expr | float = 1,
    theta_curvature_weight: sp.Expr | float = sp.Rational(1, 5),
    coupling_weight: sp.Expr | float = sp.Rational(1, 2),
) -> sp.Expr:
    """
    Build a potential with theta-dependent curvature.

    Current assumption:
        len(w) == len(theta)

    Phi_tdc(w, theta)
      = sum_i theta_i * w_i
        - (1/2) * sum_i (base_quadratic_weight + theta_curvature_weight * theta_i) * w_i^2
        - (coupling_weight / 2) * sum_{i=0}^{n-2} (w_i - w_{i+1})^2

    This model is designed to remain analytically manageable while making
    the Hessian depend on theta.

    Parameters
    ----------
    w
        Column vector of weight variables.
    theta
        Column vector of theta variables.
    base_quadratic_weight
        Baseline diagonal curvature coefficient q.
    theta_curvature_weight
        Coefficient alpha controlling theta-dependent curvature.
    coupling_weight
        Nearest-neighbour coupling coefficient c.

    Returns
    -------
    sympy.Expr
        Scalar symbolic expression for Phi_tdc(w, theta).
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
            "theta_dependent_curvature_potential currently requires len(w) == len(theta)."
        )

    q = sp.sympify(base_quadratic_weight)
    alpha = sp.sympify(theta_curvature_weight)
    c = sp.sympify(coupling_weight)
    n = w.rows

    linear_term = sum(theta[i, 0] * w[i, 0] for i in range(n))

    theta_weighted_quadratic_term = sp.Rational(1, 2) * sum(
        (q + alpha * theta[i, 0]) * w[i, 0] ** 2
        for i in range(n)
    )

    coupling_term = sp.Rational(1, 2) * c * sum(
        (w[i, 0] - w[i + 1, 0]) ** 2 for i in range(n - 1)
    )

    phi = linear_term - theta_weighted_quadratic_term - coupling_term
    return sp.simplify(phi)
