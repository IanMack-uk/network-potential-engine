import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.diffusion.node_propagation import K_from_graph, propagated_value_from_others
from network_potential_engine.graph.weight_transforms import adjacency_from_frequency, symmetrize_adjacency
from network_potential_engine.source.value_model import ValueModel


def test_affinity_pipeline_smoke_s_to_v_from_others() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=1.0, extras={}),
            1: NodeAttributes(r=2.0, extras={}),
            2: NodeAttributes(r=3.0, extras={}),
        },
        n_nodes=3,
    )
    s = ValueModel().source(x)

    freq = np.array(
        [
            [0.0, 3.0, 0.0],
            [0.0, 0.0, 5.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=float,
    )
    A = adjacency_from_frequency(freq)
    A_sym = symmetrize_adjacency(A)

    K = K_from_graph(A_sym, tau=1.0)
    v_others = propagated_value_from_others(K, s)

    assert v_others.shape == (3,)
    assert np.all(np.isfinite(v_others))
