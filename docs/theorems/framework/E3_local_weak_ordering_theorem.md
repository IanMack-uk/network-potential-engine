# E3 — Local Weak Ordering Theorem

## Purpose

This theorem exports a local weak (coordinatewise) ordering guarantee for the equilibrium map w*(θ) along a certified parameter segment.

It is the segment-level ordering statement obtained by integrating pointwise response positivity (D3) along a segment that remains inside an admissible region (E1), with segment containment certified by E2.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of A1, and let w*(θ) be an equilibrium branch when licensed by A2/A3/C1.

Let R ⊆ Θ be an admissible region as in E1.

Let θ, θ' ∈ R and define the segment

γ(t) := θ + t(θ' − θ),  t ∈ [0, 1].

------------------------------------------------------------------------

# 2. Hypotheses

Assume:

1. Segment containment: γ([0, 1]) ⊆ R (certified by E2).
2. Endpoint order: θ' \succeq θ coordinatewise.
3. Pointwise response positivity on R: for every ϑ ∈ R,

   D_θ w*(ϑ) \ge 0

   entrywise (as provided pointwise by D3 on R).

------------------------------------------------------------------------

# 3. Theorem statement

Under the hypotheses above,

w*(θ') \succeq w*(θ)

coordinatewise.

------------------------------------------------------------------------

# 4. Proof

Along the segment γ, the fundamental theorem of calculus gives

w*(θ') − w*(θ) = \int_0^1 D_θ w*(γ(t)) (θ' − θ)\,dt.

For every t ∈ [0, 1], γ(t) ∈ R, hence D_θ w*(γ(t)) is entrywise nonnegative.

Since θ' − θ \succeq 0, the integrand is entrywise nonnegative for every t, and therefore the integral is entrywise nonnegative. This yields w*(θ') − w*(θ) \succeq 0.

------------------------------------------------------------------------

# 5. TDC model instantiation (certification target)

In the TDC theorem (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), Theorem 17 proves weak ordering on the admissible region ℛ under segment containment, using Proposition 15 to guarantee pointwise response positivity along the segment.

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

TDC-specific supporting checks are implemented in:

- `src/network_potential_engine/scripts/check_E3_tdc_local_weak_ordering.py`
- `tests/test_E3_tdc_local_weak_ordering.py`
