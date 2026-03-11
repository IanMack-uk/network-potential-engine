import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.attributes.node_attributes import (
    NodeAttributeField,
    NodeAttributes,
    capacity_vector,
)


def test_node_attributes_accepts_r_and_extras() -> None:
    x0 = NodeAttributes(r=2.0, extras={"creativity": 1.5})
    assert float(x0.r) == 2.0
    assert x0.extras["creativity"] == 1.5


def test_node_attributes_rejects_non_numeric_r() -> None:
    with pytest.raises(TypeError, match="r must be a real scalar"):
        NodeAttributes(r="bad")  # type: ignore[arg-type]


def test_node_attributes_rejects_non_string_extra_keys() -> None:
    with pytest.raises(TypeError, match="extras keys must be strings"):
        NodeAttributes(r=1.0, extras={1: 2.0})  # type: ignore[dict-item]


def test_node_attributes_rejects_non_numeric_extra_values() -> None:
    with pytest.raises(TypeError, match="extras values must be real scalars"):
        NodeAttributes(r=1.0, extras={"x": "bad"})  # type: ignore[dict-item]


def test_capacity_vector_returns_r_for_all_nodes_in_order() -> None:
    field = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"a": 1.0}),
            1: NodeAttributes(r=3.0, extras={}),
            2: NodeAttributes(r=0.5, extras={"b": 9.0}),
        },
        n_nodes=3,
    )

    r = capacity_vector(field)
    assert isinstance(r, np.ndarray)
    assert r.shape == (3,)
    assert np.allclose(r, np.array([2.0, 3.0, 0.5]))


def test_capacity_vector_rejects_missing_nodes() -> None:
    field = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={}),
            2: NodeAttributes(r=0.5, extras={}),
        },
        n_nodes=3,
    )

    with pytest.raises(ValueError, match="missing NodeAttributes for node 1"):
        capacity_vector(field)


def test_node_attribute_field_rejects_out_of_range_index() -> None:
    with pytest.raises(ValueError, match="node index out of range"):
        NodeAttributeField(by_node={3: NodeAttributes(r=1.0)}, n_nodes=3)
