from __future__ import annotations

import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.source.node_source_value import psi_reference, source_vector


def main() -> None:
    print("P3 node source value smoke-check")
    print("Definition: s_i := ψ(x_i), s := (s_i)_{i in V}")
    print("Interface-first: ψ is model-specific; ψ_ref is a simple reference implementation")
    print()

    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"creativity": 1.5}),
            1: NodeAttributes(r=3.0, extras={}),
            2: NodeAttributes(r=0.5, extras={"influence": 4.0}),
        },
        n_nodes=3,
    )

    s = source_vector(x, psi=psi_reference)

    print("Computed source vector s:")
    print(s)

    assert isinstance(s, np.ndarray)
    assert s.shape == (3,)
    assert np.allclose(s, np.array([3.5, 3.0, 4.5]))

    print()
    print("P3 node source value smoke-check: PASS")


if __name__ == "__main__":
    main()
