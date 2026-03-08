# D1 — Inverse Positivity Theorem

## Purpose

This theorem exports a sufficient condition under which the inverse of the coupling operator is **entrywise nonnegative**.

It is the first sign-control theorem used downstream to convert the response identity (C1) into monotone comparative statics (D3/E-layer), but it does not itself assert anything about mixed-block positivity or ordering.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let the coupling operator be

C(w, θ) = −H(w, θ)

as exported by

B1 — Hessian–Coupling Theorem.

In response analysis one works with the equilibrium-evaluated coupling operator

C(θ) := C(w*(θ), θ)

when an equilibrium branch w*(θ) is licensed by A2/A3/C1.

------------------------------------------------------------------------

# 2. Definitions (matrix classes)

Let C be a real square matrix.

- C is called a **Z-matrix** if its off-diagonal entries are nonpositive.
- C is called a **nonsingular M-matrix** if it is a Z-matrix and belongs to the classical M-matrix class with a nonnegative inverse.

This theorem uses the following classical matrix-analysis fact:

- A nonsingular M-matrix has an entrywise nonnegative inverse.

------------------------------------------------------------------------

# 3. Theorem statement (inverse positivity)

Let θ be a parameter value such that the equilibrium-evaluated coupling matrix C(θ) is defined.

Assume C(θ) is a **nonsingular M-matrix**.

Then

C(θ)^{-1} \ge 0

entrywise.

------------------------------------------------------------------------

# 4. Corollary (strict diagonal dominance sufficient condition)

Assume C(θ) is a Z-matrix and is **strictly diagonally dominant by rows**, i.e. for each row i,

C(θ)_{ii} > \sum_{j \ne i} |C(θ)_{ij}|.

Then C(θ) is a nonsingular M-matrix, and therefore C(θ)^{-1} \ge 0 entrywise.

------------------------------------------------------------------------

# 5. Proof

1. By hypothesis, C(θ) is a nonsingular M-matrix.
2. By the classical M-matrix theorem, a nonsingular M-matrix has an entrywise nonnegative inverse.
3. Therefore C(θ)^{-1} \ge 0 entrywise.

For the corollary, strict diagonal dominance of a Z-matrix is a standard sufficient condition for nonsingular M-matrix structure.

------------------------------------------------------------------------

# 6. TDC model instantiation (certification target)

In the TDC model (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), the coupling matrix C(θ) is tridiagonal with off-diagonal entries −c \le 0, hence it is a Z-matrix.

The TDC theorem proves that if

q + \alpha\,\theta_i > 0 \quad \text{for all } i,

then C(θ) is strictly diagonally dominant (row margins q + \alpha\theta_i) and therefore is a nonsingular M-matrix.

Consequently, the conclusion of D1 holds in TDC:

C(θ)^{-1} \ge 0.

This matches Lemma 7–8 of the TDC formal theorem document.

------------------------------------------------------------------------

# 7. Computational evidence (supporting)

TDC-specific supporting checks of the analytic margin/bound machinery are implemented in:

- `src/network_potential_engine/theorem/tdc_bounds.py`
- `tests/test_tdc_bounds.py`
- `src/network_potential_engine/scripts/check_tdc_bounds.py`
