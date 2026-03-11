import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.topology.endogenous_topology import (
    propose_edge_additions,
    update_edges,
)


def test_propose_edge_additions_is_deterministic_and_respects_max_additions() -> None:
    edges = {(0, 1)}
    additions = propose_edge_additions(edges, n_nodes=3, max_additions=2)

    # All directed edges without self-loops for n=3 are:
    # (0,1),(0,2),(1,0),(1,2),(2,0),(2,1)
    # Missing after {(0,1)} are:
    # (0,2),(1,0),(1,2),(2,0),(2,1)
    # Lexicographically smallest 2 are (0,2) and (1,0).
    assert additions == {(0, 2), (1, 0)}


def test_propose_edge_additions_allows_zero_additions() -> None:
    edges = {(0, 1)}
    additions = propose_edge_additions(edges, n_nodes=3, max_additions=0)
    assert additions == set()


def test_propose_edge_additions_rejects_negative_max_additions() -> None:
    with pytest.raises(ValueError, match="max_additions must be nonnegative"):
        propose_edge_additions(set(), n_nodes=3, max_additions=-1)


def test_update_edges_applies_additions_and_removals() -> None:
    edges = {(0, 1), (1, 2)}
    new_edges = update_edges(edges, additions={(2, 0)}, removals={(0, 1)})

    assert (0, 1) not in new_edges
    assert (1, 2) in new_edges
    assert (2, 0) in new_edges
