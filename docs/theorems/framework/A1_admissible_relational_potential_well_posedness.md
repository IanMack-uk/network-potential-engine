# A1 --- Admissible Relational Potential Well-Posedness

## Purpose

This theorem establishes the **basic mathematical well‑posedness** of
the relational potential framework.

It certifies that:

-   the potential is defined on the admissible domain
-   the potential has the regularity required for derivative operations
-   the derivative objects used in later theorems are well‑defined

This theorem therefore **licenses all derivative objects used in the
framework**.

The canonical objects referenced in this theorem are defined in:

`docs/foundations/core_objects.md`

The admissibility taxonomy is defined in:

`docs/foundations/admissibility_taxonomy.md`

------------------------------------------------------------------------

# 1. Domain Setup

Let

Ω = ℝⁿ × ℝⁿ

denote the ambient domain for the state and parameter variables.

Let

W ⊆ ℝⁿ\
Θ ⊆ ℝⁿ

denote the admissible state and parameter domains.

Define the admissible potential domain

Ω_Φ ⊆ W × Θ

on which the relational potential

Φ(w, θ)

is defined.

------------------------------------------------------------------------

# 2. Regularity Assumptions

Assume the potential

Φ : Ω_Φ → ℝ

satisfies the following conditions.

### A1.1 Finite valuation

For all (w, θ) ∈ Ω_Φ, the value Φ(w, θ) is finite.

### A1.2 Continuity

The potential is continuous on Ω_Φ:

Φ ∈ C⁰(Ω_Φ)

### A1.3 State differentiability

The potential is twice continuously differentiable in the state
variables:

Φ ∈ C²_w(Ω_Φ)

Thus

∂Φ/∂w_i\
∂²Φ/(∂w_i ∂w_j)

exist and are continuous.

### A1.4 Parameter differentiability

The potential is continuously differentiable in the parameters:

Φ ∈ C¹_θ(Ω_Φ)

Thus

∂Φ/∂θ_i

exists and is continuous.

------------------------------------------------------------------------

# 3. Consequences

Under the assumptions above, the following framework objects are
well‑defined on Ω_Φ.

### 3.1 Equilibrium operator

F(w, θ) = ∇\_w Φ(w, θ)

exists and is continuous.

### 3.2 Hessian

H(w, θ) = ∇²_ww Φ(w, θ)

exists and is continuous.

### 3.3 Mixed derivative block

H_wθ(w, θ) = D_θ (∇\_w Φ(w, θ))

exists.

### 3.4 Coupling operator

C(θ) = −H(w, θ)

is therefore well‑defined.

------------------------------------------------------------------------

# 4. Licensing of Later Objects

The regularity assumptions guarantee that the derivative objects used
later exist.

  Object      Licensed by
  ----------- --------------------------
  F(w,θ)      C²_w regularity
  H(w,θ)      C²_w regularity
  H_wθ(w,θ)   C¹_θ and C²_w regularity

Later theorems may impose stronger conditions such as invertibility or
positivity.

------------------------------------------------------------------------

# 5. Boundary Considerations

This theorem does **not** claim:

-   equilibrium existence
-   uniqueness of equilibria
-   invertibility of the Hessian
-   positivity properties

Those properties are established in later theorems.

------------------------------------------------------------------------

# 6. TDC Model Instantiation

For the Theta‑Dependent Curvature (TDC) model the potential is

Φ_tdc(w, θ) = Σ_i θ_i w_i − ½ Σ_i (q + α θ_i) w_i² − (c/2)
Σ\_{i=1}\^{n−1}(w_i − w\_{i+1})²

This function is polynomial in w and θ.

Therefore

Φ_tdc ∈ C\^∞(ℝⁿ × ℝⁿ).

Consequently all derivative objects used in the framework are globally
well‑defined for the TDC model.

------------------------------------------------------------------------

# 7. Conclusion

Under the admissibility conditions above, the relational potential

Φ(w, θ)

is mathematically well‑posed and possesses the differentiability
required for the derivative operators used throughout the framework.

This theorem therefore licenses the use of the objects

F, H, H_wθ, C

in all subsequent equilibrium, response, and ordering theorems.
