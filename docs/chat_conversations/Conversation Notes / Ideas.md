# Conversation Notes / Ideas

## Index

- **Source model decision (s = q·k)**
  - Decision: use `s_i = quality_i * quantity_i` for v1 source value.
  - Repo hook: `src/network_potential_engine/source/value_model.py` (`ValueModel`) and `src/network_potential_engine/source/node_source_value.py` (`source_vector`).

- **Tie strength mapping (log1p(freq))**
  - Decision: map observed interaction frequencies to continuous tie weights via `A_ij = log1p(freq_ij)`.
  - Repo hook: `src/network_potential_engine/graph/weight_transforms.py` (`adjacency_from_frequency`, `symmetrize_adjacency`).

- **Introductions / accessibility (brokered reach)**
  - See: section “Introductions / recommendations as relationship-value mechanism” below.
  - Note: this is currently a conceptual mechanism, not yet implemented as a first-class module.

- **Pipeline wrapper (compute_node_energy)**
  - Repo hook: `src/network_potential_engine/energy/compute_node_energy.py` (`compute_node_energy`).

## Introductions / recommendations as relationship-value mechanism

- Introductions / recommendations should be treated as a first-class mechanism in the relational layer, not only as an increase in observed interaction frequency.
- A clean model treats an intro event as an update to accessibility (reachability) between two people, often via a broker/mutual connection.
- Minimal definitions:
  - Directed tie weights (relationship graph): W = [w_ij]
  - Accessibility: access_ij (direct or brokered reach)
  - Relational ability (sender): a_i
  - Relational receptiveness (target): rho_rel_j
  - Standing/fame (both parties): F_i, F_j
- Minimal brokered accessibility (2-hop introducer path):
  - access^(2)_ij = max_m A_im * A_mj
- Minimal tie-strength update incorporating accessibility, ability, receptiveness, and standing:
  - w_ij = access_ij * a_i * rho_rel_j * h(F_i, F_j) * log(1 + freq_ij)
- Intro event effect (conceptual): increase access_ij (and optionally seed a weak tie) even before substantial freq_ij exists.
- Brokerage credit: successful intros can contribute to a connector score for the introducer.

Implementation note:
- This intro/recommendation mechanism is not yet implemented as a first-class object in the codebase; currently it would only show up indirectly if it increases observed freq_ij. A dedicated module would fit naturally in the dynamic network evolution / endogenous topology layer (P15/P16).
