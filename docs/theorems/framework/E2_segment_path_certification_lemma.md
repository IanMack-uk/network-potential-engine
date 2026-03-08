# E2 — Segment / Path Certification Lemma

## Purpose

This lemma exports a checkable certificate implying that a full parameter segment remains inside a certified admissible region (E1).

It does not assert any ordering conclusion; it only certifies that the pointwise hypotheses needed for response positivity remain valid along the full segment.

------------------------------------------------------------------------

# 1. Setup

Let R ⊆ Θ be an admissible region as in E1. Let θ^L, θ^R ∈ Θ and define the line segment

θ(t) := θ^L + t(θ^R − θ^L),  t ∈ [0, 1].

------------------------------------------------------------------------

# 2. Lemma statement

Assume there exists a computable certificate, depending only on θ^L and θ^R, that implies

θ(t) ∈ R  for all t ∈ [0, 1].

Then all pointwise conclusions that hold for parameters in R (in particular the response positivity conclusion of D3) hold uniformly along the full segment.

------------------------------------------------------------------------

# 3. Proof

If the certificate guarantees θ(t) ∈ R for all t ∈ [0, 1], then for every t the pointwise hypotheses required by E1/D3 hold at θ(t). Therefore D3 holds pointwise for all t along the segment.

------------------------------------------------------------------------

# 4. TDC model instantiation (certification target)

In the TDC theorem (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), define

\[
 m_{\mathrm{seg}} := \min_i\bigl(q + \alpha\min(\theta^L_i, \theta^R_i)\bigr),
 \qquad
 M_{\mathrm{seg}} := \max(\|\theta^L\|_\infty, \|\theta^R\|_\infty).
\]

Lemma 16 proves that if

\[
 m_{\mathrm{seg}} > 0
 \qquad\text{and}\qquad
 \alpha\,\frac{M_{\mathrm{seg}}}{m_{\mathrm{seg}}} \le 1,
\]

then the full segment [θ^L, θ^R] is contained in the TDC admissible region ℛ (Definition 14).

------------------------------------------------------------------------

# 5. Computational evidence (supporting)

TDC-specific supporting checks are implemented in:

- `src/network_potential_engine/theorem/tdc_segment.py`
- `src/network_potential_engine/scripts/check_tdc_segment.py`
- `tests/test_tdc_segment.py`
