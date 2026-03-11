from __future__ import annotations

from typing import Iterable


def _all_possible_directed_edges(n_nodes: int) -> list[tuple[int, int]]:
    if n_nodes <= 0:
        raise ValueError("n_nodes must be positive")
    return [(i, j) for i in range(n_nodes) for j in range(n_nodes) if i != j]


def propose_edge_additions(
    edges: set[tuple[int, int]],
    n_nodes: int,
    *,
    max_additions: int = 1,
) -> set[tuple[int, int]]:
    """Propose a deterministic set of edge additions.

    This is a toy endogenous-topology helper: it proposes adding up to `max_additions`
    missing directed edges, choosing the lexicographically-smallest candidates.

    The function does not use the potential/equilibrium; it only provides a stable,
    auditable update rule for Step 16 evidence.
    """

    if max_additions < 0:
        raise ValueError("max_additions must be nonnegative")

    candidates = [e for e in _all_possible_directed_edges(n_nodes) if e not in edges]
    candidates.sort()

    return set(candidates[:max_additions])


def update_edges(
    edges: set[tuple[int, int]],
    *,
    additions: Iterable[tuple[int, int]] = (),
    removals: Iterable[tuple[int, int]] = (),
) -> set[tuple[int, int]]:
    """Apply edge additions/removals to an edge set."""

    new_edges = set(edges)
    for e in removals:
        new_edges.discard(e)
    for e in additions:
        new_edges.add(e)
    return new_edges
