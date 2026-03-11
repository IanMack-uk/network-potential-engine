import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.source.node_source_value import psi_reference, source_vector


def test_psi_reference_is_r_plus_sum_extras() -> None:
    x = NodeAttributes(r=2.0, extras={"a": 1.0, "b": 3.5})
    assert psi_reference(x) == pytest.approx(6.5)


def test_source_vector_orders_by_node_index_and_is_shape_n() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"a": 1.0}),
            1: NodeAttributes(r=0.0, extras={}),
            2: NodeAttributes(r=0.5, extras={"b": 9.0}),
        },
        n_nodes=3,
    )

    s = source_vector(x)
    assert isinstance(s, np.ndarray)
    assert s.shape == (3,)
    assert np.allclose(s, np.array([3.0, 0.0, 9.5]))


def test_source_vector_rejects_missing_nodes() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={}),
            2: NodeAttributes(r=0.5, extras={}),
        },
        n_nodes=3,
    )

    with pytest.raises(ValueError, match="missing NodeAttributes for node 1"):
        source_vector(x)


def test_source_vector_accepts_custom_psi() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"a": 1.0}),
            1: NodeAttributes(r=3.0, extras={}),
        },
        n_nodes=2,
    )

    def psi_only_r(xi: NodeAttributes) -> float:
        return float(xi.r)

    s = source_vector(x, psi=psi_only_r)
    assert np.allclose(s, np.array([2.0, 3.0]))
