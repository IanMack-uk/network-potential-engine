from __future__ import annotations

from network_potential_engine.graph.primitives import edge_index_from_edges
from network_potential_engine.topology.endogenous_topology import (
    propose_edge_additions,
    update_edges,
)


def main() -> None:
    print("P16 endogenous topology smoke-check")
    print("Toy rule: propose lexicographically-smallest missing directed edges")
    print()

    n_nodes = 3
    E = {(0, 1)}
    print("Initial edge set E:")
    print(sorted(E))

    additions = propose_edge_additions(E, n_nodes=n_nodes, max_additions=2)
    print("Proposed additions:")
    print(sorted(additions))

    E2 = update_edges(E, additions=additions)
    print("Updated edge set E':")
    print(sorted(E2))

    # Representation discipline: edge ordering can be re-established after update.
    idx = edge_index_from_edges(E2)
    assert len(idx) == len(E2)

    print()
    print("P16 endogenous topology smoke-check: PASS")


if __name__ == "__main__":
    main()
