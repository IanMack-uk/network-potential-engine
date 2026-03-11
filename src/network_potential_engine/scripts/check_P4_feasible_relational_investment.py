import numpy as np

from network_potential_engine.constraints.feasible_relational_investment import (
    check_capacity_from_edge_vector,
    check_row_sum_capacity,
)
from network_potential_engine.graph.primitives import edge_index_from_edges, weight_vector_to_matrix


def main() -> None:
    n_nodes = 3
    edges = {(0, 1), (0, 2), (1, 2)}
    edge_index = edge_index_from_edges(edges)

    # Edge weights aligned with edge_index_from_edges deterministic ordering.
    w = np.array([1.0, 0.5, 2.0], dtype=float)
    W = weight_vector_to_matrix(w, edge_index, n_nodes=n_nodes)

    r = np.array([2.0, 2.0, 0.0], dtype=float)

    print("P4 feasible relational investment smoke-check")
    print("Feasibility condition: for each node i,  Σ_j w_ij ≤ r_i")
    print()
    print("Edge ordering / vector representation (k ↦ (i,j), w_k = w(i,j)):")
    for e, k in sorted(edge_index.items(), key=lambda kv: kv[1]):
        print(f"  k={k}: edge {e}, w_k={w[k]:.6g}")
    print()
    print("Matrix representation W (off-support entries are 0 by construction):")
    print(W)
    print()
    row_sums = np.sum(W, axis=1)
    margins = r - row_sums
    print("Node-wise row sums and margins (matrix view):")
    for i in range(n_nodes):
        print(f"  i={i}: Σ_j W[i,j]={row_sums[i]:.6g}  ≤  r_i={r[i]:.6g}    margin=r_i-Σ_j={margins[i]:.6g}")
    print()

    out_edges_by_node: list[list[tuple[int, int, int]]] = [[] for _ in range(n_nodes)]
    for (i, j), k in edge_index.items():
        out_edges_by_node[i].append((j, i, k))
    for i in range(n_nodes):
        out_edges_by_node[i].sort(key=lambda t: t[0])

    print("Node-wise aggregation (edge-vector view):")
    for i in range(n_nodes):
        terms = [f"w_{i}{j}=w[k={k}]={w[k]:.6g}" for (j, _ii, k) in out_edges_by_node[i]]
        expr = " + ".join(terms) if terms else "0"
        print(f"  i={i}: ({expr}) = {row_sums[i]:.6g}  ≤  r_i={r[i]:.6g}")
    print()

    mat = check_row_sum_capacity(W, r)
    vec = check_capacity_from_edge_vector(w, edge_index, r, n_nodes)

    assert mat.holds == vec.holds
    assert np.allclose(mat.margins, vec.margins)

    # Demonstrate failure.
    r_bad = np.array([1.0, 2.0, 0.0], dtype=float)
    mat_bad = check_row_sum_capacity(W, r_bad)
    assert mat_bad.holds is False

    print("P4 feasible relational investment smoke-check: PASS")


if __name__ == "__main__":
    main()
