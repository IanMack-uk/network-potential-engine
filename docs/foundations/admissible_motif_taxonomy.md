# Admissible Motif Taxonomy (Framework Specification)

## Purpose

This document defines the **admissible motif-local term classes** used in the Network Potential Framework.

The intent is not to define an exhaustive ontology of network motifs.

Instead, it defines the subset of local potential terms that are **admissible for the framework** because their cross-partial structure is compatible with the structural curvature layer, in particular:

- S1 — Structural Z-Matrix Theorem (`docs/theorems/framework/S1_structural_zmatrix_theorem.md`).

This document therefore functions as a bridge between:

- potential construction rules (what terms may appear in `Φ(w, θ)`), and
- operator structure guarantees (sign structure of `H(w, θ)` and `C(w, θ)`).

All definitions in this document must be consistent with the canonical objects in:

- `docs/foundations/core_objects.md`.

------------------------------------------------------------------------

# 1. Canonical objects and scope

State and parameter variables:

- `w ∈ ℝⁿ`
- `θ ∈ ℝⁿ`

Relational potential:

- `Φ(w, θ)`

Admissible potential domain:

- `Ω_Φ ⊆ W × Θ`

Hessian and coupling operator (B1):

- `H(w, θ) := ∇²_{ww} Φ(w, θ)`
- `C(w, θ) := −H(w, θ)`

All admissibility conditions below are understood as conditions on `Ω_Φ` under the regularity hypothesis `Φ ∈ C²_w(Ω_Φ)` (A1).

------------------------------------------------------------------------

# 2. Admissible decomposition requirement (structural)

A relational potential `Φ(w, θ)` is said to satisfy the **admissible motif decomposition requirement** if it can be written as a finite sum of local terms of the form:

`Φ(w, θ) = Σ_{e ∈ E} φ_e(w_e, θ) + Σ_{m ∈ M} ψ_m(w_{S_m}, θ)`,

where:

- each `φ_e` is an edge-local term depending on a single state coordinate `w_e` (and possibly on `θ`),
- each `ψ_m` is a motif-local term depending on a finite coordinate subset `S_m ⊆ {1, …, n}` and on `θ`,
- `E` and `M` are finite index sets.

This requirement is a structural hypothesis used by S1.

------------------------------------------------------------------------

# 3. Admissibility criteria for motif-local terms

A motif-local term `ψ_m(w_{S_m}, θ)` is **admissible** (for the purpose of S1) if it satisfies the following cross-partial sign condition:

For every pair of distinct indices `i ≠ j`:

- if `{i, j} ⊆ S_m`, then `∂²ψ_m/(∂w_i ∂w_j) ≥ 0` on `Ω_Φ`,
- if at least one of `i, j` is not in `S_m`, then the contribution of `ψ_m` to `∂²Φ/(∂w_i ∂w_j)` is zero (equivalently, `∂²ψ_m/(∂w_i ∂w_j) = 0`).

This criterion is stated in terms of `H` rather than `C`. By B1, it is equivalent to the coupling sign condition:

- for `i ≠ j`, `C_{ij}^{(m)}(w, θ) ≤ 0` for the motif-level coupling contribution.

------------------------------------------------------------------------

# 4. Initial admissible motif classes (taxonomy)

This section defines the initial admissible term classes and the sign-lemma targets required to use them in S1.

## 4.1 Class A — Edge-local terms

A term is edge-local if it has the form `φ_e(w_e, θ)` for some single coordinate `w_e`.

### Required sign-lemma target (Class A)

For every edge-local term and every pair of distinct indices `i ≠ j`:

- `∂²φ_e/(∂w_i ∂w_j) = 0`.

Equivalently, edge-local terms contribute only to the diagonal of `H(w, θ)`.

## 4.2 Class B — Brokerage / interaction motifs

A term is a brokerage/interaction motif if it has the form `ψ_m(w_{S_m}, θ)` where `S_m` is a small incident set (for example, representing local interaction around a node or a short path).

In its initial admissible form for S1 certification, Class B terms are restricted to **finite sums of pairwise interaction functions** on their support.

Concretely, an admissible Class B term is any motif-local term expressible as:

`ψ_m(w_{S_m}, θ) = Σ_{(i,j) ∈ P_m} g_{ij}(w_i, w_j, θ)`,

where:

- `P_m` is a finite set of unordered index pairs with `{i, j} ⊆ S_m`,
- each `g_{ij}` is `C²` with respect to `(w_i, w_j)` on `Ω_Φ`.

### Required sign-lemma target (Class B)

For every such term and all `i ≠ j` with `{i, j} ⊆ S_m`:

- `∂²ψ_m/(∂w_i ∂w_j) ≥ 0`.

In the sufficient-form Class B family above, it is sufficient to require that for each pairwise component `g_{ij}`:

- `∂²g_{ij}/(∂w_i ∂w_j) ≥ 0` on `Ω_Φ`.

## 4.3 Class C — Redundancy / closure motifs

A term is a redundancy/closure motif if it has the form `ψ_m(w_{S_m}, θ)` where `S_m` corresponds to a local closure structure (for example, a triangle/triadic closure neighbourhood or another bounded local closure pattern).

