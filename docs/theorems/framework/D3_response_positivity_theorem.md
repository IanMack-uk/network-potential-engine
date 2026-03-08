# D3 — Response Positivity Theorem

## Purpose

This theorem exports entrywise nonnegativity of the equilibrium response operator

D_θ w*(θ)

under the factorised response identity (C1) and the two sign hypotheses exported by D1 and D2.

No claim is made here about admissible regions or path/segment arguments; those belong to the E-layer.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let w*(θ) be an equilibrium branch satisfying

F(w*(θ), θ) = 0

when licensed by A2/A3/C1.

Let the coupling operator be C(w, θ) = −H(w, θ) (B1), and define the equilibrium-evaluated coupling matrix

C(θ) := C(w*(θ), θ).

Let the mixed derivative block be

H_{wθ}(w, θ) = D_θ(∇_w Φ(w, θ))

as in `docs/foundations/core_objects.md`.

------------------------------------------------------------------------

# 2. Hypotheses

Assume the response identity of C1 holds at θ:

D_θ w*(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ).

Assume further:

1. C(θ)^{-1} \ge 0 entrywise (D1).
2. H_{wθ}(w*(θ), θ) \ge 0 entrywise (D2).

------------------------------------------------------------------------

# 3. Theorem statement

Under the hypotheses above,

D_θ w*(θ) \ge 0

entrywise.

------------------------------------------------------------------------

# 4. Proof

By C1,

D_θ w*(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ).

By D1 and D2, both factors on the right-hand side are entrywise nonnegative.

Since the product of two entrywise nonnegative matrices is entrywise nonnegative, it follows that D_θ w*(θ) \ge 0 entrywise.

------------------------------------------------------------------------

# 5. TDC model instantiation (certification target)

In the TDC model (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), response positivity is concluded pointwise by combining:

- inverse positivity of C(θ)^{-1} (Lemma 8), and
- mixed-block positivity of H_{wθ}(w*(θ), θ) (Lemma 9),

in the response identity (Proposition 6), yielding Corollary 10.

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

TDC-specific supporting checks are implemented in:

- `src/network_potential_engine/scripts/check_D3_tdc_response_positivity.py`
- `tests/test_D3_tdc_response_positivity.py`
