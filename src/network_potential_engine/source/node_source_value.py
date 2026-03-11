from __future__ import annotations

from collections.abc import Callable

import numpy as np

from network_potential_engine.attributes.node_attributes import (
    NodeAttributeField,
    NodeAttributes,
)


def psi_reference(x_i: NodeAttributes) -> float:
    """Reference production mapping ψ_ref.

    This function is intentionally simple and is provided only as an example.

    Definition (hybrid attribute record x_i = (r_i, extras_i)):

      ψ_ref(x_i) := r_i + sum_k extras_i[k]

    Missing extras contribute 0.
    """

    base = float(x_i.r)
    extras_sum = 0.0
    for v in x_i.extras.values():
        extras_sum += float(v)
    return base + extras_sum


def source_vector(
    x: NodeAttributeField,
    *,
    psi: Callable[[NodeAttributes], float] = psi_reference,
) -> np.ndarray:
    """Compute node-indexed source vector s from an attribute field.

    Returns:
      s: np.ndarray of shape (n_nodes,)

    Raises:
      ValueError: if x is missing attributes for any node index.
    """

    s = np.zeros(x.n_nodes, dtype=float)
    for i in range(x.n_nodes):
        try:
            xi = x.by_node[i]
        except KeyError as e:
            raise ValueError(f"missing NodeAttributes for node {i}") from e
        s[i] = float(psi(xi))
    return s
