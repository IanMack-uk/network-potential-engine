import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.source.node_source_value import source_vector
from network_potential_engine.source.value_model import ValueModel


def test_value_model_source_matches_source_vector_default_psi() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"a": 1.0}),
            1: NodeAttributes(r=0.0, extras={}),
            2: NodeAttributes(r=0.5, extras={"b": 9.0}),
        },
        n_nodes=3,
    )

    model = ValueModel()
    assert np.allclose(model.source(x), source_vector(x))


def test_value_model_accepts_custom_psi() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=2.0, extras={"a": 1.0}),
            1: NodeAttributes(r=3.0, extras={}),
        },
        n_nodes=2,
    )

    def psi_only_r(xi: NodeAttributes) -> float:
        return float(xi.r)

    model = ValueModel(psi=psi_only_r)
    assert np.allclose(model.source(x), np.array([2.0, 3.0]))