In its initial admissible form for S1 certification, Class C terms are restricted to **finite sums of gated triadic product monomials**.

Concretely, an admissible Class C term is any motif-local term expressible as a finite sum of terms of the form:

`a_α(θ) w_{ij}^{p_α} w_{ik}^{q_α} κ_α`,

where:

- `a_α(θ) ≥ 0` on `Ω_Φ`,
- `κ_α ≥ 0` is a topology-only gate (for example an adjacency indicator),
- `p_α, q_α > 0`, and the term is `C²_w` on `Ω_Φ`.

### Required sign-lemma target (Class C)

For every such term and all `i ≠ j` with `{i, j} ⊆ S_m`:

- `∂²ψ_m/(∂w_i ∂w_j) ≥ 0`.

## 4.4 Candidate admissible local families (Core Thesis extraction)

This subsection records concrete local term families extracted from:

- `docs/research_papers/Paper_CoreThesis/Network-Potential-and-Relational-Optimisation-mathematics-thesis.md`.

These items are recorded here as *candidate admissible building blocks* because they are explicit motif-local terms whose cross-partials can be analysed directly.

### Edge-local cohesion family

For a fixed exponent `p > 0`, the cohesion family uses edge-local monomials of the form:

- `w_e^p`.

### Edge-local brokerage family

For a fixed exponent `p > 0` and topology-only constants `B_e ∈ [0,1]`, the brokerage family uses edge-local terms of the form:

- `(1 - w_e)^p B_e`.

### Closure product family

For a fixed exponent `p > 0` and adjacency indicators `1_E(j,k) ∈ {0,1}`, the closure redundancy family uses motif-local product terms of the form:

- `w_{ij}^p w_{ik}^p 1_E(j,k)`.

These terms are supported on a bounded neighbourhood around a node and represent the prototypical admissible closure interaction motif building block.

## 4.5 Deferred composition layer (not automatically admissible for S1)

Some model instantiations form node-level or global potentials by composing local structural functionals with scalar functions (for example, `log(1 + ·)` and signed variants such as `−log(1 + ·)`).

Such *outer scalar compositions are not automatically admissible for S1*.

Admission of a composed term into the S1 pipeline requires a separate closure lemma establishing that the composition preserves the off-diagonal cross-partial sign condition required by Section 3 (or else that the composed term can be re-expressed as a sum of admissible motif-local terms that satisfy Section 3).

------------------------------------------------------------------------

# 5. Relationship to S1

S1 (`docs/theorems/framework/S1_structural_zmatrix_theorem.md`) assumes a motif-local decomposition and assumes the sign condition `∂²ψ_m/(∂w_i ∂w_j) ≥ 0` for all admissible motif terms.

The role of this taxonomy is to replace the informal hypothesis:

- “Assume cross-partials are nonnegative,”

with a framework-level admissibility statement:

- “Assume `Φ` decomposes into admissible terms from the classes above, and that each class satisfies its sign lemma target.”

Under these conditions, for all `i ≠ j`:

- `H_{ij}(w, θ) ≥ 0`, hence
- `C_{ij}(w, θ) ≤ 0`,

so `C(w, θ)` is a Z-matrix.

------------------------------------------------------------------------

# 5.1 Relationship to S2 (magnitude layer)

S2 (`docs/theorems/framework/S2_structural_diagonal_dominance_theorem.md`) is a magnitude-layer theorem. In addition to the S1 sign admissibility conditions above, S2 requires **magnitude bounds** that allow explicit construction of row-wise diagonal dominance margins.

These magnitude bounds are not implied by the S1 admissibility criteria and must be supplied as additional admissibility conditions on a certified region `Ω_{S2} ⊆ Ω_Φ`.

## S2 magnitude admissibility addendum (framework specification)

Fix a certified region `Ω_{S2} ⊆ Ω_Φ` on which S2 is to be applied.

In the initial framework closure, `Ω_{S2}` is taken to be a bounded state region together with certified bounds on any `θ`-dependent amplitude functions that appear in admitted Class A/B/C families.

### Initial B2-certified region (sufficient form)

Assume the state is bounded coordinatewise:

`0 ≤ w_i ≤ 1` for all `i`.

Assume that every admitted `θ`-dependent amplitude function that appears in a Class A/B/C term has certified lower/upper bounds on `Ω_{S2}`.

1. **Class A diagonal curvature lower bounds**

   For each coordinate `i`, the total Class A contribution to the coupling diagonal entry `C_{ii}(w, θ)` is required to admit a certified lower bound on `Ω_{S2}`.

   Concretely, for each edge-local term `φ_e(w_e, θ)`, define its diagonal curvature contribution:

   `λ_e(w, θ) := −∂²φ_e/(∂w_e²)`.

   S2-admissible instantiations must provide certified functions `\underline{λ}_e(w, θ)` such that on `Ω_{S2}`:

   `λ_e(w, θ) ≥ \underline{λ}_e(w, θ) ≥ 0`.

