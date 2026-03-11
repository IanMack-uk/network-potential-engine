import numpy as np

from network_potential_engine.graph.primitives import (
    edge_index_from_edges,
    support_mask,
    weight_matrix_to_vector,
    weight_vector_to_matrix,
)


def main() -> None:
    n_nodes = 3
    edges = {(0, 1), (1, 2)}

    idx = edge_index_from_edges(edges)
    w = np.array([2.0, 3.0], dtype=float)

    W = weight_vector_to_matrix(w, idx, n_nodes=n_nodes)

    print("P1 graph layer primitives smoke-check")
    print("Representation condition: W[i,j] = w_k for (i,j)=edge(k); W[i,j]=0 off-support")
    print()
    print("Edges E:")
    for e in sorted(edges):
        print(f"  {e}")
    print()
    print("Deterministic edge ordering / index map (k ↦ (i,j)):")
    for e, k in sorted(idx.items(), key=lambda kv: kv[1]):
        print(f"  k={k}: edge {e}, w_k={w[k]:.6g}")
    print()
    print("Edge-weight vector w:")
    print(w)
    print()
    print("Adjacency/weight matrix W induced by w on E:")
    print(W)
    print()

    mask = support_mask(edges, n_nodes=n_nodes)
    assert mask.shape == (n_nodes, n_nodes)

    print("Support mask 1_{(i,j) in E}:")
    print(mask.astype(int))
    print()

    # Off-support entries must be zero by construction.
    assert np.all(W[~mask] == 0.0)

    off_support_max_abs = float(np.max(np.abs(W[~mask]))) if np.any(~mask) else 0.0
    print(f"Off-support check: max_{'{'}(i,j) notin E{'}'} |W[i,j]| = {off_support_max_abs:.6g} (must be 0)")
    print()

    # Roundtrip consistency.
    w2 = weight_matrix_to_vector(W, idx)
    assert np.allclose(w, w2)

    print("Roundtrip check: w2 = vectorize(W) on declared support E")
    print("w2:")
    print(w2)
    print(f"max|w-w2| = {float(np.max(np.abs(w - w2))):.6g}")
    print()

    # Demonstrate off-support rejection.
    W_bad = W.copy()
    W_bad[2, 2] = 1.0
    try:
        weight_matrix_to_vector(W_bad, idx)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected off-support nonzero entry to raise ValueError")

    print("Off-support rejection check: modifying W[2,2]=1 triggers ValueError as expected")
    print()

    print("P1 graph layer primitives smoke-check: PASS")


if __name__ == "__main__":
    main()
