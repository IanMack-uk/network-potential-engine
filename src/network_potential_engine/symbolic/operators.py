from __future__ import annotations

import sympy as sp


def coupling_operator_from_hessian(hessian: sp.Matrix) -> sp.Matrix:
    """
    Define the canonical coupling/stability operator C = -H.

    Parameters
    ----------
    hessian
        Raw Hessian matrix H = ∇²_{ww} Phi.

    Returns
    -------
    sympy.Matrix
        Coupling operator C = -H.
    """
    if not isinstance(hessian, sp.MatrixBase):
        raise TypeError("hessian must be a SymPy Matrix.")

    return sp.simplify(-hessian)


def response_operator(coupling_operator: sp.Matrix, mixed_block: sp.Matrix) -> sp.Matrix:
    """
    Build the symbolic response operator

        R = C^{-1} H_{w,theta}.

    This is suitable for small symbolic examples.
    In numeric code, prefer solving C X = H_{w,theta} rather than
    forming an explicit inverse.

    Parameters
    ----------
    coupling_operator
        Matrix C = -H.
    mixed_block
        Matrix H_{w,theta}.

    Returns
    -------
    sympy.Matrix
        Symbolic response matrix.
    """
    if not isinstance(coupling_operator, sp.MatrixBase):
        raise TypeError("coupling_operator must be a SymPy Matrix.")
    if not isinstance(mixed_block, sp.MatrixBase):
        raise TypeError("mixed_block must be a SymPy Matrix.")

    if coupling_operator.rows != coupling_operator.cols:
        raise ValueError("coupling_operator must be square.")
    if coupling_operator.rows != mixed_block.rows:
        raise ValueError(
            "coupling_operator and mixed_block must have compatible shapes."
        )

    response = coupling_operator.inv() * mixed_block
    return sp.simplify(response)
