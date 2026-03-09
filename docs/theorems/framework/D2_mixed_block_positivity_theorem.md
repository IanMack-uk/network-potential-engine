# D2 — Mixed-Block Positivity Theorem

## Purpose

This theorem exports a sufficient condition under which the mixed derivative block

H_{wθ}(w*(θ), θ)

is **entrywise nonnegative**.

It is the second sign-control theorem used downstream to convert the response identity (C1) into response positivity (D3), but it does not itself assert anything about inverse positivity of C(θ)^{-1} or ordering consequences.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let the equilibrium operator be

F(w, θ) = ∇_w Φ(w, θ)

and let w*(θ) be an equilibrium branch satisfying

F(w*(θ), θ) = 0

when licensed by A2/A3b/C1.

Define the mixed derivative block

H_{wθ}(w, θ) = D_θ(∇_w Φ(w, θ))

as in `docs/foundations/core_objects.md`.

------------------------------------------------------------------------

# 2. Theorem statement (mixed-block positivity)

Let θ be a parameter value such that the equilibrium-evaluated mixed block H_{wθ}(w*(θ), θ) is defined.

Assume

H_{wθ}(w*(θ), θ) \ge 0

entrywise.

Then the mixed-block positivity hypothesis needed for the downstream response-positivity theorem (D3) holds at θ.

------------------------------------------------------------------------

# 3. Proof

This theorem is an interface theorem: it exports the mixed-block sign condition as a standalone hypothesis/conclusion at the point where the response identity factorises.

No further argument is required beyond the definition of the object being signed and its evaluation at equilibrium.

------------------------------------------------------------------------

# 4. TDC model instantiation (certification target)

In the TDC model (`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`), the mixed derivative block has the explicit form

H_{wθ}(w, θ) = diag(1 − α w_i).

Therefore, at equilibrium,

H_{wθ}(w*(θ), θ) \ge 0

is equivalent to the coordinatewise inequalities

1 − α w_i*(θ) \ge 0 \quad \text{for all } i.

This matches Proposition 4 and Lemma 9 of the TDC formal theorem document.

------------------------------------------------------------------------

# 5. Computational evidence (supporting)

TDC-specific supporting checks of the mixed-block condition are implemented in:

- `src/network_potential_engine/theorem/tdc_conditions.py`
- `tests/test_tdc_conditions.py`
- `src/network_potential_engine/scripts/check_tdc_conditions.py`