2. **Class B off-diagonal magnitude upper bounds**

   For each pairwise interaction component `g_{ij}(w_i, w_j, θ)` admitted under Class B, define its off-diagonal coupling magnitude contribution:

   `β_{ij}(w, θ) := −C_{ij}^{(g)}(w, θ) = ∂²g_{ij}/(∂w_i ∂w_j)`.

   Since Class B sign admissibility already requires `β_{ij}(w, θ) ≥ 0`, S2 magnitude admissibility additionally requires a certified upper bound `\overline{β}_{ij}(w, θ)` such that on `Ω_{S2}`:

   `0 ≤ β_{ij}(w, θ) ≤ \overline{β}_{ij}(w, θ)`.

3. **Class C off-diagonal magnitude upper bounds**

   For each gated triadic monomial `a_α(θ) w_{ij}^{p_α} w_{ik}^{q_α} κ_α` admitted under Class C, define its off-diagonal coupling magnitude contribution for the incident pair `(ij, ik)`:

   `γ_α(w, θ) := −C_{ij,ik}^{(α)}(w, θ) = ∂²/(∂w_{ij} ∂w_{ik}) [a_α(θ) w_{ij}^{p_α} w_{ik}^{q_α} κ_α]`.

   Since Class C sign admissibility already requires `γ_α(w, θ) ≥ 0` on `Ω_Φ`, S2 magnitude admissibility additionally requires a certified upper bound `\overline{γ}_α(w, θ)` such that on `Ω_{S2}`:

   `0 ≤ γ_α(w, θ) ≤ \overline{γ}_α(w, θ)`.

4. **Locality / incidence bookkeeping for row-sums (B2)**

   To globalise the magnitude bounds into a row-sum bound, S2 instantiations must supply neighborhood sets `N(i)` as in B2 such that:

   - if `j ∉ N(i)`, then `C_{ij}(w, θ) = 0` on `Ω_{S2}`.

   In particular, the row off-diagonal absolute sum reduces to a finite sum over `j ∈ N(i) \ {i}`.

### B2 closed-form bounds for the initial admitted families

The following closed-form derivative bounds complete the initial S2 magnitude layer for the concrete candidate families recorded in Section 4.4.

#### Class A (edge-local) — negative monomial / quadratic families

For each coordinate `e`, admit edge-local cohesion terms of the form:

`φ_e(w_e, θ) = −a_e(θ) w_e^{p}`

with `p ≥ 2` and amplitude bounds on `Ω_{S2}`:

`a_e(θ) ≥ \underline{a}_e > 0`.

Then

`λ_e(w, θ) = −∂²φ_e/(∂w_e²) = a_e(θ) p(p−1) w_e^{p−2}`.

On `Ω_{S2}` this implies the certified diagonal lower bound:

`λ_e(w, θ) ≥ \underline{a}_e p(p−1) w_e^{p−2} ≥ 0`.

In particular, for the quadratic case `p = 2`:

`λ_e(w, θ) = 2 a_e(θ) ≥ 2 \underline{a}_e`.

#### Class B (interaction) — bilinear product family

For the initial S2 closure, restrict admissible Class B pairwise components to the bilinear family:

`g_{ij}(w_i, w_j, θ) = b_{ij}(θ) w_i w_j`

with amplitude bounds on `Ω_{S2}`:

`0 ≤ b_{ij}(θ) ≤ \overline{b}_{ij}`.

Then

`β_{ij}(w, θ) = ∂²g_{ij}/(∂w_i ∂w_j) = b_{ij}(θ)`

so on `Ω_{S2}` the certified upper bound is:

`0 ≤ β_{ij}(w, θ) ≤ \overline{b}_{ij}`.

#### Class C (closure) — gated closure product family

For the closure product family, admit triadic terms of the form:

`a(θ) w_{ij}^{p} w_{ik}^{q} κ`

with `p, q ≥ 1`, gate `κ ∈ {0,1}`, and amplitude bounds on `Ω_{S2}`:

`0 ≤ a(θ) ≤ \overline{a}`.

Then the incident mixed partial satisfies:

`γ(w, θ) = ∂²/(∂w_{ij} ∂w_{ik}) [a(θ) w_{ij}^{p} w_{ik}^{q} κ] = a(θ) p q w_{ij}^{p−1} w_{ik}^{q−1} κ`.

On `Ω_{S2}` this yields the certified upper bound:

`0 ≤ γ(w, θ) ≤ \overline{a} p q`.

------------------------------------------------------------------------

# 6. Decomposition completeness requirement

For S1 to apply at the framework level, it must be established that:

- every admissible relational potential `Φ(w, θ)` used by the framework satisfies the admissible decomposition requirement, and
- every motif-local term in this decomposition belongs to one of the admissible motif classes in Section 4.

This “completeness” requirement is a structural specification: it constrains future potential designs and provides the checklist needed to certify S1 for new model instantiations.

------------------------------------------------------------------------

# 7. Remaining work (to complete certification)

1. Maintain the admissible motif taxonomy (this document) and the admissible potential grammar.
2. Ensure that model instantiations decompose into the admitted term families.
3. (Optional) Align the locality bookkeeping with B2 so that the sparsity pattern implied by bounded `S_m` sets is explicit for downstream S2 bounds.
