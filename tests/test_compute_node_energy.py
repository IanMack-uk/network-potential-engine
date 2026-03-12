import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField, NodeAttributes
from network_potential_engine.diffusion.node_propagation import (
    K_from_graph,
    propagated_value_from_others,
    propagated_value_outgoing_to_others,
)
from network_potential_engine.energy.compute_node_energy import compute_node_energy
from network_potential_engine.graph.weight_transforms import adjacency_from_frequency, symmetrize_adjacency
from network_potential_engine.source.value_model import ValueModel


def test_compute_node_energy_matches_component_functions() -> None:
    x = NodeAttributeField(
        by_node={
            0: NodeAttributes(r=1.0, extras={}),
            1: NodeAttributes(r=2.0, extras={}),
            2: NodeAttributes(r=3.0, extras={}),
        },
        n_nodes=3,
    )

    freq = np.array(
        [
            [0.0, 3.0, 0.0],
            [0.0, 0.0, 5.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=float,
    )

    rho = np.array([1.0, 0.5, 2.0], dtype=float)
    beta0 = 1.25
    beta1 = 0.75
    tau = 1.0

    out = compute_node_energy(
        freq=freq,
        x=x,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        tau=tau,
        value_model=ValueModel(),
    )

    s = ValueModel().source(x)
    A = adjacency_from_frequency(freq)
    A_sym = symmetrize_adjacency(A)
    K = K_from_graph(A_sym, tau=tau)

    v_in_from_others = propagated_value_from_others(K, s)
    v_out_to_others = propagated_value_outgoing_to_others(K, s)

    assert np.allclose(out.s, s)
    assert np.allclose(out.A, A)
    assert np.allclose(out.A_sym, A_sym)

    assert np.allclose(out.v_in_from_others, v_in_from_others)
    assert np.allclose(out.v_out_to_others, v_out_to_others)

    assert np.allclose(out.v_in_effective_from_others, rho * v_in_from_others)
