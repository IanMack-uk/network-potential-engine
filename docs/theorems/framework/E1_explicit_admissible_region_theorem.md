# E1 — Explicit Admissible-Region Theorem

## Purpose

This theorem exports an explicit admissible region of parameter values on which the pointwise sign-controlled response hypotheses (D1 and D2) hold, and therefore response positivity (D3) holds pointwise.

This theorem does not make any path/segment certification claim (E2) and does not make any ordering claim (E3).

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let w*(θ) be an equilibrium branch when licensed by A2/A3/C1.

Let the equilibrium response identity (C1) hold at θ:

D_θ w*(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ),

where C(θ) = C(w*(θ), θ) and H_{wθ}(w*(θ), θ) are as in `docs/foundations/core_objects.md`.

------------------------------------------------------------------------

# 2. Admissible region definition (framework)

Let R ⊆ Θ be a set of parameter values such that for every θ ∈ R:

1. C(θ)^{-1} \ge 0 entrywise.
2. H_{wθ}(w*(θ), θ) \ge 0 entrywise.

------------------------------------------------------------------------

# 3. Theorem statement

If θ ∈ R, then

D_θ w*(θ) \ge 0

entrywise.

------------------------------------------------------------------------

# 4. Proof

If θ ∈ R, then the hypotheses of D1 and D2 hold at θ.

By D3, combining C1 with D1 and D2 yields D_θ w*(θ) \ge 0 entrywise.

------------------------------------------------------------------------

# 5. TDC model instantiation (certification target)

In the TDC theorem (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), the admissible region is defined explicitly (Definition 14) as

\[
\mathcal R := \{\theta : m(\theta) > 0 \text{ and } \alpha\,\|\theta\|_\infty/m(\theta) \le 1\},
\qquad m(\theta) := \min_i (q + \alpha\theta_i).
\]

Proposition 15 proves that for θ ∈ \mathcal R the pointwise sign-controlled response properties hold.

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

TDC-specific supporting checks are implemented in:

- `src/network_potential_engine/theorem/tdc_region.py`
- `src/network_potential_engine/scripts/check_tdc_region.py`
- `tests/test_tdc_region.py`
