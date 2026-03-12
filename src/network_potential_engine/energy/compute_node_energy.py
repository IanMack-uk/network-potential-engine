from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.attributes.node_attributes import NodeAttributeField
from network_potential_engine.diffusion.node_propagation import (
    K_from_graph,
    propagated_value_from_others,
    propagated_value_outgoing_to_others,
    propagated_value_outgoing_total,
    propagated_value_total,
)
from network_potential_engine.energy.effective_energy import effective_energy_vector
from network_potential_engine.energy.node_energy import energy_vector
from network_potential_engine.graph.weight_transforms import adjacency_from_frequency, symmetrize_adjacency
from network_potential_engine.numeric.green_operator import GreenOperator
from network_potential_engine.source.value_model import ValueModel


@dataclass(frozen=True, slots=True)
class NodeEnergyComputation:
    s: np.ndarray
    A: np.ndarray
    A_sym: np.ndarray
    K: GreenOperator

    v_in_total: np.ndarray
    v_in_from_others: np.ndarray
    v_in_effective_from_others: np.ndarray

    v_out_total: np.ndarray
    v_out_to_others: np.ndarray

    E: np.ndarray
    E_effective: np.ndarray


def compute_node_energy(
    *,
    freq: np.ndarray,
    x: NodeAttributeField,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    tau: float,
    value_model: ValueModel | None = None,
) -> NodeEnergyComputation:
    freq_arr = np.asarray(freq, dtype=float)
    if freq_arr.ndim != 2 or freq_arr.shape[0] != freq_arr.shape[1]:
        raise ValueError("freq must be a square 2D array")

    n = int(freq_arr.shape[0])
    if x.n_nodes != n:
        raise ValueError("x.n_nodes must match freq dimension")

    rho_arr = np.asarray(rho, dtype=float)
    if rho_arr.ndim != 1:
        raise ValueError("rho must be a 1D vector")
    if rho_arr.shape[0] != n:
        raise ValueError("rho must have length equal to number of nodes")

    model = value_model if value_model is not None else ValueModel()

    s = model.source(x)

    A = adjacency_from_frequency(freq_arr)
    A_sym = symmetrize_adjacency(A)

    K = K_from_graph(A_sym, tau=tau)

    v_in_total = propagated_value_total(K, s)
    v_in_from_others = propagated_value_from_others(K, s)
    v_in_effective_from_others = rho_arr * v_in_from_others

    v_out_total = propagated_value_outgoing_total(K, s)
    v_out_to_others = propagated_value_outgoing_to_others(K, s)

    E = energy_vector(s, v_in_from_others, beta0=beta0, beta1=beta1)
    E_effective = effective_energy_vector(s, v_in_from_others, rho_arr, beta0=beta0, beta1=beta1)

    return NodeEnergyComputation(
        s=s,
        A=A,
        A_sym=A_sym,
        K=K,
        v_in_total=v_in_total,
        v_in_from_others=v_in_from_others,
        v_in_effective_from_others=v_in_effective_from_others,
        v_out_total=v_out_total,
        v_out_to_others=v_out_to_others,
        E=E,
        E_effective=E_effective,
    )
