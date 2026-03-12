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

### A1.5 Mixed-derivative licensing (explicit)

Downstream response theorems require differentiability of the equilibrium operator

F(w, θ) = ∇_w Φ(w, θ)

with respect to θ. Accordingly, in addition to A1.3–A1.4 we assume that the equilibrium operator is continuously differentiable in both variables on the admissible domain:

F ∈ C¹(Ω_Φ).

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

exists and is continuous.

### 3.4 Coupling operator

C(w, θ) = −H(w, θ)

is therefore well‑defined.

------------------------------------------------------------------------

# 4. Licensing of Later Objects

The regularity assumptions guarantee that the derivative objects used
later exist.

  Object      Licensed by
  ----------- --------------------------
  F(w,θ)      C²_w regularity
  H(w,θ)      C²_w regularity
  H_wθ(w,θ)   F ∈ C¹(Ω_Φ) (explicit mixed-derivative licensing)

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

------------------------------------------------------------------------

# 8. Proof

## 8.1 Domain Non‑Emptiness

Assume W and Θ are non‑empty subsets of ℝⁿ.

Since the admissible potential domain satisfies Ω_Φ ⊆ W × Θ and the
theorem is asserted on Ω_Φ, it is sufficient to exhibit that W × Θ is
non‑empty.

Pick any w₀ ∈ W and any θ₀ ∈ Θ (possible because W and Θ are non‑empty).
Then (w₀, θ₀) ∈ W × Θ, so W × Θ ≠ ∅.

In the common ambient choice W = ℝⁿ and Θ = ℝⁿ, one explicit admissible
point is (w₀, θ₀) = (0, 0), hence Ω_Φ is non‑empty whenever Ω_Φ = W × Θ.

## 8.2 Potential Well‑Definedness

By assumption A1.1 (Finite valuation), for every (w, θ) ∈ Ω_Φ the value
Φ(w, θ) is finite.

In particular, when Φ is given by a finite algebraic expression in the
components of (w, θ) involving only finitely many arithmetic operations
(addition, subtraction, multiplication, and scalar division by nonzero
constants), the value Φ(w, θ) is well‑defined and finite for all
(w, θ) where the expression is defined.

For the TDC instantiation in Section 6, Φ_tdc(w, θ) is a polynomial in
the entries of w and θ, hence is finite for all (w, θ) ∈ ℝⁿ × ℝⁿ.

## 8.3 Continuity

Assumption A1.2 states that Φ ∈ C⁰(Ω_Φ), i.e. Φ is continuous on Ω_Φ.

Moreover, in the common case where Φ is algebraic in (w, θ) and in
particular when Φ is polynomial, Φ is continuous on its domain of
definition. Therefore Φ ∈ C⁰(Ω_Φ) holds under the stated regularity.

## 8.4 State Derivative Existence

Assumption A1.3 states that Φ ∈ C²_w(Ω_Φ). By definition of C²
regularity in the state variables, all first partial derivatives
∂Φ/∂w_i and all second mixed partial derivatives ∂²Φ/(∂w_i ∂w_j) exist on
Ω_Φ and depend continuously on (w, θ).

Define the equilibrium operator

F(w, θ) = ∇\_w Φ(w, θ)

and the Hessian

H(w, θ) = ∇²_ww Φ(w, θ).

These are exactly the canonical objects recorded in
`docs/foundations/core_objects.md`. The C²_w assumption implies that F
and H are well‑defined on Ω_Φ, and that F and H are continuous on Ω_Φ.

## 8.5 Mixed Derivative Block

Assumptions A1.3 and A1.4 state that Φ ∈ C²_w(Ω_Φ) and Φ ∈ C¹_θ(Ω_Φ).

Because Φ is once continuously differentiable in θ and twice
continuously differentiable in w, the map (w, θ) ↦ ∇\_w Φ(w, θ) is well
defined on Ω_Φ and has a well‑defined θ‑derivative wherever the mixed
partials exist. In particular, under these regularity hypotheses the
mixed derivative block

H_wθ(w, θ) = D_θ (∇\_w Φ(w, θ))

exists on Ω_Φ.

## 8.6 Coupling Operator Definition

By Section 8.4, H(w, θ) = ∇²_ww Φ(w, θ) is well‑defined on Ω_Φ.

 Define the coupling operator
 
 C(w, θ) = −H(w, θ).
 
 This is therefore well‑defined wherever H exists.

 No claim is made here about invertibility, M‑matrix structure, or
 positivity of C; such properties appear only in later theorems.

## 8.7 Compatibility with Admissibility Taxonomy

The admissibility taxonomy in `docs/foundations/admissibility_taxonomy.md`
organizes domains for the framework objects.

This theorem A1 establishes the well‑posedness and differentiability of
Φ(w, θ) only on the admissible potential domain Ω_Φ. In particular, all
claims in Sections 3–6 and the definitions in Sections 8.4–8.6 are
understood as statements on Ω_Φ.

## 8.8 TDC Model Certification

For the TDC model, the potential Φ_tdc(w, θ) in Section 6 is a
polynomial in w and θ.

Polynomial functions are C^∞ on ℝⁿ × ℝⁿ.

Therefore

Φ_tdc ∈ C^∞(ℝⁿ × ℝⁿ)

and all derivative objects F, H, H_wθ, C exist globally for the TDC
instantiation.
