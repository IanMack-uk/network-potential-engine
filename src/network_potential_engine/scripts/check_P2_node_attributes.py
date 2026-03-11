from __future__ import annotations

import numpy as np

from network_potential_engine.attributes.node_attributes import (
    NodeAttributeField,
    NodeAttributes,
    capacity_vector,
)


def main() -> None:
    print("P2 node attributes smoke-check")
    print("Hybrid representation: x_i = (r_i, extras_i)")
    print("Export: capacity vector r = (r_i) for use in feasibility layer (P4)")
    print()

    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"creativity": 1.5}),
            1: NodeAttributes(r=3.0, extras={}),
            2: NodeAttributes(r=0.5, extras={"influence": 4.0}),
        },
        n_nodes=3,
    )

    r = capacity_vector(x)

    print("Node attributes:")
    for i in range(x.n_nodes):
        xi = x.by_node[i]
        print(f"  i={i}: r_i={float(xi.r):.6g}, extras={dict(xi.extras)}")
    print()

    print("Extracted capacity vector r:")
    print(r)
    assert isinstance(r, np.ndarray)
    assert r.shape == (3,)
    assert np.allclose(r, np.array([2.0, 3.0, 0.5]))

    print()
    print("P2 node attributes smoke-check: PASS")


if __name__ == "__main__":
    main()
